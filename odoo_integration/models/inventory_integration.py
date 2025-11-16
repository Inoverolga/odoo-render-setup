from odoo import models, fields, api

class InventoryIntegration(models.Model):
    _name = 'x_inventory.data'
    _description = 'Inventory Integration Data'

    x_name = fields.Char(string='Название инвентаризации')
    x_api_token = fields.Char(string='API Token')
    x_external_id = fields.Char(string='Внешний ID инвентаризации')
    x_total_count = fields.Integer(string='Общее количество')
    x_last_sync = fields.Date(string='Дата последней синхронизации')