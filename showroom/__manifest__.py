# -*- coding: utf-8 -*-
{
    'name': "showroom",

    'summary': """
        Module custom for Showroom
    """,

    'description': """
        Module Custom for Showroom
    """,

    'author': "Gibran Mahardika",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto-install': False,
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','master'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
