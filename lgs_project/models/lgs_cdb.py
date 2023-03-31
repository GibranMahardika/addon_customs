from odoo import fields, models, api, _

class lgsCDB(models.Model):
    _name = 'lgs.cdb'
    _description = "module for customer database of LGS"
    
    name = fields.Char(string="Nama Lembaga")