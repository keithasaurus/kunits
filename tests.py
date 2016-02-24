import unittest
from decimal import Decimal
from typing import NamedTuple

from kunits.base import Unit
from kunits.convert import convert_unit
from kunits.registry import unit_registry

ConversionFactor = NamedTuple("ConversionFactor", (
    ("expected_result", Decimal),
    ("from_unit", Unit),
    ("to_unit", Unit),
))


class UnitsTestCase(unittest.TestCase):

    def test_us_volume_units(self):
        test_conversions = (
            ConversionFactor(Decimal(4), unit_registry['us_gallon'], unit_registry['us_quart']),
            ConversionFactor(Decimal(2), unit_registry['us_pint'], unit_registry['us_cup']),
            ConversionFactor(Decimal(4), unit_registry['us_quart'], unit_registry['us_cup']),
            ConversionFactor(Decimal(16), unit_registry['us_cup'], unit_registry['tablespoon']),
            ConversionFactor(Decimal(3), unit_registry['tablespoon'], unit_registry['teaspoon']),
            ConversionFactor(Decimal(80), unit_registry['teaspoon'], unit_registry['minim']),
        )

        for result, from_unit, to_unit in test_conversions:
            self.assertEqual(result, convert_unit(from_unit, to_unit))
