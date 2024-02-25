# -*- coding: utf-8 -*-
{
    'name': "AB3 ACCOUNTING ACCOUNT",

    'summary': """
        Modul ini hanya untuk inherit yang berkaitan dengan product, ataupun pembuatan field baru""",

    'description': """
        in this module, they have:
        
        1. account move
        
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
        'account',
        'bi_sale_purchase_discount_with_tax',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_invoice.xml',

        'views/account_tax.xml',
        'views/account_move.xml',

    ],
}
