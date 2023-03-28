# -*- coding: utf-8 -*-
{
    'name': "master",

    'summary': """
        All master data collect and gather in this module""",

    'description': """
        All master data collect and gather in this module, there are:
        1. localization
        2. cdb
        3. etc.
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",

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
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
