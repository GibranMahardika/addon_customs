# -*- coding: utf-8 -*-
{
    'name': "gm_sale_report",

    'summary': """
        Custom Addon for Sale Report, it's inherit""",

    'description': """
        1. Task = Menampilkan field branch_id yang berada di pivot
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",
    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto-install': False,

    # any module necessary for this one to work correctly
    'depends': ['mail','equip3_inventory_masterdata','sale'],

    # always loaded
    'data': [
        # 'views/sale_report.xml',
    ],
}
