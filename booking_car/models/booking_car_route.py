from odoo import fields,models,api

class BookingCarRoute(models.Model):
    _name = 'booking.car.route'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)