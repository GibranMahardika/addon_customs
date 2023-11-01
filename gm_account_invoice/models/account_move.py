from odoo import fields, models, api

class accountMoveInherit(models.Model):
    _inherit = 'account.move'
    _description = 'Inherit of Journal Entry model account.move'

    campaign_id = fields.Many2one('utm.campaign', string='Campaign')
    city_id = fields.Many2one('res.city', string='City')
    medium_id = fields.Many2one('utm.medium', string='Medium')
    source_id = fields.Many2one('utm.source', string="Source")