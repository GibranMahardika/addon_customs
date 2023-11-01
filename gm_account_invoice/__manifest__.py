# -*- coding: utf-8 -*-
{
    'name': "gm_account_invoice",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",
    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto-install': False,

    'depends': ['account'],

    # always loaded
    'data': [
        'views/account_move.xml',
    ],
    # only loaded in demonstration mode
}
