from odoo import api, fields, models


class requestWizard(models.TransientModel):
    _name = 'request.wizard'
    _description = 'Booking Car Request Wizard'

    def _default_request(self):
        return self.env['booking.car.request'].browse(self._context.get('active_ids'))

    request_id = fields.Many2one('booking.car.request', string="Request M2O", default=_default_request)
    request_ids = fields.Many2many('booking.car.request', string='Request M2M')

    def tambah_request(self):
        self.request_id.request_ids |= self.request_ids