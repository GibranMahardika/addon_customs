from odoo import fields, models, api, _

class accountMultipaymentInherit(models.Model):
    _inherit = "account.multipayment"
    _description = "Account Multipayment"

    is_customer = fields.Boolean(string="Is a Customer")
    is_vendor = fields.Boolean(string="Is a Vendor")

    @api.onchange('partner_id')
    def _onchange_customer_vendor(self):
        for x in self:
            if x.partner_id:
                partner = self.env['res.partner'].search([('is_customer','=',x.is_customer),('is_vendor','=',x.is_vendor)])