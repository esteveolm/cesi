# -*- coding: utf-8 -*-
from odoo import http

# class Cesi(http.Controller):
#     @http.route('/cesi/cesi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cesi/cesi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cesi.listing', {
#             'root': '/cesi/cesi',
#             'objects': http.request.env['cesi.cesi'].search([]),
#         })

#     @http.route('/cesi/cesi/objects/<model("cesi.cesi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cesi.object', {
#             'object': obj
#         })