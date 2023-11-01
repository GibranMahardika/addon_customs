# -*- coding: utf-8 -*-

from odoo import models, fields


class saleReportInherit(models.Model):
    _inherit = 'sale.report'
    _description = "Sale Report Inherited"

    brand_id = fields.Many2one('product.brand', string="Brand")
    name_test = fields.Char(string="Name Test")
    

    # def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
    #     select_ = '''
    #         t.brand_id        
    #     '''
    #     for field in fields.values():
    #         select_ += field
        
    #     from_ = '''
    #         FROM sale_report s
    #         '''
        
    #     join_ = '''
    #         JOIN product_template t ON s.product_tmpl_id = t.id
    #     '''
        
    #     query = select_ + from_ + join_
        
    #     return super(saleReportInherit, self)._query(with_clause, fields, groupby, query)
    
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['brand_id'] = ", t.brand_id as brand_id"
        fields['name_test'] = ", t.name_brand as name_test"
        groupby += ', t.brand_id'         
        groupby += ', t.name_brand'         
        return super(saleReportInherit, self)._query(with_clause, fields, groupby, from_clause)
    
