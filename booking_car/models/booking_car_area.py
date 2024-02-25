from odoo import fields, models


class BookingCarArea(models.Model):
    _name = 'booking.car.area'

    name = fields.Char()
    active = fields.Boolean(
        string='Is Active?',
        required=False, default=True)

    route_id = fields.Many2one(
        comodel_name='booking.car.route',
        string='Route',
        required=True)

    ring = fields.Selection(
        string='Ring',
        selection=[('1', 'Ring 1'),
                   ('2', 'Ring 2'),
                   ('3', 'Ring 3'),
                   ('4', 'Ring 4'),
                   ('5', 'Ring 5'),
                   ('6', 'Ring 6'),
                   ('7', 'Ring 7'),
                   ('8', 'Ring 8'),
                   ('9', 'Ring 9'),
                   ],
        required=False, )

