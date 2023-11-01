from odoo import fields, models, api, _

class purchaseOrder(models.Model):
    _inherit = "purchase.order"

    # order_line_ids = fields.One2many(relates="order_line")
