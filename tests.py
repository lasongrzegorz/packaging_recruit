import unittest
from main import ProductA, Package


class TestProductA(unittest.TestCase):

    product_a = ProductA()

    def _expected_packages_count(
        self,
        small_pack_count,
        medium_pack_count,
        large_pack_count,
        collective_pack_count,
    ):
        return {
            "small_pack_count": small_pack_count,
            "medium_pack_count": medium_pack_count,
            "large_pack_count": large_pack_count,
            "collective_pack_count": collective_pack_count,
        }

    def test_calculate_product_as_count(self):
        self.assertEqual(
            self.product_a.calculate_packages_count(1),
            self._expected_packages_count(1, 0, 0, 0),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(4),
            self._expected_packages_count(0, 1, 0, 0),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(7),
            self._expected_packages_count(0, 0, 1, 0),
        )
        # algorithm exception
        self.assertEqual(
            self.product_a.calculate_packages_count(10),
            self._expected_packages_count(0, 2, 0, 1),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(12),
            self._expected_packages_count(0, 2, 0, 1),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(13),
            self._expected_packages_count(0, 0, 2, 1),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(18),
            self._expected_packages_count(0, 0, 2, 1),
        )

        self.assertEqual(
            self.product_a.calculate_packages_count(19),
            self._expected_packages_count(1, 0, 2, 1),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(27),
            self._expected_packages_count(0, 0, 3, 1),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(28),
            self._expected_packages_count(1, 0, 3, 2),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(31),
            self._expected_packages_count(0, 1, 3, 2),
        )
        self.assertEqual(
            self.product_a.calculate_packages_count(66),
            self._expected_packages_count(1, 0, 7, 4),
        )
        with self.assertRaises(Exception) as err:
            self.assertEqual(
                err.exception,
                Exception(
                    "Order size must be a positive value lower than or equal 100"
                ),
            )

    def test_get_small_pack_count(self):
        self.assertEqual(self.product_a._get_small_pack_count(1), 1)
        self.assertEqual(self.product_a._get_small_pack_count(2), 1)
        self.assertEqual(self.product_a._get_small_pack_count(3), 1)
        self.assertEqual(self.product_a._get_small_pack_count(4), 0)
        self.assertEqual(self.product_a._get_small_pack_count(5), 0)
        self.assertEqual(self.product_a._get_small_pack_count(6), 0)
        self.assertEqual(self.product_a._get_small_pack_count(7), 0)
        self.assertEqual(self.product_a._get_small_pack_count(8), 0)

    def test_get_medium_pack_count(self):
        self.assertEqual(self.product_a._get_medium_pack_count(1), 0)
        self.assertEqual(self.product_a._get_medium_pack_count(2), 0)
        self.assertEqual(self.product_a._get_medium_pack_count(3), 0)
        self.assertEqual(self.product_a._get_medium_pack_count(4), 1)
        self.assertEqual(self.product_a._get_medium_pack_count(5), 1)
        self.assertEqual(self.product_a._get_medium_pack_count(6), 1)
        self.assertEqual(self.product_a._get_medium_pack_count(7), 0)
        self.assertEqual(self.product_a._get_medium_pack_count(8), 0)

    def test_add_extra_large_pack(self):
        self.assertFalse(self.product_a._add_extra_large_pack(1))
        self.assertFalse(self.product_a._add_extra_large_pack(2))
        self.assertFalse(self.product_a._add_extra_large_pack(3))
        self.assertFalse(self.product_a._add_extra_large_pack(4))
        self.assertFalse(self.product_a._add_extra_large_pack(5))
        self.assertFalse(self.product_a._add_extra_large_pack(6))
        self.assertTrue(self.product_a._add_extra_large_pack(7))
        self.assertTrue(self.product_a._add_extra_large_pack(8))

    def test_get_collecting_pack_count(self):
        self.assertEqual(self.product_a._get_collecting_pack_count(1, 0, 3), 2)
        self.assertEqual(self.product_a._get_collecting_pack_count(0, 1, 3), 2)
        self.assertEqual(self.product_a._get_collecting_pack_count(0, 1, 4), 2)
        self.assertEqual(self.product_a._get_collecting_pack_count(1, 0, 4), 2)
        self.assertEqual(self.product_a._get_collecting_pack_count(1, 0, 5), 3)
        self.assertEqual(self.product_a._get_collecting_pack_count(0, 1, 5), 3)
        self.assertEqual(self.product_a._get_collecting_pack_count(1, 0, 9), 5)
        self.assertEqual(self.product_a._get_collecting_pack_count(1, 0, 10), 5)


class TestPackage(unittest.TestCase):

    package = Package()

    def _expected_packages_count(
        self,
        small_pack_count,
        medium_pack_count,
        large_pack_count,
        collective_pack_count,
    ):
        return {
            "small_pack_count": small_pack_count,
            "medium_pack_count": medium_pack_count,
            "large_pack_count": large_pack_count,
            "collective_pack_count": collective_pack_count,
        }

    def test_calculate_packages_count(self):
        self.assertEqual(
            self.package.calculate_packages_count(5),
            self._expected_packages_count(0, 1, 0, 0),
        )
        self.assertEqual(
            self.package.calculate_packages_count(13),
            self._expected_packages_count(0, 1, 1, 1),
        )
        self.assertEqual(
            self.package.calculate_packages_count(27),
            self._expected_packages_count(0, 0, 3, 1),
        )
        self.assertEqual(
            self.package.calculate_packages_count(28),
            self._expected_packages_count(1, 0, 3, 2),
        )
        self.assertEqual(
            self.package.calculate_packages_count(31),
            self._expected_packages_count(0, 1, 3, 2),
        )
        self.assertEqual(
            self.package.calculate_packages_count(66),
            self._expected_packages_count(1, 0, 7, 4),
        )
        with self.assertRaises(Exception) as err:
            self.assertEqual(
                err.exception,
                Exception(
                    "Order size must be a positive value lower than or equal 100"
                ),
            )

    def test_get_small_pack_count(self):
        self.assertEqual(self.package._get_small_pack_count(1), 1)
        self.assertEqual(self.package._get_small_pack_count(2), 1)
        self.assertEqual(self.package._get_small_pack_count(3), 1)
        self.assertEqual(self.package._get_small_pack_count(4), 0)
        self.assertEqual(self.package._get_small_pack_count(5), 0)
        self.assertEqual(self.package._get_small_pack_count(6), 0)
        self.assertEqual(self.package._get_small_pack_count(7), 0)
        self.assertEqual(self.package._get_small_pack_count(8), 0)

    def test_get_medium_pack_count(self):
        self.assertEqual(self.package._get_medium_pack_count(1), 0)
        self.assertEqual(self.package._get_medium_pack_count(2), 0)
        self.assertEqual(self.package._get_medium_pack_count(3), 0)
        self.assertEqual(self.package._get_medium_pack_count(4), 1)
        self.assertEqual(self.package._get_medium_pack_count(5), 1)
        self.assertEqual(self.package._get_medium_pack_count(6), 1)
        self.assertEqual(self.package._get_medium_pack_count(7), 0)
        self.assertEqual(self.package._get_medium_pack_count(8), 0)

    def test_add_extra_large_pack(self):
        self.assertFalse(self.package._add_extra_large_pack(1))
        self.assertFalse(self.package._add_extra_large_pack(2))
        self.assertFalse(self.package._add_extra_large_pack(3))
        self.assertFalse(self.package._add_extra_large_pack(4))
        self.assertFalse(self.package._add_extra_large_pack(5))
        self.assertFalse(self.package._add_extra_large_pack(6))
        self.assertTrue(self.package._add_extra_large_pack(7))
        self.assertTrue(self.package._add_extra_large_pack(8))

    def test_get_collecting_pack_count(self):
        self.assertEqual(self.package._get_collecting_pack_count(1, 0, 3), 2)
        self.assertEqual(self.package._get_collecting_pack_count(0, 1, 3), 2)
        self.assertEqual(self.package._get_collecting_pack_count(0, 1, 4), 2)
        self.assertEqual(self.package._get_collecting_pack_count(1, 0, 4), 2)
        self.assertEqual(self.package._get_collecting_pack_count(1, 0, 5), 3)
        self.assertEqual(self.package._get_collecting_pack_count(0, 1, 5), 3)
        self.assertEqual(self.package._get_collecting_pack_count(1, 0, 9), 5)
        self.assertEqual(self.package._get_collecting_pack_count(1, 0, 10), 5)


if __name__ == "__main__":
    unittest.main()
