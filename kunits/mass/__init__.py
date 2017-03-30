from ..base import UnitDict  # noqa: F401
from .metric import units as metric_mass_units
from .us import units as us_mass_units

mass_units: UnitDict = {}
for m_units in (metric_mass_units, us_mass_units):
    mass_units.update(m_units)

__all__ = ('mass_units', )
