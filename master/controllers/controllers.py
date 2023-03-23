# -*- coding: utf-8 -*-
# from odoo import http


# class Master(http.Controller):
#     @http.route('/master/master', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/master/master/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('master.listing', {
#             'root': '/master/master',
#             'objects': http.request.env['master.master'].search([]),
#         })

#     @http.route('/master/master/objects/<model("master.master"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('master.object', {
#             'object': obj
#         })
