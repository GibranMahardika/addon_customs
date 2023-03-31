from odoo import fields, models


class lgsIdemitsu(models.Model):
    _name = 'lgs.idemitsu'
    _rec_name = 'name'

    company_id = fields.Many2one(
        'res.company', string="Company", tracking=True, required=True)

    # tab Pricelist Reguler
    area_id 
    # tab Pricelist Tanggerang

    # tab Pricelist Medan
