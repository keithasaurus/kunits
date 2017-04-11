from ..base import Dimension, StandardTransform, Unit
from decimal import Decimal

us_pound_to_gram = StandardTransform(
    to_standard=Decimal('453.59237'),
    dimension=Dimension.mass,
)

units = (
    Unit("dram_us", "dram", "drams", "dr",
         Decimal('1') / Decimal('16') / Decimal('8'),
         us_pound_to_gram),
    Unit("ounce_us", "ounce", "ounces", "oz", Decimal('1') / Decimal('16'),
                     us_pound_to_gram),
    Unit("pound_us", "pound", "pounds", "lb", Decimal(1), us_pound_to_gram),
)
