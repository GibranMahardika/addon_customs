from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime


class BookingCarRequest(models.Model):
    _name = 'booking.car.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "name_seq"

    @api.depends('passenger_ids', 'num_of_passengers')
    def _passenger_num(self):
        for x in self:
            x.num_of_passengers = len(x.passenger_ids)

    @api.onchange('current_department', 'company_id', 'first_approval', 'second_approval')
    def _onchange_approval(self):
        for x in self:
            if x.current_department:
                move = self.env['booking.car.conf.approval'].search(
                    [('department_id', '=', x.current_department.id), ('company_id', '=', x.current_company.id)])
                if move:
                    for y in move:
                        x.first_approval = y.first_approval.id
                        x.second_approval = y.second_approval.id

    @api.constrains('start_date', 'end_date', 'request_date')
    def _date_check(self):
        for x in self:
            if x.start_date <= x.request_date:
                raise ValidationError('EROR!!!, START DATE can not be lesser or equal than TODAY')
            if x.end_date <= x.start_date:
                raise ValidationError('EROR!!!, END DATE cannot be lesser or equal than START DATE')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('booking.car.request.sequence') or _('New')
            result = super(BookingCarRequest, self).create(vals)
        return result

    name_seq = fields.Char(string='Name Sequence', copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    request_date = fields.Datetime(string="Request Date", readonly=True, default=datetime.today())
    start_date = fields.Datetime(string='Start Date', tracking=True)
    end_date = fields.Datetime(string='End Date', tracking=True)
    booking_status = fields.Selection(string='Booking Status',
                                      selection=[('1', 'Mobil'),
                                                 ('2', 'Driver'),
                                                 ('3', 'Mobil & Driver')],
                                      tracking=True)
    booking_type = fields.Selection(string='Booking Type',
                                    selection=[('1', 'Keperluan kantor'), ('2', 'Keperluan pribadi'),
                                               ('3', 'Keperluan lembur')],
                                    tracking=True)
    destination = fields.Text(string="Destination", tracking=True)
    purpose_remark = fields.Text(string="Purpose Remark", tracking=True)
    passenger_ids = fields.Many2many(comodel_name='res.partner', string='Passenger', tracking=True)
    num_of_passengers = fields.Integer(string='Num. Of Passengers', store=True,
                                       compute='_passenger_num', tracking=True)
    area_id = fields.Many2one(comodel_name='booking.car.area', string='Area', tracking=True)
    vehicle_category_id = fields.Many2one(comodel_name='booking.car.vehicle.category', string='Vehicle Category',
                                          tracking=True)
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('approve1', 'Approve 1'),
                                        ('approve2', 'Approve 2'),
                                        ('approved', 'Approved'),
                                        ('reject', 'Reject')],
                             default='draft', tracking=True)
    first_approval = fields.Many2one(comodel_name='res.users', string='First Approval', readonly=True)
    second_approval = fields.Many2one(comodel_name='res.users', string='Second Approval', readonly=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company')
    _defaults = {'current_uid': lambda self, cr, uid, ctx=None: uid}
    current_user = fields.Many2one(comodel_name='res.users', string='Request by', default=lambda self: self.env.user, readonly=True)
    current_company = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id,
                                      readonly=True)
    current_department = fields.Many2one('booking.car.department', 'Department',
                                         default=lambda self: self.env.user.department_id.id,
                                         readonly=True)
    transaction_id = fields.Many2one('transaction.daily.request', string='Record Transaction')
    def button_reject(self):
        self.write({'state': 'reject'})

    def button_reject2(self):
        self.write({'state': 'reject'})

    def button_approve_1(self):
        self.write({'state': 'approve2'})

    def button_approve_2(self):
        self.write({'state': 'approved'})
        self._get_approval_type()

    def button_draft(self):
        self.write({'state': 'draft'})

    # def button_approve(self):
    #     self._get_approval_type()

    def _get_approval_type(self):
        for x in self:
            env_move = self.env['transaction.daily.request'].create({
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