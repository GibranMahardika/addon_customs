from odoo import fields, models, api


class purchaseRequestLineInherit(models.Model):
    _inherit = 'purchase.request.line'

    # @api.onchange('product_id')
    # def onchange_min_qty(self):
    #     if self.product_id:
    #         env = self.env['stock.warehouse.orderpoint'].search([('product_id', '=', self.product_id.id)])
    #         self.product_min_qty = min(env.mapped('product_min_qty'))
    #         self.product_qty = self.product_min_qty
            # self.product_min_qty = self.orderpoint_id.product_min_qty

    @api.onchange("product_id")
    def onchange_product_id(self):
        res = super(purchaseRequestLineInherit, self).onchange_product_id()
        if self.product_id:
            env = self.env['stock.warehouse.orderpoint'].search([('product_id', '=', self.product_id.id)])
            self.product_min_qty = min(env.mapped('product_min_qty'))
            self.product_qty = self.product_min_qty
        return res

    # @api.onchange("product_id")
    # def onchange_product_id(self):
    #     if self.product_id:
    #         env = self.env['stock.warehouse.orderpoint'].search([('product_id', '=', self.product_id.id)])
    #         self.product_min_qty = min(env.mapped('product_min_qty'))
    #         name = self.product_id.name
    #         if self.product_id.code:
    #             name = "[{}] {}".format(name, self.product_id.code)
    #         if self.product_id.description_purchase:
    #             name += "\n" + self.product_id.description_purchase
    #         self.product_uom_id = self.product_id.uom_id.id
    #         self.product_qty = self.product_min_qty
    #         self.name = name

    product_min_qty = fields.Float(string='Min Quantity')
