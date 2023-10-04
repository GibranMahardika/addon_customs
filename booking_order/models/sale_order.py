from odoo import fields, models, api, _
from odoo.exceptions import UserError


class saleOrder(models.Model):
    _inherit = "sale.order"

    is_booking_order = fields.Boolean(string="Booking Order", default=True, required=True)
    service_team_id = fields.Many2one(comodel_name="service.team", string="Team", required=True)
    team_leader_id = fields.Many2one(comodel_name="res.users", string="Team Leader", required=True)
    team_members_ids = fields.Many2many(comodel_name="res.users", string="Team Member", required=True)
    booking_start = fields.Datetime(string="Start Booking", required=True)
    booking_end = fields.Datetime(string="Booking End", required=True)

    @api.onchange('service_team_id', 'team_leader_id', 'team_members_ids')
    def _onchange_service_team(self):
        for record in self:
            if record.service_team_id:
                team = record.service_team_id
                record.team_leader_id = team.team_leader_id.id
                record.team_members_ids = [(6, 0, team.team_members_ids.ids)]

    
    def action_check_work_order(self):
        for order in self:
            team = order.service_team_id
            team_leader = order.team_leader_id
            bo_start = order.booking_start
            bo_end = order.booking_end

            work_orders = self.env['work.order'].search([
                ('service_team_id', '=', team.id),
                ('team_leader_id', '=', team_leader.id),
                ('state','!=', 'cancelled'),
                ('start_plan', '<', bo_start),
                ('end_plan', '>', bo_end),
            ])

            if work_orders:
                message = "Team already has work order during that period on "
                message += ". ".join(work_orders.mapped('name'))
                order.message_post(body=message)

                # tampilan popup dengan pesan/message
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Team already has work order',
                        'sticky': False,
                        'message': message,
                    }
                }
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Team is available for booking',
                        'sticky': False,
                        'message': "Team is available for booking",
                    }
                }
            
    def action_confirm(self):
        for order in self:
            # 1. Cek availability team sesuai dengan point e
            team = order.service_team_id
            team_leader = order.team_leader_id
            bo_start = order.booking_start
            bo_end = order.booking_end

            work_orders = self.env['work.order'].search([
                ('service_team_id', '=', team.id),
                ('team_leader_id', '=', team_leader.id),
                ('state','!=', 'cancelled'),
                ('start_plan', '<', bo_start),
                ('end_plan', '>', bo_end),
            ])

            if work_orders:
                # Jika ada overlap, tampilkan pesan kesalahan
                message = "Team is not available during this period, already booked on "
                message += ", ".join(work_orders.mapped('name'))
                raise UserError(message)
            else:
                # 2. Auto create 1 work order record
                work_order = self.env['work.order'].create({
                    'booking_order_reference': order.id,
                    'service_team_id': team.id,
                    'team_leader_id': team_leader.id,
                    'team_members_ids': [(6, 0, order.team_members.ids)],
                    'start_plan': booking_start,
                    'end_plan': booking_end,
                    'state': 'pending',
                })

                # 3. Tampilkan Work Order yang dibuat di kanan atas Booking Order Form View
                order.write({'work_order_id': work_order.id})

                # 4. Panggil fungsi action_confirm asli
                super(saleOrder, order).action_confirm()