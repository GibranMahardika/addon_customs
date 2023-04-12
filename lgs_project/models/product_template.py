from odoo import fields, models

class productTemplateInherit(models.Model):
    _inherit = 'product.template'
    
    lgs_pricelist_id = fields.Many2one('lgs.pricelist')
    
    