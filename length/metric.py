from ..base import Dimension, generate_metric_units, StandardTransform
from decimal import Decimal
from kunits.base import UnitDict  # noqa

meter_to_meter = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.length,
)

units: UnitDict = {
    unit.name: unit for unit
    in generate_metric_units(name='meter',
                             abbrev='m',
                             standard_transform=meter_to_meter)
}
