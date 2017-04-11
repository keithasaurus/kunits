from .count import count_units
from .length import length_units
from .mass import mass_units
from .time import time_units
from .volume import volume_units
from kunits.base import Unit
from types import SimpleNamespace
from typing import Dict, List, Tuple


def _register_units(unit_groups: List[Tuple[Unit, ...]]) -> Dict[str, Unit]:
    unit_registry: Dict[str, Unit] = {}

    def register_units(units: Tuple[Unit, ...]):
        for unit in units:
            assert unit.id not in unit_registry, f"{unit.id} already registered"

            unit_registry[unit.id] = unit

    for units in unit_groups:
        register_units(units)

    return unit_registry


units = SimpleNamespace(**_register_units([
    count_units,
    length_units,
    mass_units,
    volume_units,
    time_units
]))
