from .base import UnitDict
from .count import count_units
from .length import length_units
from .mass import mass_units
from .time import time_units
from .volume import volume_units
from frozendict import frozendict


def register_all_units():
    unit_registry = {}

    def register_units(units: UnitDict):
        for unit_key, unit in units.items():
            assert unit_key not in unit_registry, "{} already registered".format(
                unit.name)

            unit_registry[unit_key] = unit

    for unit_dict in [count_units, length_units, mass_units,
                      volume_units, time_units]:
        register_units(unit_dict)

    return frozendict(unit_registry)

unit_registry = register_all_units()  # type: UnitDict
