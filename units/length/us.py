from decimal import Decimal

from ..base import Unit, MetricTransform, Dimension

inch_to_meter = MetricTransform(
    to_metric=Decimal('.0254'),
    dimension=Dimension.length,
)

point = Unit("point", "points", "p", Decimal(1) / Decimal(6) / Decimal(12), inch_to_meter)

pica = Unit("pica", "picas", "P/", Decimal(1) / Decimal(6), inch_to_meter)

inch = Unit("inch", "inches", "in", Decimal(1), inch_to_meter)

foot = Unit("foot", "feet", "ft", Decimal(12), inch_to_meter)

yard = Unit("yard", "yards", "yd", Decimal(12 * 3), inch_to_meter)

mile = Unit("mile", "miles", "mi", Decimal(12 * 5280), inch_to_meter)


survey_foot_to_meter = MetricTransform(
    to_metric=Decimal(1200)/Decimal(3937),
    dimension=Dimension.length,
)

# BEGIN US SURVEY UNITS
link = Unit("link", "links", "li", Decimal(33) / Decimal(50), survey_foot_to_meter)

# the meters transform is not a typo
survey_foot = Unit("survey foot", "survey feet", "ft", Decimal(1), survey_foot_to_meter)

rod = Unit("rod", "rods", "rd", Decimal(16.5), survey_foot_to_meter)

chain = Unit("chain", "chains", "ch", Decimal(66), survey_foot_to_meter)

furlong = Unit("furlong", "furlongs", "fur", Decimal(10 * 66), survey_foot_to_meter)

survey_mile = Unit("survey mile", "survey miles", "mi", Decimal(8 * 10 * 66), survey_foot_to_meter)

league = Unit("league", "leagues", "lea", Decimal(3 * 8 * 10 * 66), survey_foot_to_meter)

# END US SURVEY UNITS

# BEGIN INTERNATIONAL NAUTICAL
_fathon_multiple = Decimal(12 * 3 * 2)
fathom = Unit("fathom", "fathoms", "ftm", _fathon_multiple, inch_to_meter)

cable = Unit("cable", "cables", "cb", Decimal(120) * _fathon_multiple, inch_to_meter)

nautical_mile = Unit("nautical mile", "nautical miles", "nmi", Decimal("8.439") * Decimal(120) * _fathon_multiple, inch_to_meter)

# END INTERNATIONAL NAUTICAL
