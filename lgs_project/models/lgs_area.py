from odoo import fields, models


class lgsArea(models.Model):
    _name = 'lgs.area'
    _description = 'model for Area of LGS Company'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    
    name = fields.Char(string="Name", tracking=True)
    code = fields.Char(string="Kode", tracking=True, related='origin_id.name', store=True)
    origin_id = fields.Many2one('origin.type', string="Origin", tracking=True)