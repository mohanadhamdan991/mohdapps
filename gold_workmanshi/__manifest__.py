# -*- coding: utf-8 -*-
{
    'name': "Gold Workmanship",
    'version': '13.0.1',
    'summary': 'This module is used to calculate the gold workmanship per unit',
    'sequence': -100,
    'description': """This module is used to calculate the gold workmanship per unit""",
    'category': 'Accounting',
    'author': "HamdanERP",
    'maintainer': 'HamdanERP',
    'price': '2.99',
    'currency': 'USD',
    'website': 'https://www.hamdanerp.com',
    'license': 'AGPL-3',
    'depends': ['sale', 'sale_management', 'account', 'purchase'],
    'data': [
        'views/account_move.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'report/sale_report_inherit.xml',
        'report/purchase_report_inherit.xml',
        'report/account_report_inherit.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner4.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
