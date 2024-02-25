from odoo import fields, models, api


class BookingCarDepartment(models.Model):
    _name = 'booking.car.department'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

class BookingCarInheritResUsers(models.Model):
    _inherit = 'res.users'

    department_id = fields.Many2one(
        comodel_name='booking.car.department',
        string='Department',
        required=False)

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=False)