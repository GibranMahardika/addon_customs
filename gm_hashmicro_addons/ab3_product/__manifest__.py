# -*- coding: utf-8 -*-
{
    'name': "AB3 Product",

    'summary': """
        Modul ini hanya untuk inherit yang berkaitan dengan product, ataupun pembuatan field baru""",

    'description': """
        in this module, they have:
        
        1. product classification
        2. product detail
        3. product product
        4. product template
        
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
        'equip3_inventory_operation',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/menu_action.xml',
        'views/menu_items.xml',

        'views/product_classification.xml',
        'views/product_detail.xml',
        'views/product_template.xml',
        'views/product_supplier_info.xml',
    ],
}
