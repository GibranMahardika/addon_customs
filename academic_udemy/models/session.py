from odoo import api, fields, models, _

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)

    course_id = fields.Many2one(comodel_name='academic.course', string="Course")

    instructor_id = fields.Many2one(comodel_name='res.partner', string="Instructor")

    start_date = fields.Date("Start Date")
    
    duration = fields.Integer("Duration")
    
    seats = fields.Integer("Seats")

    active = fields.Boolean("Is active", default=True)

    attendee_ids = fields.One2many(comodel_name='academic.attendee', inverse_name='session_id', string='Attendees')

    taken_seats = fields.Float(string="Taken Seats", compute="_compute_taken_seats")

    def _compute_taken_seats(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.0 * len(x.attendee_ids) / x.seats
            else:
                x.taken_seats = 0.0

    @api.onchange('seats')
    def onchange_seats(self):
        if self.seats > 0:
                self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
        else:
            self.taken_seats = 0.0