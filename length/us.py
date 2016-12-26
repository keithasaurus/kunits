from ..base import Dimension, StandardTransform, Unit, UnitDict  # noqa
from decimal import Decimal

inch_to_meter = StandardTransform(
    to_standard=Decimal('.0254'),
    dimension=Dimension.length,
)

survey_foot_to_meter = StandardTransform(
    to_standard=Decimal(1200) / Decimal(3937),
    dimension=Dimension.length,
)

_fathon_multiple = Decimal(12 * 3 * 2)

units: UnitDict = {
    'point_us': Unit("point", "points", "p",
                     Decimal(1) / Decimal(6) / Decimal(12), inch_to_meter),
    'pica_us': Unit("pica", "picas", "P/", Decimal(1) / Decimal(6),
                    inch_to_meter),
    'inch_us': Unit("inch", "inches", "in", Decimal(1), inch_to_meter),
    'foot_us': Unit("foot", "feet", "ft", Decimal(12), inch_to_meter),
    'yard_us': Unit("yard", "yards", "yd", Decimal(12 * 3), inch_to_meter),
    'mile_us': Unit("mile", "miles", "mi", Decimal(12 * 5280), inch_to_meter),

    # BEGIN US SURVEY UNITS
    'link_us': Unit("link", "links", "li", Decimal(33) / Decimal(50),
                    survey_foot_to_meter),
    'survey_foot_us': Unit("survey foot", "survey feet", "ft", Decimal(1),
                           survey_foot_to_meter),
    'rod_us': Unit("rod", "rods", "rd", Decimal(16.5), survey_foot_to_meter),
    'chain_us': Unit("chain", "chains", "ch", Decimal(66),
                     survey_foot_to_meter),
    'furlong_us': Unit("furlong", "furlongs", "fur", Decimal(10 * 66),
                       survey_foot_to_meter),
    'survey_mile_us': Unit("survey mile", "survey miles", "mi",
                           Decimal(8 * 10 * 66),
                           survey_foot_to_meter),
    'league_us': Unit("league", "leagues", "lea", Decimal(3 * 8 * 10 * 66),
                      survey_foot_to_meter),
    # END US SURVEY UNITS

    # BEGIN INTERNATIONAL NAUTICAL
    'fathom_us': Unit("fathom", "fathoms", "ftm", _fathon_multiple,
                      inch_to_meter),
    'cable_us': Unit("cable", "cables", "cb", Decimal(120) * _fathon_multiple,
                     inch_to_meter),
    'nautical_mile_us': Unit("nautical mile", "nautical miles", "nmi",
                             Decimal("8.439") * Decimal(120) * _fathon_multiple,
                             inch_to_meter),
    # END INTERNATIONAL NAUTICAL
}
