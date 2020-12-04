"""
Script is to colculate number of packs (three sizes available: small,
medium, large) needed to pack the order as well as a number of collective
packs used for shipping order, whenever more than 1 pack is used.
"""


class ProductA:
    def __init__(self):
        self.small_pack_size = 3
        self.medium_pack_size = 6
        self.large_pack_size = 9
        self.min_order_size = 0
        self.max_order_size = 100

    def _get_small_pack_count(self, remainder):
        """Count small size packs needed for shipping order"""
        if 0 < remainder <= self.small_pack_size:
            small_pack_count = 1
        else:
            small_pack_count = 0
        return small_pack_count

    def _get_medium_pack_count(self, remainder):
        """Count medium size packs needed for shipping order"""
        if self.small_pack_size < remainder <= self.medium_pack_size:
            medium_pack_count = 1
        else:
            medium_pack_count = 0
        return medium_pack_count

    def _add_extra_large_pack(self, remainder):
        """Check if additional large pack is needed for the remainder stock"""
        if self.medium_pack_size < remainder <= self.large_pack_size:
            return True
        else:
            return False

    def _get_collecting_pack_count(
        self, small_pack_count, medium_pack_count, large_pack_count
    ):
        """Count collective packs needed for packing product packs"""
        return (small_pack_count + medium_pack_count + large_pack_count) // 2

    def calculate_packages_count(self, order_size):
        """Calculate number of packages required for shipping a given order size"""

        if not self.min_order_size <= order_size <= self.max_order_size:
            raise Exception("Order size must be positive value lower than or equal 100")

        small_pack_count = 0
        medium_pack_count = 0
        large_pack_count = 0

        remainder = order_size % self.large_pack_size
        if self.large_pack_size < order_size <= self.large_pack_size * 2:
            if 0 < remainder <= self.small_pack_size:
                medium_pack_count = 2
            else:
                large_pack_count = 2
        else:
            # get number completely filled large packs
            large_pack_count = order_size // self.large_pack_size

            # add extra pack depending on the reminder
            remainder = order_size - large_pack_count * self.large_pack_size
            small_pack_count = self._get_small_pack_count(remainder)
            medium_pack_count = self._get_medium_pack_count(remainder)
            large_pack_count += int(self._add_extra_large_pack(remainder))

        collective_pack_count = self._get_collecting_pack_count(
            small_pack_count, medium_pack_count, large_pack_count,
        )

        return {
            "small_pack_count": small_pack_count,
            "medium_pack_count": medium_pack_count,
            "large_pack_count": large_pack_count,
            "collective_pack_count": collective_pack_count,
        }


class Package:
    def __init__(self):
        self.small_pack_size = 3
        self.medium_pack_size = 6
        self.large_pack_size = 9
        self.min_order_size = 0
        self.max_order_size = 100

    def _get_small_pack_count(self, remainder):
        """Count small size packs needed for shipping order"""
        if 0 < remainder <= self.small_pack_size:
            small_pack_count = 1
        else:
            small_pack_count = 0
        return small_pack_count

    def _get_medium_pack_count(self, remainder):
        """Count medium size packs needed for shipping order"""
        if self.small_pack_size < remainder <= self.medium_pack_size:
            medium_pack_count = 1
        else:
            medium_pack_count = 0
        return medium_pack_count

    def _add_extra_large_pack(self, remainder):
        """Check if additional large pack is needed for the remainder stock"""
        if self.medium_pack_size < remainder <= self.large_pack_size:
            return True
        else:
            return False

    def _get_collecting_pack_count(
        self, small_pack_count, medium_pack_count, large_pack_count
    ):
        """Count collective packs needed for packing product packs"""
        return (small_pack_count + medium_pack_count + large_pack_count) // 2

    def calculate_packages_count(self, order_size):
        """Calculate number of packages required for shipping a given order size"""

        if not self.min_order_size < order_size <= self.max_order_size:
            raise Exception(
                "Order size must be a positive value lower than or equal 100"
            )

        # get number of completely filled large packs
        large_pack_count = order_size // self.large_pack_size

        # add extra pack depending on the reminder
        remainder = order_size - large_pack_count * self.large_pack_size
        small_pack_count = self._get_small_pack_count(remainder)
        medium_pack_count = self._get_medium_pack_count(remainder)
        large_pack_count += int(self._add_extra_large_pack(remainder))

        collective_pack_count = self._get_collecting_pack_count(
            small_pack_count, medium_pack_count, large_pack_count,
        )

        return {
            "small_pack_count": small_pack_count,
            "medium_pack_count": medium_pack_count,
            "large_pack_count": large_pack_count,
            "collective_pack_count": collective_pack_count,
        }


if __name__ == "__main__":
    print("PyCharm")
