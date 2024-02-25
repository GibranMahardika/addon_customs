# -*- coding: utf-8 -*-
{
    'name': "AB3 PURCHASE",

    'summary': """
        Purchase Request inherited module""",

    'description': """
        in this module, they have:
        1. purchase request
        2. purchase request line
        
        please if you (dev or sup) using this module, update the description, 
        and use COMMENT in every sintax your made
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",
    'category': 'Product',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto-install': False,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'purchase_request',
        'equip3_inventory_control',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'report/report_purchase_template.xml',
        
        'views/purchase_request.xml',
        'views/res_users_views.xml',
        
    ],
}
