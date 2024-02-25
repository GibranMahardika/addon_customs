from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'AB3 Sale Order'

    source_so = fields.Selection([
        ('wa', 'WhatsApp'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('po', 'PO')],
        string='Source SO')

    source_po = fields.Char(string='Number PO Customer')