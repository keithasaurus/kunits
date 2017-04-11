from ..base import Dimension, StandardTransform, Unit
from decimal import Decimal

count_to_count = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.count,
)

units = (
    Unit('count', 'count', 'count', 'ct', Decimal(1), count_to_count),
    Unit('dozen', 'dozen', 'dozen', 'doz', Decimal(12), count_to_count)
)
