from ..base import Dimension, generate_metric_units, StandardTransform
from decimal import Decimal

meter_to_meter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.length,
)

units = generate_metric_units(name='meter',
                              abbrev='m',
                              standard_transform=meter_to_meter)
