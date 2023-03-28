# -*- coding: utf-8 -*-
# from odoo import http


# class LgsProject(http.Controller):
#     @http.route('/lgs_project/lgs_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lgs_project/lgs_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lgs_project.listing', {
#             'root': '/lgs_project/lgs_project',
#             'objects': http.request.env['lgs_project.lgs_project'].search([]),
#         })

#     @http.route('/lgs_project/lgs_project/objects/<model("lgs_project.lgs_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lgs_project.object', {
#             'object': obj
#         })
