from odoo import fields, models, api, _
import datetime

class workOrder(models.Model):
    _name = 'work.order'
    _description = 'booking_order.work.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="WO Number", required=True, default=lambda self: _('New'))
    bo_ref_id = fields.Many2one(comodel_name='sale.order', string="Booking Order Reference")
    service_team_id = fields.Many2one(comodel_name="service.team", string="Team", required=True)
    team_leader_id = fields.Many2one(comodel_name="res.users", string="Team Leader", required=True)
    team_members_ids = fields.Many2many(comodel_name="res.users", string="Team Member", required=True)
    start_plan = fields.Datetime(string="Planned Start", required=True)
    end_plan = fields.Datetime(string="Planned End", required=True)
    date_start = fields.Datetime(string="Date Start")
    date_end = fields.Datetime(string="Date End")
    state = fields.Selection([
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel')],
        default='pending', copy=False, tracking=True)
    notes = fields.Text(string="Notes")
    customer_id = fields.Many2one(comodel_name="res.partner")

    @api.model
    def create(self, vals):
        vals['state'] = 'draft'
        return super(workOrder, self).create(vals)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'work.order.sequence') or _('New')
            result = super(workOrder, self).create(vals)
        return result
    
    @api.onchange('service_team_id', 'team_leader_id', 'team_members_ids')
    def _onchange_service_team(self):
        for record in self:
            if record.service_team_id:
                team = record.service_team_id
                record.team_leader_id = team.team_leader_id.id
                record.team_members_ids = [(6, 0, team.team_members_ids.ids)]
    
    def action_start_work(self):
        self.write({'state': 'progress', 'date_start': fields.Datetime.now()}) 

    def action_end_work(self):
        self.write({'state': 'done', 'date_end': fields.Datetime.now()})

    def action_reset_work(self):
        self.write({'state': 'pending', 'date_start': False, 'date_end': False})

    def action_cancel_work(self):
       self.write({'state': 'cancel'})
       action = self.env.ref('booking_order.cancel_work_order_wizard_action').read()[0]
       return action