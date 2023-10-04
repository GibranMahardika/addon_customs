# -*- coding: utf-8 -*-
# from odoo import http


# class GmBookList(http.Controller):
#     @http.route('/gm_book_list/gm_book_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gm_book_list/gm_book_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gm_book_list.listing', {
#             'root': '/gm_book_list/gm_book_list',
#             'objects': http.request.env['gm_book_list.gm_book_list'].search([]),
#         })

#     @http.route('/gm_book_list/gm_book_list/objects/<model("gm_book_list.gm_book_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gm_book_list.object', {
#             'object': obj
#         })
