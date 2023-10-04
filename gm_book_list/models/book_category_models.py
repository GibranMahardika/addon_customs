from odoo import fields, models, api, _

class bookCategory(models.Model):
      _name = 'book.category'
      _description = "Kategori Buku"
      _inherit = ["mail.thread", "mail.activity.mixin"]

      name = fields.Char(string="Name", tracking=True)

      book_list_ids = fields.One2many('book.list', 'kategori_buku_id', tracking=True)

      @api.model
      def create(self, vals):
            if vals.get('name', _('New')) == _('New'):
                  vals['name'] = self.env['ir.sequence'].next_by_code(
                  'book.chapter.sequence') or _('New')
                  result = super(bookCategory, self).create(vals)
            return result