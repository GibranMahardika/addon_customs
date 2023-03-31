from odoo import fields, models

class fleetVehicles(models.Model):
    _inherit = 'fleet.vehicle'
    
class fleetVehiclesModel(models.Model):
    _inherit = 'fleet.vehicle.model'
    
    total_wheel = fields.Integer(string="Wheel Number", tracking=True, required=True)
    total_weight = fields.Integer(string="Total Weight", tracking=True, required=True)
    weight_unit = fields.Selection([
        ('kg','KG'),
        ('ton','TON'),
        ], tracking=True, required=True)