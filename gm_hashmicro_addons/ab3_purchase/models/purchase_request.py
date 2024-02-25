from odoo import fields, models, api


class purchaseRequestInherit(models.Model):
    _inherit = 'purchase.request'
    _description = 'Inherited class of purchase.request'



    # product_min_qty = fields.Float(
    #     'Min Quantity', related='line_ids.orderpoint_id.product_min_qty')
