from odoo import fields, models


class fleetVehicles(models.Model):
    _inherit = 'fleet.vehicle'
    cdb_id = fields.Many2one('lgs.cdb', string="CDB", tracking=True)

class fleetVehiclesModel(models.Model):
    _inherit = 'fleet.vehicle.model'

    total_wheel = fields.Integer(string="Wheel Number", tracking=True)
    total_weight = fields.Integer(string="Total Weight", tracking=True)
    weight_unit = fields.Selection([
        ('kg', 'KG'),
        ('ton', 'TON'),
    ], tracking=True)
    company_id = fields.Many2one(
        'res.company', string="Company", tracking=True)

    # tab pricelist
    area_id = fields.Many2one('lgs.area', string="Area", tracking=True)
    cdb_id = fields.Many2one('lgs.cdb', string="CDB", tracking=True)
