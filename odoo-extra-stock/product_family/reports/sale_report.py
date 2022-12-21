# Copyright 2018 Tecnativa - David Vidal
# Copyright 2020 Tecnativa - João Marques
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    product_family_id = fields.Many2one(comodel_name="product.family", string="family")

    def _query(self, with_clause="", fields=None, groupby="", from_clause=""):
        fields = fields or {}
        fields["product_family_id"] = ", t.product_family_id as product_family_id"
        groupby += ", t.product_family_id"
        return super()._query(with_clause, fields, groupby, from_clause)
