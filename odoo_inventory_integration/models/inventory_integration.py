from odoo import models, fields, api
import requests
import json
import logging
import os

_logger = logging.getLogger(__name__)

class InventoryIntegration(models.Model):
    _inherit = 'x_inventory_data'

    def _get_api_base_url(self):
        """Получаем базовый URL API из переменных окружения или используем по умолчанию"""
        # Пробуем получить из переменных окружения Odoo
        base_url = os.environ.get('INVENTORY_API_URL') 
        
        # Если нет в переменных, пробуем получить из параметров системы Odoo
        if not base_url:
            base_url = self.env['ir.config_parameter'].sudo().get_param(
                'inventory_integration.api_url',
                'https://odoo-render-setup.onrender.com'  # значение по умолчанию
            )
        
        _logger.info(f"Using API base URL: {base_url}")
        return base_url

    @api.model
    def import_from_api(self):
        """Метод для импорта данных из внешнего API"""
        _logger.info("Starting API import process")
        
        records = self.search([('x_api_token', '!=', False)])
        _logger.info(f"Found {len(records)} records with API tokens")
        
        base_url = self._get_api_base_url()
        
        for record in records:
            try:
                if not record.x_api_token:
                    continue
                    
                _logger.info(f"Importing data for inventory: {record.x_name}")
                
                # Вызов вашего API с динамическим URL
                url = f"{base_url}/api/odoo/{record.x_api_token}/aggregateddata"
                _logger.info(f"API URL: {url}")
                
                # Добавляем обработку таймаутов и ошибок сети
                response = requests.get(url, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    _logger.info(f"API response received for {record.x_name}")
                    
                    # Сохраняем агрегированные данные
                    updates = {
                        'x_total_count': data.get('aggregations', {}).get('total_count', 0),
                        'x_field_definitions': json.dumps(data.get('inventory', {}).get('fields', []), ensure_ascii=False),
                    }
                    
                    # Сохраняем агрегации по типам
                    aggregations = data.get('aggregations', {}).get('fields_aggregation', {})
                    numeric_aggr = {}
                    text_aggr = {}
                    boolean_aggr = {}
                    
                    for field_name, aggr_data in aggregations.items():
                        field_type = aggr_data.get('type', '')
                        if field_type == 'number':
                            numeric_aggr[field_name] = aggr_data
                        elif field_type == 'string':
                            text_aggr[field_name] = aggr_data
                        elif field_type == 'boolean':
                            boolean_aggr[field_name] = aggr_data
                    
                    updates.update({
                        'x_numeric_aggregations': json.dumps(numeric_aggr, ensure_ascii=False),
                        'x_text_aggregations': json.dumps(text_aggr, ensure_ascii=False),
                        'x_boolean_aggregations': json.dumps(boolean_aggr, ensure_ascii=False),
                        'x_last_sync_result': f"Успешно: {updates['x_total_count']} элементов"
                    })
                    
                    record.write(updates)
                    _logger.info(f"Data imported successfully for {record.x_name}")
                    
                else:
                    record.write({
                        'x_last_sync_result': f"Ошибка API: {response.status_code}"
                    })
                    _logger.error(f"API error for {record.x_name}: {response.status_code}")
                    
            except requests.exceptions.Timeout:
                record.write({
                    'x_last_sync_result': "Ошибка: таймаут подключения"
                })
                _logger.error(f"Timeout for {record.x_name}")
            except requests.exceptions.ConnectionError:
                record.write({
                    'x_last_sync_result': "Ошибка: нет подключения к сети"
                })
                _logger.error(f"Connection error for {record.x_name}")
            except Exception as e:
                record.write({
                    'x_last_sync_result': f"Ошибка: {str(e)}"
                })
                _logger.error(f"Error importing data for {record.x_name}: {str(e)}")
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Импорт данных',
                'message': f'Импорт завершен для {len(records)} записей',
                'type': 'success',
                'sticky': False,
            }
        }

    def action_import_data(self):
        """Действие для кнопки импорта"""
        return self.import_from_api()