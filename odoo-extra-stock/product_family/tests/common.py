# Copyright 2018 Daniel Campos <danielcampos@avanzosc.es> - Avanzosc S.L.
# Copyright 2021 Camptocamp SA
# @author: Simone Orsi <simone.orsi@camptocamp.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class CommonCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.product = cls.env.ref("product.product_product_4")
        cls.supplier = cls.env.ref("base.res_partner_2")
        cls.product_family_obj = cls.env["product.family"]
        cls.product_family = cls.product_family_obj.create(
            {
                "name": "Test family",
                "description": "Test family description",
                "partner_id": cls.supplier.id,
            }
        )
