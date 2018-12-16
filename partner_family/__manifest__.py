# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Family",
    "summary": "",
    "version": "11.0.1.0.0",
    # see https://odoo-community.org/page/development-status
    "development_status": "Alpha",
    "category": "Uncategorized",
    "website": "https://github.com/humanilog/partner-contact/tree/11.0_partner_family/partner_family",
    "author": "Ben Brich (humanilog), Odoo Community Association (OCA)",
    # see https://odoo-community.org/page/maintainer-role for a description of the maintainer role and responsibilities
    "maintainers": ["HaGuesto"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,

    "depends": [
        "base",
    ],
    "data": [
        "views/res_partner.xml"
    ],

}
