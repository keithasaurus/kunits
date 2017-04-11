from ..base import Dimension, generate_metric_units, StandardTransform
from decimal import Decimal

liter_to_liter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.volume,
)

units = generate_metric_units(name='liter',
                              abbrev='l',
                              standard_transform=liter_to_liter)
