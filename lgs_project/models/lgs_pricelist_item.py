from odoo import fields, models, api, _


class lgsPricelistItem(models.Model):
    _name = 'lgs.pricelist.item'
    _description = 'table item of LGS Pricelist'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    pricelist_id = fields.Many2one('lgs.pricelist')

    is_fixed_price = fields.Boolean(string=" Is Fixed Price", tracking=True)

    fixed_price = fields.Float(
        string="Price", tracking=True)

    periode = fields.Char(string="Price Periode", tracking=True)
    date_start = fields.Datetime(string="Price Periode Start", tracking=True)
    date_end = fields.Datetime("", tracking=True)
