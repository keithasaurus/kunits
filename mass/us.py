from decimal import Decimal

from ..base import StandardTransform, Dimension, Unit, UnitDict  # noqa

us_pound_to_gram = StandardTransform(
    to_standard=Decimal('453.59237'),
    dimension=Dimension.volume,
)


units = {  # type: UnitDict
    "dram_us": Unit("dram", "drams", "dr", Decimal('1') / Decimal('16') / Decimal('8'),
                    us_pound_to_gram),
    "ounce_us": Unit("ounce", "ounces", "oz", Decimal('1') / Decimal('16'), us_pound_to_gram),
    "pound_us": Unit("pound", "pounds", "lb", Decimal(1), us_pound_to_gram),
}
