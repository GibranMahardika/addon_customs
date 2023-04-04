from odoo import fields, models, api, _

class originType(models.Model):
    _name = 'origin.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    kode = fields.Char(string="Kode", tracking=True,
                       related='name', readonly=True, store=True)