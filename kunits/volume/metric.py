from ..base import Dimension, generate_metric_units, StandardTransform
from decimal import Decimal
from kunits.base import UnitDict  # noqa

liter_to_liter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.volume,
)

units: UnitDict = {
    unit.name: unit for unit
    in generate_metric_units(name='liter',
                             abbrev='l',
                             standard_transform=liter_to_liter)
}
