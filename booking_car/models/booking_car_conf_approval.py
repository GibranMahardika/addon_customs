from odoo import fields, models, api


class BookingCarConfApproval(models.Model):
    _name = 'booking.car.conf.approval'
    _description = 'Description'

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=False)

    department_id = fields.Many2one(
        comodel_name='booking.car.department',
        string='Department',
        required=False)

    first_approval = fields.Many2one(
        comodel_name='res.users',
        string='First Approval',
        required=False)


    second_approval = fields.Many2one(
        comodel_name='res.users',
        string='Second Approval',
        required=False)