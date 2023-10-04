from odoo import api, models, fields

class WorkOrderCancelWizard(models.TransientModel):
    _name = 'work.order.cancel.wizard'
    _description = 'Work Order Cancel Wizard'
    
    notes = fields.Text(string="Notes")
    cancellation_reason = fields.Text(string="Cancellation Reason", required=True)

    def action_confirm_cancel(self):
        active_work_order_id = self.env.context.get('active_id')
        work_order = self.env['work.order'].browse(active_work_order_id)

        work_order.action_confirm_cancel(self.cancellation_reason)

        return {'type': 'ir.actions.act_window_close'}
