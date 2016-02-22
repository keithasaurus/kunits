from decimal import Decimal

from units.base import MetricTransform, Dimension, Unit

us_minim_to_liter = MetricTransform(
    to_metric=Decimal(".000061611519921875"),
    dimension=Dimension.volume
)


minim = Unit('minim', 'minims', 'min', Decimal(1), us_minim_to_liter)

fluid_dram = Unit('US fluid dram', 'US fluid drams', 'fl dr', Decimal(60), us_minim_to_liter)

teaspoon = Unit('teaspoon', 'teaspoons', 'tsp', Decimal(80), us_minim_to_liter)

tablespoon = Unit('tablespoon', 'tablespoons', 'Tbsp', Decimal(240), us_minim_to_liter)

_ounce_minim_multiple = Decimal(480)
fluid_ounce = Unit('US fluid ounce', 'US fluid ounces', 'fl oz', Decimal(480), us_minim_to_liter)

shot = Unit('US shot', 'US shots', 'jig', Decimal('1.5') * _ounce_minim_multiple, us_minim_to_liter)

gill = Unit('US gill', 'US gills', 'gil', Decimal(4) * _ounce_minim_multiple, us_minim_to_liter)

cup = Unit('US cup', 'US cups', 'cp', Decimal(8) * _ounce_minim_multiple, us_minim_to_liter)

pint = Unit('US pint', 'US pints', 'pt', Decimal(16) * _ounce_minim_multiple, us_minim_to_liter)

quart = Unit('US quart', 'US quarts', 'qt', Decimal(32) * _ounce_minim_multiple, us_minim_to_liter)

gallon = Unit('US gallon', 'US gallons', 'gal', Decimal(128) * _ounce_minim_multiple, us_minim_to_liter)

barrel = Unit('barrel', 'barrels', 'bbl', Decimal('31.5') * Decimal(128) * _ounce_minim_multiple, us_minim_to_liter)

