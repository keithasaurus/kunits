from decimal import Decimal
from enum import Enum
from typing import NamedTuple, FrozenSet, Tuple

from collections import OrderedDict


class UnitSystem(Enum):
    metric = 10
    imperial = 20
    us = 30


class Dimension(Enum):
    mass = 10
    volume = 20
    length = 30


class TransformTarget(Enum):
    grams = 10
    meters = 20
    inch = 30
    liters = 40
    minim_us = 50
    pound_weight = 60


Transform = NamedTuple("TransformFactor", (
    ("target", TransformTarget),
    ("divisor", Decimal),
))


Unit = NamedTuple("Unit", (
    ("name", str),
    ("name_plural", str),
    ("abbrev", str),
    ("systems", FrozenSet[UnitSystem]),
    ("dimension", Dimension),
    ("transforms", Transform),
))

MetricMultiple = NamedTuple("MetricMultiple", (("prefix", str), ("abbrev_prefix", str), ("divisor", Decimal)))
metric_multiples = (
    MetricMultiple("yotta", "Y",  Decimal("1e24")),
    MetricMultiple("zetta", "Z",  Decimal("1e21")),
    MetricMultiple("exa", "E",  Decimal("1e18")),
    MetricMultiple("peta", "P",  Decimal("1e15")),
    MetricMultiple("tera", "T",  Decimal("1e12")),
    MetricMultiple("giga", "G",  Decimal("1e9")),
    MetricMultiple("mega", "M",  Decimal("1e6")),
    MetricMultiple("kilo", "k",  Decimal("1e3")),
    MetricMultiple("hecto", "h", Decimal("1e2")),
    MetricMultiple("deca", "da", Decimal("1e1")),
    MetricMultiple("",     "",   Decimal("1e0")),
    MetricMultiple("deci", "d",  Decimal("1e-1")),
    MetricMultiple("centi", "c", Decimal("1e-2")),
    MetricMultiple("milli", "m", Decimal("1e-3")),
    MetricMultiple("micro", "μ", Decimal("1e-6")),
    MetricMultiple("nano", "n",  Decimal("1e-9")),
    MetricMultiple("pico", "p",  Decimal("1e-12")),
    MetricMultiple("femto", "f", Decimal("1e-15")),
    MetricMultiple("atto", "a", Decimal("1e-18")),
    MetricMultiple("zepto", "z", Decimal("1e-21")),
    MetricMultiple("yocto", "y", Decimal("1e-24")),
)


all_units = []

# convenience
metric_system_only = frozenset([UnitSystem.metric])
imperial_system_only = frozenset([UnitSystem.imperial])
us_system_only = frozenset([UnitSystem.us])
imperial_and_us_systems = frozenset([UnitSystem.imperial, UnitSystem.us])

for prefix, abbrev, divisor in metric_multiples:
    all_units.extend([
        Unit(
            name="{}gram".format(prefix),
            name_plural="{}grams".format(prefix),
            abbrev="{}g".format(abbrev),
            systems=metric_system_only,
            dimension=Dimension.mass,
            transform=(Transform(
                target=TransformTarget.grams,
                divisor=divisor
            ),)
        ),
        Unit(
            name="{}liter".format(prefix),
            name_plural="{}liters".format(prefix),
            abbrev="{}l".format(abbrev),
            systems=metric_system_only,
            dimension=Dimension.volume,
            transform=(Transform(
                target=TransformTarget.liters,
                divisor=divisor
            ),)
        ),
        Unit(
            name="{}meter".format(prefix),
            name_plural="{}meters".format(prefix),
            abbrev="{}m".format(abbrev),
            systems=metric_system_only,
            dimension=Dimension.length,
            transform=(Transform(
                target=TransformTarget.meters,
                divisor=divisor
            ),)
        )
    ])

all_units.extend([
    Unit(
        name="pound",
        name_plural="pounds",
        abbrev="lb",
        systems=frozenset([UnitSystem.imperial, UnitSystem.us]),
        dimension=Dimension.mass,
        transform=Transform(
            target=TransformTarget.grams,
            divisor=Decimal("453.59237"),
        ),
    ),
    Unit(
        name="ounce",
        name_plural="ounces",
        abbrev="oz",
        systems=frozenset([UnitSystem.imperial, UnitSystem.us]),
        dimension=Dimension.mass,
        transform=Transform(
            target=TransformTarget.pound,
            divisor=Decimal('1') / Decimal('16')
        )
    ),
    Unit(
        name="dram",
        name_plural="drams",
        abbrev="dr",
        systems=frozenset([UnitSystem.imperial, UnitSystem.us]),
        dimension=Dimension.mass,
        transform=Transform(
            target=TransformTarget.pound,
            divisor=Decimal('1') / Decimal('16') / Decimal('16')
        )
    ),
    Unit(
        name="stone",
        name_plural="stone",
        abbrev="st",
        systems=imperial_system_only,
        dimension=Dimension.mass,
        transform=Transform(
            target=TransformTarget.grams,
            divisor=Decimal("6350.29318"),
        ),
    ),
    Unit(
        name="ton",
        name_plural="tons",
        abbrev="t",
        systems=imperial_system_only,
        dimension=Dimension.mass,
        transform=Transform(
            target=TransformTarget.grams,
            divisor=Decimal("1016046.9088"),
        ),
    ),

    # US VOLUMES
    Unit(
        name="minim",
        name_plural="minims",
        abbrev="min",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal("1"),
        ),
    ),

    Unit(
        name="fluid dram",
        name_plural="fluid drams",
        abbrev="fl dr",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal("60"),
        )
    ),

    Unit(
        name="teaspoon",
        name_plural="teaspoons",
        abbrev="tsp",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(80),
        )
    ),
    Unit(
        name="tablespoon",
        name_plural="tablespoons",
        abbrev="Tbsp",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(3 * 80),
        )
    ),
    Unit(
        name="fluid ounce",
        name_plural="fluid ounces",
        abbrev="fl oz",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(2 * 3 * 80),
        )
    ),
    Unit(
        name="shot",
        name_plural="shots",
        abbrev="jig",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(3 * 3 * 80),
        )
    ),
    Unit(
        name="gill",
        name_plural="gills",
        abbrev="gi",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(4 * 2 * 3 * 80),
        )
    ),
    Unit(
        name="cup",
        name_plural="cup",
        abbrev="cp",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(2 * 4 * 2 * 3 * 80),
        )
    ),
    Unit(
        name="pint",
        name_plural="pints",
        abbrev="pt",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(2 * 2 * 4 * 2 * 3 * 80),
        )
    ),
    Unit(
        name="quart",
        name_plural="quarts",
        abbrev="qt",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(2 * 2 * 2 * 4 * 2 * 3 * 80),
        )
    ),
    Unit(
        name="gallon",
        name_plural="gallons",
        abbrev="gal",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.minim_us,
            divisor=Decimal(4 * 2 * 2 * 2 * 4 * 2 * 3 * 80),
        )
    ),
    Unit(
        name="barrel",
        name_plural="barrels",
        abbrev="bbl",
        systems=us_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal("119.240471196")
        )
    ),

    # IMPERIAL VOLUMES
    Unit(
        name="fluid ounce",
        name_plural="fluid ounces",
        abbrev="fl oz",
        systems=imperial_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal(".0284130625")
        )
    ),
    Unit(
        name="gill",
        name_plural="gills",
        abbrev="gi",
        systems=imperial_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal(".1420653125")
        )
    ),
    Unit(
        name="pint",  # british pint
        name_plural="pints",
        abbrev="pt",
        systems=imperial_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal(".56826125")
        )
    ),
    Unit(
        name="quart",
        name_plural="quarts",
        abbrev="qt",
        systems=imperial_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal("1.1365225")
        )
    ),
    Unit(
        name="gallon",
        name_plural="gallons",
        abbrev="gal",
        systems=imperial_system_only,
        dimension=Dimension.volume,
        transform=Transform(
            target=TransformTarget.liters,
            divisor=Decimal("4.54609")
        )
    ),

    # Non-metric LENGTHS
    Unit(
        name="inch",
        name_plural="inches",
        abbrev="in",
        systems=imperial_and_us_systems,
        dimension=Dimension.length,
        transform=Transform(
            target=TransformTarget.meters,
            divisor=Decimal(".00254")
        )
    ),
    Unit(
        name="pica",
        name_plural="picas",
        abbrev="P/",  # TODO: find way to express in unicode
        system=imperial_and_us_systems,
        dimension=Dimension.length,
        transform=Transform(
            target=TransformTarget.inch,
            divisor=Decimal(1) / Decimal(6)
        )
    )
])


metric_units = OrderedDict()
imperial_units = OrderedDict()
us_units = OrderedDict()
for unit in all_units:
    for collection, system in (
        (metric_units, UnitSystem.metric),
        (imperial_units, UnitSystem.imperial),
        (us_units, UnitSystem.us),
    ):
        if system in unit.systems:
            assert unit.name not in collection
            collection[unit.name] = unit


class TransformTargetError(Exception):
    pass


def get_conversion_factor(source: Unit, dest: Unit):
    for dest_transform in dest.transforms:
        if source_transform.target == dest_transform.target:
            return source_transform.divisor / dest_transform.divisor
    raise TransformTargetError("No common transform target found.")


Quantity = NamedTuple("Quantity", (
    ("number", Decimal),
    ("unit", Unit),
))


if __name__ == "__main__":
    qty = Quantity(
        number=Decimal(1),
        unit=metric_units['liter']
    )

    print(len(all_units))

    print(qty.number * get_conversion_factor(qty.unit, metric_units['zettaliter']))
    print(qty.number * get_conversion_factor(qty.unit, us_units['teaspoon']))
    print(qty.number * get_conversion_factor(qty.unit, us_units['minim']))
    print(qty.number * get_conversion_factor(qty.unit, us_units['cup']))
