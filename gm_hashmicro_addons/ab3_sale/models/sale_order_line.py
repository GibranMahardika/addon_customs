from odoo import fields, models, api, _


class saleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(saleOrderLineInherit, self).product_id_change()
        for order in self:
            if order.product_id:
                order.fixed_price = order.order_id.pricelist_id.item_ids.fixed_price
                order.min_price = order.order_id.pricelist_id.item_ids.minimum_price
        return res

    min_price = fields.Float('Min Price', readonly=True, store=True, tracking=True)
    fixed_price = fields.Float(string='Pricelist', readonly=True, store=True, tracking=True)

    # Other useless field
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', help='Pricelist when added')
    # Connector
    order_id = fields.Many2one('sale.order', string='Sale Order')
