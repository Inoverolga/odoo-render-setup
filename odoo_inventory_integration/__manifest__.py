{
    'name': 'Inventory Integration',
    'version': '1.0',
    'summary': 'Integration with external inventory system',
    'category': 'Inventory',
    'author': 'Your Name',
    'website': 'https://your-website.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}