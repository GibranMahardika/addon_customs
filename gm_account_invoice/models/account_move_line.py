from odoo import fields, models, api

class accountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'
    _description = 'Account Move Line = Journal Item, inherit'

    campaign_id = fields.Many2one('utm.campaign')
    medium_id = fields.Many2one('utm.medium', string='Medium')
    source_id = fields.Many2one('utm.source', string="Source")