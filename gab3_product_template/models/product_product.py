from odoo import fields, models, api

class productProductInherit(models.Model):
    _inherit = 'product.product'
    _description = 'Product Inherit'

    orderpoint_id = fields.Many2one(
        comodel_name="stock.warehouse.orderpoint", string="Orderpoint")
    
    product_min_qty = fields.Float(
        'Min Quantity', related='orderpoint_id.product_min_qty', store=True)