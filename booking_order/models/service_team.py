from odoo import fields, models, api, _

class serviceTeam(models.Model):
    _name = "service.team"
    _description = "booking_order.service.team"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True, default=lambda self: _('New'))
    team_leader_id = fields.Many2one(comodel_name='res.users', required=True, string="Team Leader")
    team_members_ids = fields.Many2many(comodel_name='res.users', string="Team Member")
    
    sale_order_id = fields.One2many(comodel_name='sale.order', inverse_name='service_team_id')