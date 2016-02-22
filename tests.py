import unittest
from decimal import Decimal
from typing import NamedTuple

from units.convert import convert_unit
from units.base import Unit
from units.volume import us as volume_us

ConversionFactor = NamedTuple("ConversionFactor", (
    ("expected_result", Decimal),
    ("from_unit", Unit),
    ("to_unit", Unit),
))


class UnitsTestCase(unittest.TestCase):

    def test_us_volume_units(self):
        test_conversions = (
            ConversionFactor(Decimal(4), volume_us.gallon, volume_us.quart),
            ConversionFactor(Decimal(2), volume_us.pint, volume_us.cup),
            ConversionFactor(Decimal(4), volume_us.quart, volume_us.cup),
            ConversionFactor(Decimal(16), volume_us.cup, volume_us.tablespoon),
            ConversionFactor(Decimal(3), volume_us.tablespoon, volume_us.teaspoon),
            ConversionFactor(Decimal(80), volume_us.teaspoon, volume_us.minim),
        )

        for result, from_unit, to_unit in test_conversions:
            self.assertEqual(result, convert_unit(from_unit, to_unit))
