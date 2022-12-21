# Copyright 2009 NetAndCo (<http://www.netandco.net>).
# Copyright 2011 Akretion Benoît Guillot <benoit.guillot@akretion.com>
# Copyright 2014 prisnet.ch Seraphine Lantible <s.lantible@gmail.com>
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# Copyright 2018 Daniel Campos <danielcampos@avanzosc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class Productfamily(models.Model):
    _name = "product.family"
    _description = "Product Family"
    _order = "name"

    name = fields.Char("Family Name", required=True)
    description = fields.Text(translate=True)
    buho_id = fields.Char("Buho ID")

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        help="Select a partner for this family if any.",
        ondelete="restrict",
    )
    logo = fields.Binary("Logo File")
    product_ids = fields.One2many(
        "product.template", "product_family_id", string="family Products"
    )
    products_count = fields.Integer(
        string="Number of products", compute="_compute_products_count"
    )

    @api.depends("product_ids")
    def _compute_products_count(self):
        product_model = self.env["product.template"]
        groups = product_model.read_group(
            [("product_family_id", "in", self.ids)],
            ["product_family_id"],
            ["product_family_id"],
            lazy=False,
        )
        data = {group["product_family_id"][0]: group["__count"] for group in groups}
        for family in self:
            family.products_count = data.get(family.id, 0)
