from decimal import Decimal
from kunits.base import Dimension, StandardTransform, Unit

second_to_second = StandardTransform(
    to_standard=Decimal('1'),
    dimension=Dimension.time
)

_day_multiple = Decimal(60) * Decimal(60) * Decimal(24)

units = (
    Unit("second", "second", "seconds", "sec", Decimal(1), second_to_second),
    Unit("minute", "minute", "minutes", "min", Decimal(60), second_to_second),
    Unit("hour", "hour", "hours", "hr", Decimal(60) * Decimal(60),
         second_to_second),
    Unit("day", "day", "days", "day", _day_multiple, second_to_second),
    Unit("week", "week", "weeks", "wk", _day_multiple * Decimal(7),
         second_to_second),
    Unit("month", "month", "months", "mo", _day_multiple * 30,
         second_to_second),
    Unit("year", "year", "years", "yr", _day_multiple * Decimal(365),
         second_to_second),
)
