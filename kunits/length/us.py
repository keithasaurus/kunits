from ..base import Dimension, StandardTransform, Unit
from decimal import Decimal

inch_to_meter = StandardTransform(
    to_standard=Decimal('.0254'),
    dimension=Dimension.length,
)

survey_foot_to_meter = StandardTransform(
    to_standard=Decimal(1200) / Decimal(3937),
    dimension=Dimension.length,
)

_fathom_multiple = Decimal(12 * 3 * 2)

units = (
    Unit("point_us",
         "point",
         "points",
         "p",
         Decimal(1) / Decimal(6) / Decimal(12),
         inch_to_meter),
    Unit("pica_us",
         "pica",
         "picas",
         "P/",
         Decimal(1) / Decimal(6),
         inch_to_meter),
    Unit("inch_us",
         "inch",
         "inches",
         "in",
         Decimal(1),
         inch_to_meter),
    Unit("foot_us",
         "foot",
         "feet",
         "ft",
         Decimal(12),
         inch_to_meter),
    Unit('yard_us', "yard", "yards", "yd", Decimal(12 * 3), inch_to_meter),
    Unit('mile_us', "mile", "miles", "mi", Decimal(12 * 5280), inch_to_meter),

    # BEGIN US SURVEY UNITS
    Unit('link_us', "link", "links", "li", Decimal(33) / Decimal(50),
         survey_foot_to_meter),
    Unit('survey_foot_us', "survey foot", "survey feet", "ft", Decimal(1),
         survey_foot_to_meter),
    Unit('rod_us', "rod", "rods", "rd", Decimal(16.5), survey_foot_to_meter),
    Unit('chain_us', "chain", "chains", "ch", Decimal(66),
         survey_foot_to_meter),
    Unit('furlong_us', "furlong", "furlongs", "fur", Decimal(10 * 66),
         survey_foot_to_meter),
    Unit('survey_mile_us',
         "survey mile",
         "survey miles",
         "mi",
         Decimal(8 * 10 * 66),
         survey_foot_to_meter),
    Unit('league_us', "league", "leagues", "lea", Decimal(3 * 8 * 10 * 66),
         survey_foot_to_meter),
    # END US SURVEY UNITS

    # BEGIN INTERNATIONAL NAUTICAL
    Unit('fathom_us', "fathom", "fathoms", "ftm", _fathom_multiple, inch_to_meter),
    Unit('cable_us', "cable", "cables", "cb", Decimal(120) * _fathom_multiple,
         inch_to_meter),
    Unit('nautical_mile_us', "nautical mile", "nautical miles", "nmi",
         Decimal("8.439") * Decimal(120) * _fathom_multiple,
         inch_to_meter),
    # END INTERNATIONAL NAUTICAL
)
