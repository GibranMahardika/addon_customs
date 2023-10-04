# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule/academicUdemy(http.Controller):
#     @http.route('/my_module/academic_udemy/my_module/academic_udemy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module/academic_udemy/my_module/academic_udemy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module/academic_udemy.listing', {
#             'root': '/my_module/academic_udemy/my_module/academic_udemy',
#             'objects': http.request.env['my_module/academic_udemy.my_module/academic_udemy'].search([]),
#         })

#     @http.route('/my_module/academic_udemy/my_module/academic_udemy/objects/<model("my_module/academic_udemy.my_module/academic_udemy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module/academic_udemy.object', {
#             'object': obj
#         })
