from odoo import fields, models, api


class bookingCarVehicle(models.Model):
    _name = 'booking.car.vehicle'

    @api.onchange('vehicle_model_id')
    def _onchange_model(self):
        for x in self:
            if x.vehicle_model_id:
                move = self.env['fleet.vehicle'].search([('model_id', '=', x.vehicle_model_id.id)])
                if move:
                    for y in move:
                        x.seats = y.seats
                        x.license_plate = y.license_plate
                        x.fuel_type = y.fuel_type
                        x.transmission = y.transmission
                        x.x_model = y.x_model

    # @api.depends('seats', 'num_of_passengers')
    # def _compute_seats(self):
    #     for x in self:
    #         # if h.amount_to_pay >= h.plafon_id:
    #         seat = x.seats - x.num_of_passengers
    #         if seat <= 0:
    #             raise ValidationError("Number of Seats is 0")

    x_model = fields.Char('Model Group')
    license_plate = fields.Integer(string='License Plate')
    status = fields.Selection(selection=[('booked', 'Booked'),
                                         ('free', 'Free')], required=False, default='free', tracking=True)
    seats = fields.Integer('Seats Number', help='Number of seats of the vehicle')
    vehicle_model_id = fields.Many2one('fleet.vehicle.model', 'Vehicle Model',
                                       tracking=True, required=True, help='Model of the vehicle')
    fuel_type = fields.Selection([
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('lpg', 'LPG'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid')
    ], 'Fuel Type', help='Fuel Used by the vehicle')
    transmission = fields.Selection([('manual', 'Manual'),
                                     ('automatic', 'Automatic')], 'Transmission',
                                    help='Transmission Used by the vehicle')
