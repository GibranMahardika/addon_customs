# -*- coding: utf-8 -*-
# from odoo import http


# class GmAgroAccountingOperation(http.Controller):
#     @http.route('/gm_agro__accounting_operation/gm_agro__accounting_operation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gm_agro__accounting_operation/gm_agro__accounting_operation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gm_agro__accounting_operation.listing', {
#             'root': '/gm_agro__accounting_operation/gm_agro__accounting_operation',
#             'objects': http.request.env['gm_agro__accounting_operation.gm_agro__accounting_operation'].search([]),
#         })

#     @http.route('/gm_agro__accounting_operation/gm_agro__accounting_operation/objects/<model("gm_agro__accounting_operation.gm_agro__accounting_operation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gm_agro__accounting_operation.object', {
#             'object': obj
#         })
