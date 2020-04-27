# -*- coding: utf-8 -*-

{
    'name': 'Ooredoo Contacts',
    'category': 'Tools',
    'summary': 'Centralize ooredoo address book',
    'depends': ['base', 'mail', 'purchase', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/ooredoo_price_list_views.xml',
        'views/product_template_views.xml',
        'views/orders_views.xml',
        'views/dealer_views.xml',
        'views/warehouse_views.xml',
        'views/salesperson_views.xml',
        'views/distributor_views.xml',
        'views/hierarchical_views.xml',
        'views/configurations_views.xml',
        'views/product_pricelist_views.xml',
        'views/menu_views.xml',
    ],
    'application': True,
}
