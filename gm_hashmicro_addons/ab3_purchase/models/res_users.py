from odoo import _, api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    job_position = fields.Char(string='Job Position')
