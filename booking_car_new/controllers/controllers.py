# -*- coding: utf-8 -*-
# from odoo import http


# class BookingCarNew(http.Controller):
#     @http.route('/booking_car_new/booking_car_new/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_car_new/booking_car_new/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_car_new.listing', {
#             'root': '/booking_car_new/booking_car_new',
#             'objects': http.request.env['booking_car_new.booking_car_new'].search([]),
#         })

#     @http.route('/booking_car_new/booking_car_new/objects/<model("booking_car_new.booking_car_new"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_car_new.object', {
#             'object': obj
#         })
