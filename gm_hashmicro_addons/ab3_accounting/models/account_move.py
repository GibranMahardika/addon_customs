from odoo import fields, models, api, _


class accountMoveInherit(models.Model):
    _inherit = 'account.move'
    _description = 'AB3 Account Move Inherit'

    @api.depends(
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.debit',
        'line_ids.credit',
        'line_ids.currency_id',
        'line_ids.amount_currency',
        'line_ids.amount_residual',
        'line_ids.amount_residual_currency',
        'line_ids.payment_id.state',
        'line_ids.full_reconcile_id', 'discount_method', 'discount_type', 'discount_amount')
    def _compute_pph_ppn_tax(self):
        for x in self:
            ppn = 0.0
            pph = 0.0
            for y in x.line_ids:
                if y.tax_line_id.tax_scope == 'service' and y.tax_line_id.tax_type == 'pph':
                    pph += y.balance
                elif y.tax_line_id.tax_scope != 'service' and y.tax_line_id.tax_type == 'pph':
                    ppn = 0

                elif y.tax_line_id.tax_scope != 'service' and y.tax_line_id.tax_type == 'ppn':
                    ppn += y.balance
                elif y.tax_line_id.tax_scope == 'service' and y.tax_line_id.tax_type == 'ppn':
                    pph = 0

                elif y.tax_line_id.tax_scope != 'service' and y.tax_line_id.tax_type == '':
                    ppn += y.balance
                elif y.tax_line_id.tax_scope == 'service' and y.tax_line_id.tax_type == '':
                    pph += y.balance

            if x.move_type == 'entry' or x.is_outbound():
                sign = 1
            else:
                sign = -1

            x.pph_tax = sign * pph
            x.ppn_tax = sign * ppn

            x.amount_tax = x.ppn_tax + x.pph_tax
            x.amount_total = x.amount_untaxed - x.discount_amt - x.amount_tax

    pph_tax = fields.Monetary(string="PPH", compute="_compute_pph_ppn_tax", currency_field='currency_id', store=True)
    ppn_tax = fields.Monetary(string="PPN", compute="_compute_pph_ppn_tax", currency_field='currency_id', store=True)