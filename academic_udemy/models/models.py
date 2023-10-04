# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name")
    description = fields.Text("Description")
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible")