from ..base import UnitDict  # noqa: F401
from .metric import units as metric_length_units
from .us import units as us_length_units


length_units: UnitDict = {}

for l_units in (metric_length_units, us_length_units):
    length_units.update(l_units)


__all__ = ('length_units', )
