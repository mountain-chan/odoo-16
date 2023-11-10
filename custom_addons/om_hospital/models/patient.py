from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Records'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string="Age")
    notes = fields.Text(string="Notes")
