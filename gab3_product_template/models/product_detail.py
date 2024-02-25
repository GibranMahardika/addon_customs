from odoo import fields, models, api, _

class productDetail(models.Model):
    _name = 'product.detail'
    _description = 'Product Detail'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')