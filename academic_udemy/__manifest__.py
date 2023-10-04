# -*- coding: utf-8 -*-
{
    'name': "Academic Udemy",

    'summary': """
        note:
        1. gunakan command ini, pada saat upgrade base res.partner : python odoo-bin -c odoo.conf -d db_14_test -u academic_udemy""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto-install': False,
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/menu_action.xml',
        'views/menu_item.xml',
        
        'views/course_views.xml',
        'views/session_views.xml',
        'views/attendee_views.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
