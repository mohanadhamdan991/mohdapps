# -*- coding: utf-8 -*-
{
    'name': "User interface Python",
    'version': '16.0.2',
    'summary': 'Execute Python Codes',
    'sequence': -100,
    'description': """Execute Python Codes""",
    'category': 'Extra Tools',
    'author': "Mohannad Hamdan",
    'maintainer': 'Mohannad Hamdan',
    'price': '0.99',
    'currency': 'USD',
    'website': "https://www.hamdanerp.com",
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'views/ui_python.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
