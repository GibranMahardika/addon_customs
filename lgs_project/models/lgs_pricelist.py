from odoo import fields, models, _, api


class lgsPricelist(models.Model):
    _name = 'lgs.pricelist'
    _description = 'module custom Pricelist for LGS Company'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    so_name = fields.Char(string="SO Code", tracking=True,
                          default=lambda self: _('New'), states={'draft': [('readonly', False)]}, index=True, )

    name = fields.Char(string="", tracking=True, required=True)

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=_get_default_currency_id, tracking=True, required=True)
    customer_id = fields.Many2one(
        'res.partner', string="Customer", tracking=True, required=True)

    origin_id = fields.Many2one(
        'lgs.area', string="Origin", tracking=True, required=True)

    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True)

    model_id = fields.Many2one(
        'fleet.vehicle.model', string="Vehicle Model", tracking=True)

    price = fields.Float(string="Price", tracking=True)

    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('order', 'Sale Order'),
                                        ('reject', 'Reject')],
                             tracking=True, default='draft')

    type_pengiriman = fields.Selection([
        ('sd', 'Single Drop'),
        ('md', 'Multi Drop'),
    ], string="Tipe Pengiriman", tracking=True, required=True)

    sd_product_id = fields.Many2one(
        'product.template', string="Single Drop Product", tracking=True, domain="[('name', '=', 'Pengiriman Single Drop')]")
    md_product_id = fields.Many2one(
        'product.template', string="Multi Drop Product", tracking=True, domain="[('name', '=', 'Pengiriman Multi Drop')]")

    order_line_ids = fields.One2many(
        'product.template', 'lgs_pricelist_id', string="Product", tracking=True)

    # CONNECTOR
    # item_ids = fields.One2many('lgs.pricelist.item', 'pricelist_id')
    cdb_id = fields.Many2one('lgs.cdb', tracking=True)

    # button and notification

    @api.model
    def create(self, vals):
        if vals.get('so_name', _('New')) == _('New'):
            vals['so_name'] = self.env['ir.sequence'].next_by_code(
                'sale.order') or _('New')
            result = super(lgsPricelist, self).create(vals)
        return result

    def button_draft(self):

        self.write({'state': 'draft'})
        message = 'State on Draft'
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }

    def button_sale_order(self):
        for x in self:
            x.write({'state': 'order'})
            x._get_order()
            message = 'Data has been parsed on Sale Order'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

    def button_reject(self):
        self.write({
            'state': 'reject'
        })

    def _get_order(self):
        for x in self:
            env_move = self.env['sale.order'].create({
                'name': x.so_name,
                'partner_id': x.customer_id.id,
                'origin_id': x.origin_id.id,
                'destination_id': x.destination_id.id,
                'model_id': x.model_id.id,
                'price': x.price,
            })
