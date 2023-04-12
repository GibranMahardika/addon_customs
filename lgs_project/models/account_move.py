from odoo import fields, models


class accountMoveInherit(models.Model):
    _inherit = 'account.move'

    origin_id = fields.Many2one(
        'lgs.area', string="Origin", tracking=True)

    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True)

    model_id = fields.Many2one(
        'fleet.vehicle.model', string="Vehicle Model", tracking=True)

    price = fields.Float(string="Price", tracking=True)
