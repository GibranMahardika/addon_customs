# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gm_agro__accounting_operation(models.Model):
#     _name = 'gm_agro__accounting_operation.gm_agro__accounting_operation'
#     _description = 'gm_agro__accounting_operation.gm_agro__accounting_operation'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
