# -*- coding: utf-8 -*-
{
    'name': "Booking Order",

    'summary': """
        Gibran Mahardika_Odoo Test Hashmicro""",

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
    'depends': ['base','sale', 'mail', ],

    # always loaded
    'data': [
        'security/booking_order_group_role.xml',
        'security/ir.model.access.csv',

        'wizard/cancel_work_order_view.xml',
        
        'views/menu_action.xml',
        'views/menu_item.xml',

        'views/sale_order.xml',
        'views/service_team.xml',
        'views/work_order.xml',

        'data/data.xml',
        'report/work_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
