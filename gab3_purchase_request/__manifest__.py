# -*- coding: utf-8 -*-
{
    'name': "Purchase Request inherited module",

    'summary': """
        Purchase Request inherited module""",

    'description': """
        1. Terdapat tambahan field "Minimal Stock" pada Purchase Request". Relate to Minimal Stock pada Reorderring Rules.
        2. Pada PR →  Hide Estimate Cost, Purchase Budget.
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
        'views/purchase_request.xml',
    ],
}
