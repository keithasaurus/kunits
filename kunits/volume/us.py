from ..base import Dimension, StandardTransform, Unit, UnitDict  # noqa
from decimal import Decimal

us_minim_to_liter = StandardTransform(
    to_standard=Decimal(".000061611519921875"),
    dimension=Dimension.volume
)

_ounce_minim_multiple = Decimal(480)

units: UnitDict = {
    'minim_us': Unit('minim', 'minims', 'min', Decimal(1), us_minim_to_liter),
    'fluid_dram_us': Unit('fluid dram', 'fluid drams', 'fl dr', Decimal(60),
                          us_minim_to_liter),
    # note that dash, pinch, and drop are not OFFICIAL,
    # but are widely accepted as 1/8 tsp, 1/16 tsp and 1/96 tsp, respectively
    'drop_us': Unit('drop', 'drops', 'dr', Decimal(5) / Decimal(6),
                    us_minim_to_liter),
    'pinch_us': Unit('pinch', 'pinches', 'pn', Decimal(5), us_minim_to_liter),
    'dash_us': Unit('dash', 'dashes', 'ds', Decimal(10), us_minim_to_liter),
    'teaspoon_us': Unit('teaspoon', 'teaspoons', 'tsp', Decimal(80),
                        us_minim_to_liter),
    'tablespoon_us': Unit('tablespoon', 'tablespoons', 'Tbsp', Decimal(240),
                          us_minim_to_liter),
    'fluid_ounce_us': Unit('fluid ounce', 'fluid ounces', 'fl oz', Decimal(480),
                           us_minim_to_liter),
    'shot_us': Unit('shot', 'shots', 'jig',
                    Decimal('1.5') * _ounce_minim_multiple,
                    us_minim_to_liter),
    'gill_us': Unit('gill', 'gills', 'gil', Decimal(4) * _ounce_minim_multiple,
                    us_minim_to_liter),
    'cup_us': Unit('cup', 'cups', 'c', Decimal(8) * _ounce_minim_multiple,
                   us_minim_to_liter),
    'pint_us': Unit('pint', 'pints', 'pt', Decimal(16) * _ounce_minim_multiple,
                    us_minim_to_liter),
    'quart_us': Unit('quart', 'quarts', 'qt',
                     Decimal(32) * _ounce_minim_multiple,
                     us_minim_to_liter),
    'gallon_us': Unit('gallon', 'gallons', 'gal',
                      Decimal(128) * _ounce_minim_multiple,
                      us_minim_to_liter),
    'barrel_us': Unit('barrel', 'barrels', 'bbl',
                      Decimal('31.5') * Decimal(128) * _ounce_minim_multiple,
                      us_minim_to_liter),
}
