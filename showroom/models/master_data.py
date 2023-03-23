from odoo import fields, models, api, _

class masterData(models.Model):
    _name =  'mstr.data'
    _description = 'Module for collect all about data'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", tracking=True, required=True)
    code = fields.Char(string="Code", tracking=True, required=True)
    