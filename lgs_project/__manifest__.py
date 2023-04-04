# -*- coding: utf-8 -*-
{
    'name': "lgs_project",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
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
    'depends': ['base', 'mail', 'fleet', 'hr'],

    # always loaded
    'data': [
        'security/lgs_group_role.xml',
        'security/ir.model.access.csv',

        
        'views/menu_action.xml',
        'views/menu_item.xml',

        
        'views/fleet_vehicles.xml',
        'views/lgs_area.xml',
        'views/origin_type.xml',
        
        'views/lgs_pricelist.xml',
        'views/lgs_pricelist_item.xml',
        'views/lgs_pricelist_master.xml',
        # 'views/product_pricelist.xml',
        
        'views/lgs_cdb.xml',
        
        'data/data.xml'
        
        
        # 'views/lgs_cdb.xml',
    ],  
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
