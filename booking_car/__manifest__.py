# -*- coding: utf-8 -*-
{
    'name': "Booking Car",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        1. Tambahan state dan button pada booking_car_request_view.xml
        2. Mengatur sintaks dan membuat file berdasarkan model
        3. Membuat Record Rule, Group, Access Rule
        4. Merubah state dan menambahkan fitur readonly pada tiap field dengan state approve
        5. 
    """,

    'author': "Panca Budi Niaga",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'sequence': 1,
    'category': 'Fleet (Booking Car)',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'mail'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/booking_car_groups.xml',
        'security/booking_car_security.xml',
        'security/ir.model.access.csv',
        'views/booking_car_request_view.xml',
        'views/booking_car_area.xml',
        'views/booking_car_conf_approval.xml',
        'views/booking_car_departement.xml',
        'views/booking_car_driver.xml',
        'views/booking_car_vehicle.xml',
        'views/booking_car_inherit.xml',
        'views/booking_car_route.xml',
        'views/booking_car_vehicle_category.xml',
        'views/booking_car_vendor.xml',
        'views/booking_car_transaction.xml',
        'wizard/wizard_request.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
