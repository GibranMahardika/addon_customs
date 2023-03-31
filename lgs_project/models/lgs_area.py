from odoo import fields, models, api, _


class lgsArea(models.Model):
    _name = 'lgs.area'
    _description = 'model for Area of LGS Company'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True)
    origin_type_id = fields.Many2one('origin.type', string="Origin Type")


class originType(models.Model):
    _name = 'origin.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", tracking=True)
    kode = fields.Char(string="Kode", tracking=True)
    
    area_ids = fields.One2many('lgs.area', 'origin_type_id')