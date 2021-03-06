# coding: utf-8
# © 2016 Vauxoo
#   Coded by: lescobar@vauxoo.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Runbot Send Email Result",
    "summary": "This module sends the results of the RunBot builds through \
email.",
    "version": "8.0.1.0.0",
    "category": "runbot",
    "website": "https://www.vauxoo.com",
    "author": "Vauxoo,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "runbot",
        "fetchmail",
    ],
    "data": [
        'security/runbot_groups.xml',
        'security/ir.model.access.csv',
        "views/runbot_send_email_view.xml",
        "views/assets.xml",
        "data/runbot_send_email_data.xml",
    ],
    "demo": [
        "demo/ir_mail_server_demo.xml",
    ],
    'qweb': [
        'static/src/xml/runbot_template.xml',
    ],
    "application": False,
    "installable": True,
}
