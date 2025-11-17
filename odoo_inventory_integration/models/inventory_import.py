from odoo import models, api
import requests
import json
from datetime import datetime
from odoo.exceptions import UserError

class XInventoryData(models.Model):
    _inherit = 'x_inventory.data'

    def action_import_from_api(self):
        if not self.x_api_token:
            raise UserError("Введите API токен")
        
        try:
    
            api_url = f"https://mainproject-back.onrender.com/api/odoo/{self.x_api_token}/aggregateddata"
            response = requests.get(api_url, timeout=30)
            response.raise_for_status()
            data = response.json()
          
            self.write({
                'x_name': data['inventory']['name'],
                'x_external_id': data['inventory']['id'],
                'x_total_count': data['aggregations']['total_count'],
                'x_last_sync': datetime.now(),
                'x_last_sync_result': f"Успешно: {data['aggregations']['total_count']} элементов"
            })
            
        except Exception as e:
            raise UserError(f"Ошибка импорта: {str(e)}")