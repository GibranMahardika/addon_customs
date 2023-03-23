from odoo import fields, models

class resPartner(models.Model):
    _inherit = 'res.partner'
    
    # agama = fields.Char('Agama', required=True)