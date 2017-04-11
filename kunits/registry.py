from .count import count_units
from .length import length_units
from .mass import mass_units
from .time import time_units
from .volume import volume_units
from kunits.base import Unit
from types import MappingProxyType
from typing import Dict, Mapping, Tuple


def register_all_units():
    _unit_registry: Dict[str, Unit] = {}

    def register_units(units: Tuple[Unit]):
        for unit in units:
            assert unit.id not in _unit_registry, f"{unit.id} already registered"

            _unit_registry[unit.id] = unit

    for unit_dict in [count_units, length_units, mass_units,
                      volume_units, time_units]:
        register_units(unit_dict)

    return MappingProxyType(_unit_registry)


unit_registry: Mapping[str, Unit] = register_all_units()
