# -*- coding: utf-8 -*-
# from odoo import http


# class HrFamily(http.Controller):
#     @http.route('/hr_family/hr_family/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_family/hr_family/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_family.listing', {
#             'root': '/hr_family/hr_family',
#             'objects': http.request.env['hr_family.hr_family'].search([]),
#         })

#     @http.route('/hr_family/hr_family/objects/<model("hr_family.hr_family"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_family.object', {
#             'object': obj
#         })
