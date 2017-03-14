from ..base import Dimension, StandardTransform, Unit
from decimal import Decimal
from kunits.base import UnitDict  # noqa

count_to_count = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.count,
)

units: UnitDict = {
    'count': Unit('count', 'count', 'ct', Decimal(1), count_to_count),
    'dozen': Unit('dozen', 'dozen', 'doz', Decimal(12), count_to_count)
}
