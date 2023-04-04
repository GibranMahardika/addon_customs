from odoo import fields, models, api, _


class lgsPricelistMaster(models.Model):
    _name = 'lgs.pricelist.master'
    _description = 'master table for LGS Pricelist'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    
