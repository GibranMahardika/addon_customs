from odoo import fields, models, api, _


class productSupplierInfoInherit(models.Model):
    _inherit = 'product.supplierinfo'

    taxes_id = fields.Many2one(
        'account.tax',
        string="Taxes"
    )

    # taxes_id = fields.Many2one(
    #     'account.tax',
    #     string="Taxes",
    #     default=lambda self: self.env['account.tax'].search([('type_tax_use', '=', 'purchase'), ('active', '=', True)],
    #                                                         limit=1),
    # )

    discount = fields.Char("Discount")
