from .base import UnitDict
from .count import count_units
from .length import length_units
from .mass import mass_units
from .volume import volume_units

unit_registry = {}


def register_units(units: UnitDict):
    for unit_key, unit in units.items():
        assert unit_key not in unit_registry, "{} already registered".format(unit.name)

        unit_registry[unit_key] = unit


for unit_dict in (count_units, length_units, mass_units, volume_units):
    register_units(unit_dict)
