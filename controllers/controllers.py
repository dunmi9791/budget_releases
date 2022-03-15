# -*- coding: utf-8 -*-
from odoo import http

# class BudgetReleases(http.Controller):
#     @http.route('/budget_releases/budget_releases/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/budget_releases/budget_releases/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('budget_releases.listing', {
#             'root': '/budget_releases/budget_releases',
#             'objects': http.request.env['budget_releases.budget_releases'].search([]),
#         })

#     @http.route('/budget_releases/budget_releases/objects/<model("budget_releases.budget_releases"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('budget_releases.object', {
#             'object': obj
#         })