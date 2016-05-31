from decimal import Decimal
from kunits.base import Unit
from kunits.convert import convert_unit
from kunits.registry import unit_registry
from typing import NamedTuple

import unittest

ConversionFactor = NamedTuple("ConversionFactor", (
    ("expected_result", Decimal),
    ("from_unit", Unit),
    ("to_unit", Unit),
))


class UnitsTestCase(unittest.TestCase):

    def test_us_volume_units(self):
        test_conversions = (
            ConversionFactor(Decimal(4), unit_registry['gallon_us'], unit_registry['quart_us']),
            ConversionFactor(Decimal(2), unit_registry['pint_us'], unit_registry['cup_us']),
            ConversionFactor(Decimal(4), unit_registry['quart_us'], unit_registry['cup_us']),
            ConversionFactor(Decimal(16), unit_registry['cup_us'], unit_registry['tablespoon_us']),
            ConversionFactor(Decimal(3), unit_registry['tablespoon_us'],
                             unit_registry['teaspoon_us']),
            ConversionFactor(Decimal(80), unit_registry['teaspoon_us'], unit_registry['minim_us']),
        )

        for result, from_unit, to_unit in test_conversions:
            self.assertEqual(result, convert_unit(from_unit, to_unit))
