from ..base import Dimension, generate_metric_units, StandardTransform
from decimal import Decimal

gram_to_gram = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.mass,
)

units = generate_metric_units(name='gram',
                              abbrev='g',
                              standard_transform=gram_to_gram)
