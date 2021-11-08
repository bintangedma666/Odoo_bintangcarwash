# -*- coding: utf-8 -*-
# from odoo import http


# class Bintangcarwash(http.Controller):
#     @http.route('/bintangcarwash/bintangcarwash/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bintangcarwash/bintangcarwash/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bintangcarwash.listing', {
#             'root': '/bintangcarwash/bintangcarwash',
#             'objects': http.request.env['bintangcarwash.bintangcarwash'].search([]),
#         })

#     @http.route('/bintangcarwash/bintangcarwash/objects/<model("bintangcarwash.bintangcarwash"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bintangcarwash.object', {
#             'object': obj
#         })
