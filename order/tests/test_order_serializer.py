from unittest import TestCase

import pytest

from order.factories import OrderFactory
from order.serializers.order_serializer import OrderSerializer
from product.factories import ProductFactory


@pytest.mark.django_db
class TestOrderSerializer(TestCase):
    def setUp(self):
        self.product_a = ProductFactory()
        self.product_b = ProductFactory()

        self.order = OrderFactory(product=(self.product_a, self.product_b))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_is_serialized(self):

        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data["product"][0]["title"], self.product_a.title)
        self.assertEqual(serializer_data["product"][0]["title"], self.product_a.title)

        valor_total_dos_produtos = self.product_a.price + self.product_b.price
        self.assertEqual(serializer_data["total"], valor_total_dos_produtos)
