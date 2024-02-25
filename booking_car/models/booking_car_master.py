from odoo import fields, models,api

class bookingCarInheritFleetVehicleBrand(models.Model):
    _inherit = ['fleet.vehicle.model.brand']

    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

class bookingCarVehicleCategory(models.Model):
    _name = 'booking.car.vehicle.category'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

class bookingCarInheritFleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'

    vehicle_type = fields.Selection(
        string='Vehicle Type',
        selection=[('', ''),
                   ('', ''), ],
        required=False, )

    vehicle_category = fields.Many2one(
        comodel_name='booking.car.vehicle.category',
        string='Vehicle Category',
        required=False)

class bookingCarVehicleName(models.Model):
    _name = 'booking.car.vehicle.name'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

class bookingCarVehicleType(models.Model):
    _name = 'booking.car.vehicle.type'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

class BookingCarInheritResCompany(models.Model):
    _inherit = 'res.company'
