from decimal import Decimal

from ..base import Unit, MetricTransform, Dimension

inch_to_meter = MetricTransform(
    to_metric=Decimal('.0254'),
    dimension=Dimension.length,
)

survey_foot_to_meter = MetricTransform(
    to_metric=Decimal(1200)/Decimal(3937),
    dimension=Dimension.length,
)

_fathon_multiple = Decimal(12 * 3 * 2)


units = (
    Unit("point", "points", "p", Decimal(1) / Decimal(6) / Decimal(12), inch_to_meter),
    Unit("pica", "picas", "P/", Decimal(1) / Decimal(6), inch_to_meter),
    Unit("inch", "inches", "in", Decimal(1), inch_to_meter),
    Unit("foot", "feet", "ft", Decimal(12), inch_to_meter),
    Unit("yard", "yards", "yd", Decimal(12 * 3), inch_to_meter),
    Unit("mile", "miles", "mi", Decimal(12 * 5280), inch_to_meter),

    # BEGIN US SURVEY UNITS
    Unit("link", "links", "li", Decimal(33) / Decimal(50), survey_foot_to_meter),
    Unit("survey foot", "survey feet", "ft", Decimal(1), survey_foot_to_meter),
    Unit("rod", "rods", "rd", Decimal(16.5), survey_foot_to_meter),
    Unit("chain", "chains", "ch", Decimal(66), survey_foot_to_meter),
    Unit("furlong", "furlongs", "fur", Decimal(10 * 66), survey_foot_to_meter),
    Unit("survey mile", "survey miles", "mi", Decimal(8 * 10 * 66), survey_foot_to_meter),
    Unit("league", "leagues", "lea", Decimal(3 * 8 * 10 * 66), survey_foot_to_meter),
    # END US SURVEY UNITS

    # BEGIN INTERNATIONAL NAUTICAL
    Unit("fathom", "fathoms", "ftm", _fathon_multiple, inch_to_meter),
    Unit("cable", "cables", "cb", Decimal(120) * _fathon_multiple, inch_to_meter),
    Unit("nautical mile", "nautical miles", "nmi", Decimal("8.439") * Decimal(120) * _fathon_multiple, inch_to_meter),
    # END INTERNATIONAL NAUTICAL
)





