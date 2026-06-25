# Copyright 2026 Antigravity
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Debranded Retail and Marketplace Setup",
    "summary": "Debrands the system and configures 10 selling outlets and 10 vendor portal accounts.",
    "version": "18.0.1.0.0",
    "category": "Customization",
    "author": "Antigravity, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-brand",
    "license": "AGPL-3",
    "depends": [
        "portal",
        "point_of_sale",
        "website_sale",
        "base_setup",
        "l10n_sa",
    ],
    "data": [
        "views/debranding_views.xml",
        "data/selling_outlets_data.xml",
        "data/vendor_portal_data.xml",
        "data/localization_data.xml",
    ],
    "installable": True,
    "application": True,
}
