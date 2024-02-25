from odoo import fields, models, api, _


class accountTaxInherit(models.Model):
    _inherit = 'account.tax'
    _description = 'AB3 Account Tax Inherit'

    tax_type = fields.Selection([
        ('pph', 'PPH'),
        ('ppn', 'PPN')
    ], string='PPN / PPH')
