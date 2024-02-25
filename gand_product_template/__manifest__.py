# -*- coding: utf-8 -*-
{
    'name': "gand_product_template",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        inventory -> Product
        1. is ROLL? -> diganti -> is a Haspel
        2. lot number auto generated by system -> diganti jadi FALSE
        3. General Information -> dibawah product category membuat master data product.clasification (name & description) type data Many2one
        4. General Information -> dibawah product category product.detail type data Many2one
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",
    'category': 'Product',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto-install': False,

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'equip3_inventory_operation',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/menu_action.xml',
        'views/menu_items.xml',

        'views/product_classification.xml',
        'views/product_detail.xml',
    ],
}
