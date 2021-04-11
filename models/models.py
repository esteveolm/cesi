# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cesiPartner(models.Model):
    _inherit = 'res.partner'
    
    cesitype = fields.Selection([
        ('student', 'Unconnected Student'),
        ('student_online', 'Connected Student'),
        ('donor', 'Possible Donor'),
        ('donor_online', 'Donor')
    ], string='Contact Type', help="CESI contact type.")

# class cesi(models.Model):
#     _name = 'cesi.cesi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100