# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gm_book_list(models.Model):
#     _name = 'gm_book_list.gm_book_list'
#     _description = 'gm_book_list.gm_book_list'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
