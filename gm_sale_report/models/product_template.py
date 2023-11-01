from odoo import fields, models, api

class productTemplateInherit(models.Model):
    _inherit = 'product.template'
    _description = "Product Template Inherit"

    brand_id = fields.Many2one('product.brand', compute="_compute_product_brand", store=True)
    name_brand = fields.Char(string="Name Brand", compute="_compute_nama_brand", store=True)

    @api.depends('brand_ids')
    def _compute_product_brand(self):
        for x in self:
            if x.brand_ids:
                x.brand_id = x.brand_ids[0]

    @api.depends('brand_ids')
    def _compute_nama_brand(self):
        for y in self:
            if y.brand_ids:
                y.name_brand = ', '.join( y.brand_ids.mapped('brand_name')) #untuk menghubungi