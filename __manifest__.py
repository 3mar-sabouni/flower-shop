# -*- coding: utf-8 -*-
{
    'name': "flower shop",

    'summary': "",

    'description': """
    """,

    'author': "Omar Sabouni",
    'website': "",
    'category': 'Uncategorized',
    'version': '17.0.0.2',
    'depends': ['base','sale','website_sale','stock'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/flower_water_views.xml',
        'views/flower_flower_views.xml',
        'views/product_product_views.xml',
        'views/template_product_inhert.xml',
        'views/stock_production_lot_inhert.xml',
        'views/warehouse_weather_views.xml',
        'views/stock_warehouse_views.xml',
        'reports/flower_sale_order_views.xml',
        'data/ir_cron.xml',
        'data/ir_actions_server.xml',
        'data/ir_config_parameter_data.xml'
        ],
    'demo': [
    ],
}

