# -*- coding: utf-8 -*-
{
    'name': "Clear Cart",
    'version': '17.0.1.0.0',
    'depends': ['base','contacts','product', 'stock', 'sale','website_sale'],
    'category': '',
    'description': """
    summary of this app
    """,
    'data': [
        'views/website_sale_total.xml',
             ],
    'assets':{
        'web.assets_frontend': [
            'clear_cart/static/src/js/clear_cart.js',
        ],
    },
    # 'demo': [],
    'application': 'True',
    'installable': True,
}