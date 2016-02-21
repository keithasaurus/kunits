from decimal import Decimal

from ..base import generate_metric_units, MetricTransform, Dimension

gram_to_gram = MetricTransform(
    to_metric=Decimal("1"),
    dimension=Dimension.mass,
)

for unit in generate_metric_units(name='gram', abbrev='g', metric_transform=gram_to_gram):
    globals()[unit.name] = unit

