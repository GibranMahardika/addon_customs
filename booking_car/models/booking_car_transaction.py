from datetime import datetime

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class transactionDailyRequest(models.Model):
    _name = "transaction.daily.request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'td_seq'

    @api.constrains('start_date', 'end_date', 'request_date')
    def _date_check(self):
        for x in self:
            if x.start_date <= x.request_date:
                raise ValidationError('EROR!!!, START DATE can not be lesser or equal than TODAY')
            if x.end_date <= x.start_date:
                raise ValidationError('EROR!!!, END DATE cannot be lesser or equal than START DATE')

    @api.model
    def create(self, vals):
        if vals.get('td_seq', _('New')) == _('New'):
            vals['td_seq'] = self.env['ir.sequence'].next_by_code('booking.car.transaction.sequence') or _('New')
            result = super(transactionDailyRequest, self).create(vals)
        return result

    @api.onchange('model_id')
    def _onchange_model_vehicle(self):
        self.seats = self.model_id.seats
        self.license_plate = self.model_id.license_plate

    # @api.model
    # def create(self,vals):
    #     if not vals.get['start_date']:
    #         vals['start_date'] = 'New start date'
    #     res = super(transactionDailyRequest, self).create(vals)
    #     return res
    #
    # def write(self, values):
    #     return super(transactionDailyRequest, self).write(values)
    #     print('this is values', values)

    # @api.onchange('model_id')
    # def _onchange_date_transaction(self):
    #     res = {}
    #     if self.model_id:
    #         res.update({
    #             'domain':
    #                 {
    #                     'start_date': [],
    #                     'end_date': [],
    #                     'model_id': [],
    #                     'vehicle_category_id': []
    #                 }
    #         })
    #         return res
    #     else:
    #         domain = []
    #         for r in self:
    #             if r.model_id.id:
    #                 domain.append(r.model_id.id)
    #             if r.start_date:
    #                 domain.append(r.start_date)
    #             if r.end_date:
    #                 domain.append(r.end_date)
    #             if r.vehicle_category_id:
    #                 domain.append(r.vehicle_category_id.id)
    #
    #         res.update({
    #             'domain':
    #                 {
    #                     'start_date': [('start_date', 'in', domain)],
    #                     'end_date': [('end_date', 'in', domain)],
    #                     'model_id': [('model_id', 'in', domain)],
    #                     'vehicle_category_id': [('vehicle_category_id', 'in', domain)]
    #                 }
    #         })
    # @api.onchange('model_id', 'start_date', 'end_date')
    # def _onchange_date_transaction(self):
    #     for x in self:
    #         if x.model_id.id:
    #             domain = ([
    #                 'start_date', '>=', x.start_date,
    #                 'end_date', '<=', x.end_date,
    #                 'model_id', '=', x.model_id.id,
    #                 'vehicle_category_id', '=', x.vehicle_category_id.id
    #             ])
    #         else:
    #             booked_car = self.search(domain)
    #             list = []
    #             for y in booked_car:
    #                 if y.model_id.id:
    #                     list.append(x.model_id.id)
    #             return {
    #                 'value': {'model_id': False},
    #                 'domain': {'model_id': [('model_id', 'not in', list)]}
    #             }

    @api.onchange('start_date', 'end_date', 'model_id')
    def _onchange_date_transaction(self):
        for x in self:
            if x.start_date and x.end_date and x.model_id.id:
                domain = ([
                    ('start_date', '>=', x.start_date),
                    ('end_date', '<=', x.end_date),
                    ('model_id', '=', x.model_id.id),
                    ('vehicle_category_id', '=', x.vehicle_category_id.id)
                ])
                domain_search = self.search(domain)
                for y in domain_search:
                    if y.model_id.id == x.model_id.id:
                        raise ValidationError('Kendaraan sudah di Booking')

    @api.onchange('start_date', 'end_date')
    def _hide_vehicle(self):
        for x in self:
            if x.start_date and x.end_date:
                x.model_id = False

    vehicle_model_con_id = fields.Many2one(comodel_name='fleet.vehicle.model')
    td_seq = fields.Char(string='Name Sequence', cFopy=False, readonly=True, index=True,
                         default=lambda self: _('New'))
    transaction_con_id = fields.Many2one('booking.car.request')
    request_con = fields.Many2one('booking.car.request', string='Request Connect')

    booking_status = fields.Selection(string='Booking Status',
                                      selection=[('1', 'Mobil'),
                                                 ('2', 'Driver'),
                                                 ('3', 'Mobil & Driver')],
                                      tracking=True, readonly=True)
    current_user = fields.Many2one('res.users', 'Request by', readonly=True)
    first_approval = fields.Many2one(comodel_name='res.users', string='First Approval', readonly=True)
    second_approval = fields.Many2one(comodel_name='res.users', string='Second Approval', readonly=True)
    num_of_passengers = fields.Integer(string='Num. Of Passengers', tracking=True, readonly=True)
    request_sequence = fields.Many2one(comodel_name='booking.car.request', string='Request ID', readonly=True)

    request_date = fields.Datetime(string="Request Date", readonly=True, default=datetime.today())
    start_date = fields.Datetime(string='Start Date', tracking=True)
    end_date = fields.Datetime(string='End Date', tracking=True)
    request_ids = fields.One2many('booking.car.request', 'transaction_id')

    # if MOBIL
    model_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle',
                               tracking=True, help='Model of the vehicle')
    vehicle_category_id = fields.Many2one(comodel_name='booking.car.vehicle.category', string='Vehicle Category',
                                          tracking=True, readonly=True)
    seats = fields.Integer('Seats Number', help='Number of seats of the vehicle', readonly=True)
    license_plate = fields.Char(string="License Plate", readonly=True)
    # if Driver
    driver_name_id = fields.Many2one(comodel_name='booking.car.driver', string='Driver Name', tracking=True)


class transactionCar(models.Model):
    _name = 'transaction.car'
    _rec_name = 'name_seq'

    @api.model
    def create(self, vals):
        if vals.get('td_seq', _('New')) == _('New'):
            vals['td_seq'] = self.env['ir.sequence'].next_by_code('booking.car.transaction.sequence') or _('New')
            result = super(transactionCar, self).create(vals)
        return result

    @api.onchange('vehicle_id')
    def _onchange_model(self):
        for x in self:
            if x.vehicle_id:
                move = self.env['fleet.vehicle'].search([('model_id', '=', x.vehicle_id.id)])
                if move:
                    for y in move:
                        x.seats = y.seats

        #         seats = x.seats - x.num_of_passengers
        # if seats < 0:
        #     raise ValidationError('Number of Seats is 0')

    name_seq = fields.Char(string='Name Sequence', cFopy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    transaction_con_id = fields.Many2one('booking.car.request')
    request_con = fields.Many2one('booking.car.request', string='Request Connect')

    booking_status = fields.Selection(string='Booking Status',
                                      selection=[('1', 'Mobil'),
                                                 ('2', 'Driver'),
                                                 ('3', 'Mobil & Driver')],
                                      tracking=True)
    current_user = fields.Many2one('res.users', 'Request by', readonly=True)
    first_approval = fields.Many2one(comodel_name='res.users', string='First Approval', readonly=True)
    second_approval = fields.Many2one(comodel_name='res.users', string='Second Approval', readonly=True)
    num_of_passengers = fields.Integer(string='Num. Of Passengers', tracking=True, readonly=True)

    # if MOBIL
    model_id = fields.Many2one('fleet.vehicle.model', 'Vehicle Model',
                               tracking=True, help='Model of the vehicle')
    vehicle_category_id = fields.Many2one(comodel_name='booking.car.vehicle.category', string='Vehicle Category',
                                          tracking=True, readonly=True)
    seats = fields.Integer('Seats Number', help='Number of seats of the vehicle')
