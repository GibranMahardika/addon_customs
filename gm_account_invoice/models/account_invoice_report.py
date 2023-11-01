# -*- coding: utf-8 -*-

from odoo import models, fields, api
import traceback

class accountInvoiceReportInherit(models.Model):
    _inherit = 'account.invoice.report'
    _description = 'Account Invoice Report Inherit'

    campaign_id = fields.Many2one('utm.campaign', string='Campaign')
    city_id = fields.Many2one('res.city', string='City')
    medium_id = fields.Many2one('utm.medium', string='Medium')
    source_id = fields.Many2one('utm.source', string="Source")

    def _select(self):
        # traceback.extract_stack()
        print("query 1 is : ", super(accountInvoiceReportInherit, self)._select())
        return super(accountInvoiceReportInherit, self)._select() + ", move.campaign_id as campaign_id, move.medium_id as medium_id, move.source_id, partner.city_id as city_id"

    # def _select(self):
    #     return super(accountInvoiceReportInherit, self)._select() + ", move.utm_campaign_id as campaign_id, move.city_id as city_id, move.utm_medium_id as medium_id, move.utm_source_id as source_id"

