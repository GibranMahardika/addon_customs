from odoo import fields,models

class inheritFleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    vehicle_category_id = fields.Many2one(comodel_name='booking.car.vehicle.category', string='Vehicle Category',
                                          tracking=True)