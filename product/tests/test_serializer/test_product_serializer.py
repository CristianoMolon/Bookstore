from unittest import TestCase

import pytest

from product.factories import CategoryFactory, ProductFactory
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
class testProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="Smartphones")
        self.product = ProductFactory(
            title="Iphone", price=10000, category=[self.category]
        )

        self.serializer = ProductSerializer(self.product)

    def test_product_is_serialized(self):
        serializer_data = self.serializer.data
        self.assertEqual(serializer_data["title"], "Iphone")
        self.assertEqual(serializer_data["price"], 10000)
        self.assertEqual(serializer_data["category"][0]["title"], self.category.title)
