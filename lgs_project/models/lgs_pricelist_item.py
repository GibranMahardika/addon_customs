from odoo import fields, models, api, _


class lgsPricelistItem(models.Model):
    _name = 'lgs.pricelist.item'
    _description = 'table item of LGS Pricelist'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    pricelist_id = fields.Many2one('lgs.pricelist')

    is_fixed_price = fields.Boolean(string=" Is Fixed Price", tracking=True)
    is_changed_price = fields.Boolean(string="Is Changed Price", tracking=True)

    fixed_price = fields.Float(
        string="Fixed Price", tracking=True, required=True)
    change_price = fields.Float(string="Change Price", tracking=True)

    periode = fields.Char(string="Expired Date", tracking=True)
    date_start = fields.Datetime(string="Expired Date", tracking=True)
    date_end = fields.Datetime("", tracking=True)

    apply_on = fields.Many2one(
        'lgs.pricelist.master', string="Apply On", tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 'Currency',
        readonly=True, related='pricelist_id.currency_id', store=True)

    company_id = fields.Many2one(
        'res.company', 'Company',
        readonly=True, related='pricelist_id.company_id', store=True)

    model_id = fields.Many2one(
        'fleet.vehicle.model', string="Car Model", tracking=True, required=True)
