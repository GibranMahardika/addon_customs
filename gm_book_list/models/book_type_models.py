from odoo import fields, models, api, _

class bookType(models.Model):
      _name = 'book.type'
      _description = "Type of Books"
      _inherit = ["mail.thread", "mail.activity.mixin"]

      name = fields.Char(string="Name", tracking=True)

      book_list_ids = fields.One2many('book.list', 'kategori_buku_id', tracking=True)