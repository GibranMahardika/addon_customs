from odoo import fields, models, api, _


class lifetimeRerportWizard(models.TransientModel):
    _name = 'lifetime.report.wizard'
    _description = "Lifetime Report Wizard"

    name = fields.Char('Name')
    product_id = fields.Many2one('product.product', 'Nama Material')
    lot_id = fields.Many2one('stock.production.lot', 'Serial Number')
    default_code = fields.Char('Part Number')
    parent_equipment_id = fields.Many2one('maintenance.equipment', 'Unit Terpasang')
    add_date = fields.Date('Tanggal Pemasangan')
    remove_date = fields.Date('Tanggal Penggantian')
    lifetime = fields.Integer('Lifetime (Days)')
    actual_lifetime = fields.Integer('Actual Lifetime (Days)')
    state = fields.Selection([('failed', 'Failed'), ('goal', 'Goal')], 'Status')
    maintenance_ro_id = fields.Many2one('maintenance.repair.order', 'Maintenance Repair Order')
    notes = fields.Char('Notes')

    def action_create_lifetime_report(self):
        # Your logic here
        # For example, print the wizard's name
        print(f"Confirmed wizard with name: {self.name}")

        # Close the wizard (optional)
        return {'type': 'ir.actions.act_window_close'}
