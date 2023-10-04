from odoo import fields, models, api, _

class bookChapter(models.Model):
    _name = 'book.chapter'
    _description = "Bab Buku"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    chap_name = fields.Char(string="BAB", tracking=True)
    keterangan = fields.Text(string="Keterangan", tracking=True)
    halaman = fields.Integer(string="Halaman", tracking=True)
    hal_extra = fields.Integer(string="Hal. Extra", tracking=True)
    hal_extra_2 = fields.Integer(string="Hal. Extra", tracking=True)

    book_list_id = fields.Many2one('book.list')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'book.chapter.sequence') or _('New')
            result = super(bookChapter, self).create(vals)
        return result