from decimal import Decimal

from kunits.base import UnitDict  # noqa
from ..base import generate_metric_units, StandardTransform, Dimension

liter_to_liter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.volume,
)

units = {  # type: UnitDict
    unit.name: unit for unit
    in generate_metric_units(name='liter', abbrev='l', standard_transform=liter_to_liter)
}
