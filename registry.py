from typing import Iterable

from .base import Unit
from .length import length_units
from .mass import mass_units
from .volume import volume_units

unit_registry = {}


def register_units(units: Iterable[Unit]):
    for unit in units:
        assert unit.name not in unit_registry, \
            "{} already registered".format(unit.name)

        unit_registry[unit.name.lower().replace(' ', '_')] = unit


for unit_list in (length_units, mass_units, volume_units):
    register_units(unit_list)
