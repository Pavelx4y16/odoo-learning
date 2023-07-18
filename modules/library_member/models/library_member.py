from odoo import fields, models


class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    card_number = fields.Char()
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        delegate=True,
        ondelete="cascade",
        required=True
    )

