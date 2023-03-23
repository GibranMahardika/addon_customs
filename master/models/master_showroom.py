from odoo import fields, models, api, _

class masterShowroom(models.Model):
    _name = 'master.showroom'    
    _description = 'Module for collect all about data'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", tracking=True, required=True)
    code = fields.Char(string="Code", tracking=True, required=True)
    
class masterShowroomHeader(models.Model):
    _name = 'master.showroom.header'
    _description = 'a new table Master Showroom Header'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    is_cdb = fields.Boolean(string="CDB", tracking=True)
    type_cdb = fields.Many2one('type.cdb', string="Type CDB", tracking=True)
    question = fields.Char(string='Question', tracking=True)
    
class typeCDB(models.Model):
    _name = 'type.cdb'
    _description = 'a new table Type CDB'
    _inherit = ['mail.thread', 'mail.activity.mixin']