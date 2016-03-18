from decimal import Decimal

from kunits.base import UnitDict
from ..base import generate_metric_units, StandardTransform, Dimension

gram_to_gram = StandardTransform(
    to_standard=Decimal("1"),
    dimension=Dimension.mass,
)

units = {  # type: UnitDict
    unit.name: unit for unit in generate_metric_units(name='gram', abbrev='g', standard_transform=gram_to_gram)
}
