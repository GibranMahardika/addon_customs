from odoo import fields, models, api, _


class bookingCarDriver(models.Model):
    _name = 'booking.car.driver'

    @api.model
    def create(self, vals):
        if vals.get('driver_seq', _('New')) == _('New'):
            vals['driver_seq'] = self.env['ir.sequence'].next_by_code('booking.car.driver.sequence') or _('New')
            result = super(bookingCarDriver, self).create(vals)
        return result

    driver_seq = fields.Char(string='Name Sequence', copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    name = fields.Many2one('res.partner', string='Name')
    age = fields.Integer('Age')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                              required=False, default='male', tracking=True)
    email_address = fields.Char(string='Email Address', required=False)
    phone = fields.Integer(string='Mobile', required=False)
    phone1 = fields.Integer(string='Home')
    sim = fields.Selection(selection=[('a', 'A'),
                                      ('b1', 'B1'),
                                      ('b2', 'B2'),
                                      ('c', 'C'),
                                      ('d', 'D')],
                              required=False, default='male', tracking=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', required=False, tracking=True)
    other_info = fields.Text(string='Other Info')
    active = fields.Boolean(string='Is Active?', required=False, default=True)


class bookingCarDriverLine(models.Model):
    _name = 'booking.car.driver.cek.status'
    _description = 'Booking car driver cek status'

    # @api.onchange('booking_status')
    # def _onchange_booking_status(self):
    #     for x in self:
    #         if x.booking_status:
    #             move = self.env['booking.car.request'].search([('booking_status', '=', x.booking_status)])
    #             if move:
    #                 for y in move:
    #                     x.booking_status = y.booking_status

    name = fields.Many2one('res.partner', string='Name')
    status_aktif = fields.Selection(selection=[('1', 'Ongoing'),
                                               ('2', 'Idle')], required=False, default='2', tracking=True)
    active = fields.Boolean(string="Active")
