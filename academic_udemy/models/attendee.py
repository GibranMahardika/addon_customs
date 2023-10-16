from odoo import fields, models, api, _

class Attendee(models.Model):
    _name = "academic.attendee"
    _description = "Academic Attendee"

    name = fields.Char("Reg Number", required=True, size=100)

    session_id = fields.Many2one(comodel_name='academic.session', string="Session")
    attendee_id = fields.Many2one(comodel_name='res.partner', string="Attendence")
    is_instructor = fields.Boolean("Is Instructor")