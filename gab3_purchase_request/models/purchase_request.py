from odoo import fields, models, api


class purchaseRequestInherit(models.Model):
    _inherit = 'purchase.request'
    _description = 'Inherited class of purchase.request'

    @api.onchange('product_id')
    def onchange_min_qty(self):
        if self.product_id:
            self.product_min_qty = self.orderpoint_id.product_min_qty

    product_min_qty = fields.Float(
        'Min Quantity', related='line_ids.orderpoint_id.product_min_qty', store=True)
