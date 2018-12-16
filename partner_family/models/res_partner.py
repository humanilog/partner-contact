# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ResPartner(models.Model):
    """Adds family value to partner comapny type."""
    _inherit = 'res.partner'

    company_type = fields.Selection(selection_add=[('family', 'Family')])