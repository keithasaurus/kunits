from ..base import UnitDict  # noqa: F401
from .metric import units as metric_volume_units
from .us import units as us_volume_units


volume_units: UnitDict = {}

for vol_units in (metric_volume_units, us_volume_units):
    volume_units.update(vol_units)


__all__ = ('volume_units', )
