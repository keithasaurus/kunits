from decimal import Decimal
from enum import Enum
from typing import Dict, Mapping, NamedTuple, Tuple


class Dimension(Enum):
    mass = 10
    volume = 20
    length = 30
    time = 40
    count = 50


class StandardTransform(NamedTuple):
    to_standard: Decimal
    dimension: Dimension


class Unit(NamedTuple):
    id: str
    name: str
    name_plural: str
    abbrev: str
    transform_multiple: Decimal
    standard_transform: StandardTransform


def generate_metric_units(name: str,
                          abbrev: str,
                          standard_transform: StandardTransform
                          ) -> Tuple[Unit, ...]:
    return tuple(
        Unit(
            id=f"{prefix}{name}",
            name=f"{prefix}{name}",
            name_plural=f"{prefix}{name}s",
            abbrev=f"{prefix_abbrev}{abbrev}",
            transform_multiple=multiple,
            standard_transform=standard_transform
        ) for prefix, prefix_abbrev, multiple in (
            ("yotta", "Y", Decimal("1e24")),
            ("zetta", "Z", Decimal("1e21")),
            ("exa", "E", Decimal("1e18")),
            ("peta", "P", Decimal("1e15")),
            ("tera", "T", Decimal("1e12")),
            ("giga", "G", Decimal("1e9")),
            ("mega", "M", Decimal("1e6")),
            ("kilo", "k", Decimal("1e3")),
            ("hecto", "h", Decimal("1e2")),
            ("deca", "da", Decimal("1e1")),
            ("", "", Decimal("1e0")),
            ("deci", "d", Decimal("1e-1")),
            ("centi", "c", Decimal("1e-2")),
            ("milli", "m", Decimal("1e-3")),
            ("micro", "μ", Decimal("1e-6")),
            ("nano", "n", Decimal("1e-9")),
            ("pico", "p", Decimal("1e-12")),
            ("femto", "f", Decimal("1e-15")),
            ("atto", "a", Decimal("1e-18")),
            ("zepto", "z", Decimal("1e-21")),
            ("yocto", "y", Decimal("1e-24")),
        )
    )
