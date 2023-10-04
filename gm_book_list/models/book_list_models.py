from odoo import fields, models, api, _

class bookList(models.Model):
    _name = 'book.list'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Book List"
    _rec_name = "name"

    name = fields.Char(string="Nama Buku", required=False, Tracking=True, copy=True,
                       default=lambda self: _('New'))
    pengarang = fields.Char(string="Pengarang", required=False, Tracking=True)
    tgl_terbit = fields.Date(string="Tanggal Terbit", required=False, Tracking=True)
    # jenis_buku = fields.Selection([
    #     ('sd', 'SD'),
    #     ('ipa', 'IPA'),
    #     ('ips', 'IPS')],
    #     default='', required=False, copy=True)
    jenis_buku_id = fields.Many2one('book.type', string='Jenis Buku', required=False, tracking=True)
    kategori_buku_id = fields.Many2one('book.category', string="Kategori Buku", tracking=True)
    state = fields.Selection([
        (' ', ' '),
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')],
        default=' ', copy=False, tracking=True)
    tag_ids = fields.Many2many('book.type', string='Tags', tracking=True)

    bab_buku_ids = fields.One2many('book.chapter', 'book_list_id')

    @api.model
    def create(self, vals):
        vals['state'] = 'draft'
        return super(bookList, self).create(vals)
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'book.list.sequence') or _('New')
            result = super(bookList, self).create(vals)
        return result


    def btn_draft(self):
            self.write({'draft': 'Draft'})
            message = 'State on Draft'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

    def btn_done(self):
            self.write({'done': 'Done'})
            message = 'State on Done'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

    def btn_cancel(self):
            self.write({'cancel': 'Cancel'})
            message = 'State on Cancel'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }