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
        'res.partner', string="Company", tracking=True, required=True)
    
    origin_id = fields.Many2one(
        'lgs.area', string="Origin", tracking=True, required=True)
    
    destination_id = fields.Many2one(
        'lgs.area', string="Destination", tracking=True)
    
    model_id = fields.Many2one(
        'fleet.vehicle', string="Vehicle Model", tracking=True)
    
    price = fields.Integer(string="Price", translate=True, tracking=True)
    
    # CONNECTOR
    item_ids = fields.One2many('lgs.pricelist.item', 'pricelist_id')
    cdb_id = fields.Many2one('lgs.cdb', tracking=True)
