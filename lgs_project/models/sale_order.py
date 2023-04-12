from odoo import fields, models, api, _


class saleOrderInherit(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        res = super(saleOrderInherit, self)._prepare_invoice()
        res.update({
            "origin_id": self.origin_id,
            "destination_id": self.destination_id,
            "model_id": self.model_id,
        })
        return res

    @api.onchange('origin_id', 'destination_id', 'model_id', 'price')
    def _onchange_origin(self):
        for x in self:
            if x.origin_id:
                env = self.env['lgs.pricelist'].search([
                    ('origin_id', '=', x.origin_id.id),
                    ('destination_id', '=', x.destination_id.id),
                    ('model_id', '=', x.model_id.id),
                    ('customer_id', '=', x.partner_id.id),
                ])
                if env:
                    for y in env:
                        x.price = y.price

    origin_id = fields.Many2one(
        'lgs.area', string="Origin", tracking=True)

    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True)

    model_id = fields.Many2one(
        'fleet.vehicle.model', string="Vehicle Model", tracking=True)

    price = fields.Float(string="Price", tracking=True)


class saleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        super(saleOrderLineInherit, self).product_uom_change()

        # if self.product_id:
        #     move = self.env['sale.order'].search(
        #         [('price', '=', self.price_unit)])
        #     if move:
        #         move.price = self.price_unit
        
        # for x in self:
        #     if x.product_id:
        #         move = self.env['lgs.pricelist'].search(
        #             [('price', '=', x.price_unit)])
        #         if move:
        #             for y in move:
        #                 y. price = x.price_unit

        if self.product_id:
            self.price_unit = self.order_id.price

    lgs_pricelist_id = fields.Many2one('lgs.pricelist')
