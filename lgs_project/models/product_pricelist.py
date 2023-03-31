from odoo import fields, models

class productPricelist(models.Model):
    _inherit = 'product.pricelist'
    
    area_id = fields.Many2one('lgs.area', string="Area", tracking=True, required=True)