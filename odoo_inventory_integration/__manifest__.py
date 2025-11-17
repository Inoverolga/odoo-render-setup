{
    'name': 'Inventory Integration',
    'version': '1.0',
    'summary': 'Storage for external inventory data',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}