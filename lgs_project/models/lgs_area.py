from odoo import fields, models, api, _

class lgsArea(models.Model):
    _name = 'lgs.area'
    _description = 'model for Area of LGS Company'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", tracking=True, required=True)