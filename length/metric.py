from decimal import Decimal

from ..base import generate_metric_units, MetricTransform, Dimension

meter_to_meter = MetricTransform(
    to_metric=Decimal("1"),
    dimension=Dimension.length,
)

units = generate_metric_units(name='meter', abbrev='m', metric_transform=meter_to_meter)

