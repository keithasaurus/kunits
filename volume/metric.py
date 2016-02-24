from decimal import Decimal

from ..base import generate_metric_units, MetricTransform, Dimension

liter_to_liter = MetricTransform(
    to_metric=Decimal("1"),
    dimension=Dimension.volume,
)

units = generate_metric_units(name='liter', abbrev='l', metric_transform=liter_to_liter)

