# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import fields, models


class SaleOrderDuplicationWizardDateLine(models.TransientModel):
    _name = 'sale.order.duplication.wizard.date.line'

    wizard_id = fields.Many2one(
        comodel_name='sale.order.duplication.wizard')

    date = fields.Date(string='Date', required=True)
