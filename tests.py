from decimal import Decimal
from kunits import units
from kunits.base import Unit
from kunits.convert import convert_unit
from typing import NamedTuple

import unittest


class ConversionFactor(NamedTuple):
    expected_result: Decimal
    from_unit: Unit
    to_unit: Unit


class UnitsTestCase(unittest.TestCase):
    def test_us_volume_units(self):
        test_conversions = (
            ConversionFactor(Decimal(4), units.gallon_us,
                             units.quart_us),
            ConversionFactor(Decimal(2), units.pint_us,
                             units.cup_us),
            ConversionFactor(Decimal(4), units.quart_us,
                             units.cup_us),
            ConversionFactor(Decimal(16), units.cup_us,
                             units.tablespoon_us),
            ConversionFactor(Decimal(3), units.tablespoon_us,
                             units.teaspoon_us),
            ConversionFactor(Decimal(80), units.teaspoon_us,
                             units.minim_us),
        )

        for result, from_unit, to_unit in test_conversions:
            self.assertEqual(result, convert_unit(from_unit, to_unit))
