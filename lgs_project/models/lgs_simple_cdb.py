from odoo import fields, models, api, _

class simpleCDB(models.Model):
    _name = 'simple.cdb'
    
    customer_id = fields.Many2one('res.partner', string="Customer", tracking=True)