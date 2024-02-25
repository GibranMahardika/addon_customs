from odoo import fields, models, api


class purchaseRequestLineInherit(models.Model):
    _inherit = 'purchase.request.line'

    product_min_qty = fields.Float(string='Min Quantity')