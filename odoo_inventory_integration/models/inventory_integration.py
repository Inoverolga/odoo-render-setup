from odoo import models, fields

class InventoryIntegration(models.Model):
    _inherit = 'x_inventory_data'
    
    # Только наследуем модель, методы импорта будут в JSON-RPC скрипте