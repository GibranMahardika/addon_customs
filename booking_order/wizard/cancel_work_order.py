from odoo import fields, models, api

class cancelWorkOrderWizard(models.TransientModel):
    _name = "cancel.work.order.wizard"
    _description = "Cancel Work Order button with Wizzard"

    cancellation_reason = fields.Text(string="Notes")

    def action_cancel(self):
        context = self.env.context
        work_order_id = context.get('active_id')
        work_order = self.env['work.order'].browse(work_order_id)

        # Update the state to cancelled
        work_order.write({'state': 'cancel'})

        # Append the cancellation reason to the notes field
        work_order.notes = self.cancellation_reason

        return {'type': 'ir.actions.act_window_close'}