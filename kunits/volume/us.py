from ..base import Dimension, StandardTransform, Unit
from decimal import Decimal

us_minim_to_liter = StandardTransform(
    to_standard=Decimal(".000061611519921875"),
    dimension=Dimension.volume
)

_ounce_minim_multiple = Decimal(480)

units = (
    Unit('minim_us', 'minim', 'minims', 'min', Decimal(1), us_minim_to_liter),
    Unit('fluid_dram_us', 'fluid dram', 'fluid drams', 'fl dr', Decimal(60),
                          us_minim_to_liter),
    # note that dash, pinch, and drop are not OFFICIAL,
    # but are widely accepted as 1/8 tsp, 1/16 tsp and 1/96 tsp, respectively
    Unit('drop_us', 'drop', 'drops', 'dr', Decimal(5) / Decimal(6),
                    us_minim_to_liter),
    Unit('pinch_us', 'pinch', 'pinches', 'pn', Decimal(5), us_minim_to_liter),
    Unit('dash_us', 'dash', 'dashes', 'ds', Decimal(10), us_minim_to_liter),
    Unit('teaspoon_us', 'teaspoon', 'teaspoons', 'tsp', Decimal(80),
                        us_minim_to_liter),
    Unit('tablespoon_us', 'tablespoon', 'tablespoons', 'Tbsp', Decimal(240),
                          us_minim_to_liter),
    Unit('fluid_ounce_us', 'fluid ounce', 'fluid ounces', 'fl oz', Decimal(480),
                           us_minim_to_liter),
    Unit('shot_us', 'shot', 'shots', 'jig',
         Decimal('1.5') * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('gill_us', 'gill', 'gills', 'gil', Decimal(4) * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('cup_us', 'cup', 'cups', 'c', Decimal(8) * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('pint_us', 'pint', 'pints', 'pt', Decimal(16) * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('quart_us', 'quart', 'quarts', 'qt',
         Decimal(32) * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('gallon_us', 'gallon', 'gallons', 'gal',
         Decimal(128) * _ounce_minim_multiple,
         us_minim_to_liter),
    Unit('barrel_us', 'barrel', 'barrels', 'bbl',
         Decimal('31.5') * Decimal(128) * _ounce_minim_multiple,
         us_minim_to_liter),
)
