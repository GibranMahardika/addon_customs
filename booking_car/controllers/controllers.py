# -*- coding: utf-8 -*-
# from odoo import http


# class BookingCar(http.Controller):
#     @http.route('/booking_car/booking_car/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_car/booking_car/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_car.listing', {
#             'root': '/booking_car/booking_car',
#             'objects': http.request.env['booking_car.booking_car'].search([]),
#         })

#     @http.route('/booking_car/booking_car/objects/<model("booking_car.booking_car"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_car.object', {
#             'object': obj
#         })
