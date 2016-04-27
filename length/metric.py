from decimal import Decimal

from kunits.base import UnitDict  # noqa
from ..base import generate_metric_units, StandardTransform, Dimension

meter_to_meter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.length,
)

units = {  # type: UnitDict
    unit.name: unit for unit
    in generate_metric_units(name='meter', abbrev='m', standard_transform=meter_to_meter)
}
