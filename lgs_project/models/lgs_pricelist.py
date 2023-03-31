from odoo import fields, models, _, api


class lgsPricelist(models.Model):
    _name = 'lgs.pricelist'
    _description = 'module custom Pricelist for LGS Company'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    name = fields.Char(string="", tracking=True, required=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=_get_default_currency_id, tracking=True, required=True)
    company_id = fields.Many2one(
        'res.company', string="Company", tracking=True, required=True)
    area_id = fields.Many2one(
        'lgs.area', string="Area", tracking=True, required=True)

    item_ids = fields.One2many('lgs.pricelist.item', 'pricelist_id')
