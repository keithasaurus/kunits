from decimal import Decimal
from typing import NamedTuple

from django.test import TestCase

from .units import get_conversion_factor, Unit
from .units import us_units

ConversionFactor = NamedTuple("ConversionFactor", (
    ("expected_result", Decimal),
    ("from_unit", Unit),
    ("to_unit", Unit),
))


class UnitsTestCase(TestCase):

    def test_us_volume_units(self):
        test_conversions = (
            ConversionFactor(Decimal(4), us_units['gallon'], us_units['quart']),
            ConversionFactor(Decimal(2), us_units['pint'], us_units['cup']),
            ConversionFactor(Decimal(4), us_units['quart'], us_units['cup']),
            ConversionFactor(Decimal(16), us_units['cup'], us_units['tablespoon']),
            ConversionFactor(Decimal(3), us_units['tablespoon'], us_units['teaspoon']),
            ConversionFactor(Decimal(80), us_units['teaspoon'], us_units['minim']),
        )

        for result, from_unit, to_unit in test_conversions:
            self.assertEqual(result, get_conversion_factor(from_unit, to_unit))
