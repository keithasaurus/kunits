from decimal import Decimal
from kunits.base import Dimension, StandardTransform, Unit, UnitDict

second_to_second = StandardTransform(
    to_standard=Decimal('1'),
    dimension=Dimension.time
)

_day_multiple = Decimal(60) * Decimal(60) * Decimal(24)

units: UnitDict = {
    "second": Unit("second", "seconds", "sec", Decimal(1), second_to_second),
    "minute": Unit("minute", "minutes", "min", Decimal(60), second_to_second),
    "hour": Unit("hour", "hours", "hr", Decimal(60) * Decimal(60),
                 second_to_second),
    "day": Unit("day", "days", "day", _day_multiple, second_to_second),
    "week": Unit("week", "weeks", "wk", _day_multiple * Decimal(7),
                 second_to_second),
    "month": Unit("month", "months", "mo", _day_multiple * 30,
                  second_to_second),
    "year": Unit("year", "years", "yr", _day_multiple * Decimal(365),
                 second_to_second),
}
