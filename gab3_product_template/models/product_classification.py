from odoo import fields, models, api, _

class productClassification(models.Model):
    _name = 'product.classification'
    _description = 'Product Classification'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')