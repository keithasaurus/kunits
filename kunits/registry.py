from .base import UnitDict
from .count import count_units
from .length import length_units
from .mass import mass_units
from .time import time_units
from .volume import volume_units
from types import MappingProxyType


def register_all_units():
    unit_registry: UnitDict = {}

    def register_units(units: UnitDict):
        for unit_key, unit in units.items():
            assert unit_key not in unit_registry, f"{unit.name} already registered"

            unit_registry[unit_key] = unit

    for unit_dict in [count_units, length_units, mass_units,
                      volume_units, time_units]:
        register_units(unit_dict)

    return MappingProxyType(unit_registry)


unit_registry: UnitDict = register_all_units()
