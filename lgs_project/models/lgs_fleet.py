from odoo import fields, models, api, _


class lgsFleet(models.Model):
    _name = 'lgs.fleet'
    _description = 'module custom Fleet for LGS Company'    
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # name = fields.Char(string="Name", tracking=True, required=True)
    # model_id = fields.Many2one(
    #     'lgs.vehicle.model', string="Model", tracking=True, required=True)
    # license_plate = fields.Char(
    #     string="License Plate", tracking=True, required=True)
    # tags_ids = fields.Many2many(
    #     'lgs.vehicle.tag', string="Tags", tracking=True, required=True)

    # # driver
    # driver_id = fields.Many2one(
    #     'lgs.employee', string="Driver", tracking=True, required=True)
    # driver_next_id = fields.Many2one(
    #     'lgs.employee', string="Driver Future", tracking=True, required=True)
    # assignment_date = fields.Date(string="Assignment Date")

    # # vehicle
    # chasis_number = fields.Char(
    #     string="Chassis Number", tracking=True, required=True)
    # manager_id = fields.Many2one(
    #     'lgs.manager', string="Fleet Manager", tracking=True, required=True)
    # location = fields.Char(string="Location", tracking=True)
    # company_id = fields.Many2one(
    #     'res.company', string="Company", tracking=True)

    # # tab Model
    # model_year = fields.Char(string="Model Year", tracking=True)
    # transmission = fields.Selection([
    #     ('auto', 'Automatic'),
    #     ('manual', 'Manul'),
    # ], string="Transmission", tracking=True)
    # color = fields.Char(string="Color", tracking=True)
    # horsepower = fields.Integer(string="Horsepower", tracking=True)
    # power = fields.Integer(string="Power", tracking=True)
    # fuel_type = fields.Selection([
    #     ('disel', 'Disel'),
    #     ('bensin', 'Bensin'),
    # ], string="Transmission", tracking=True)
