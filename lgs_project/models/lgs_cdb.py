from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError


class lgsCDB(models.Model):
    _name = 'lgs.cdb'
    _description = "module for customer database of LGS"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    name = fields.Char(string="Nama Lembaga", copy=False,
                       default=lambda self: _('New'))

    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True, required=True)

    origin_id = fields.Many2one(
        'lgs.area', string="Origin", tracking=True, required=True)

    customer_id = fields.Many2one(
        'res.partner', string="Customer", tracking=True, required=True)

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=_get_default_currency_id, tracking=True, required=True)

    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('order', 'Sale Order'),
                                        ('reject', 'Reject')],
                             tracking=True, default='draft')

    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True)

    model_id = fields.Many2one(
        'fleet.vehicle.model', string="Vehicle Model", tracking=True)

    price = fields.Float(string="Price", tracking=True)

    # connector
    pricelist_ids = fields.One2many('lgs.pricelist', 'cdb_id', tracking=True)

    model_ids = fields.One2many('fleet.vehicle', 'cdb_id')

    def button_draft(self):
        message = 'State on Draft'
        self.write({'state': 'draft'})
        return {
            'type': 'ir.action.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }

    def button_sale_order(self):
        message = 'Data has been parsed on Sale Order'
        self.write({'state': 'order'})
        self._get_order()
        return {
            'type': 'ir.action.client',
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
                'first_approval': x.first_approval.id,
                'second_approval': x.second_approval.id,
                'current_user': x.current_user.id,
                'booking_status': x.booking_status,
                'num_of_passengers': x.num_of_passengers,
                'vehicle_category_id': x.vehicle_category_id.id,
                'request_sequence': x.id,
                'start_date': x.start_date,
                'end_date': x.end_date,
            })
            return {
                'warning': {
                    'title': 'PERINGATAN!',
                    'message': 'Apakah Data sudah benar?'}
            }
    # brand_id = fields.Many2one(
    #     'fleet.vehicle.model', string="Vehicle Model", tracking=True)
    # seats = fields.Integer(string="Seats Number",
    #                        tracking=True, related='brand_id.seats', store=True)

    # doors = fields.Integer(string="Seats Number",
    #                        tracking=True, related='brand_id.doors', store=True)

    # total_wheel = fields.Integer(string="Wheel Number", tracking=True,
    #                              related='brand_id.total_wheel', store=True)

    # total_weight = fields.Integer(string="Total Weight", tracking=True,
    #                               related='brand_id.total_weight', store=True)

    # weight_unit = fields.Selection([
    #     ('kg', 'KG'),
    #     ('ton', 'TON'),
    # ], tracking=True, related='brand_id.weight_unit', store=True)

    # cdb_state = fields.Selection([
    #     ('draft','Draft'),
    #     ('order','Order'),
    #     ])
    # origin

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'lgs.cdb.sequence') or _('New')
            result = super(lgsCDB, self).create(vals)
        return result
