# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BudgetReleases(models.Model):
    _name = 'budget.release'
    _description = 'BudgetReleases'

    name = fields.Char()
    date = fields.Date(
        string='Date',
        required=False)
    amount = fields.Float(
        string='Amount',
        required=False)
    budget_line = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Budget line',
        required=False)


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    budget_releases = fields.One2many(
        comodel_name='budget.release',
        inverse_name='budget_line',
        string='Budget_releases',
        required=False)



# class budget_releases(models.Model):
#     _name = 'budget_releases.budget_releases'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100