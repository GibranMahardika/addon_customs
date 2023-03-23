# -*- coding: utf-8 -*-
# from odoo import http


# class Showroom(http.Controller):
#     @http.route('/showroom/showroom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/showroom/showroom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('showroom.listing', {
#             'root': '/showroom/showroom',
#             'objects': http.request.env['showroom.showroom'].search([]),
#         })

#     @http.route('/showroom/showroom/objects/<model("showroom.showroom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('showroom.object', {
#             'object': obj
#         })
