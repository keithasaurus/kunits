from decimal import Decimal

from kunits.base import MetricTransform, Dimension, Unit

us_pound_to_gram = MetricTransform(
    to_metric=Decimal('453.59237'),
    dimension=Dimension.volume,
)

dram = Unit("dram", "drams", "dr", Decimal('1') / Decimal('16') / Decimal('8'), us_pound_to_gram)

ounce = Unit("ounce", "ounces", "oz", Decimal('1') / Decimal('16'), us_pound_to_gram)

pound = Unit("pound", "pounds", "lb", Decimal(1), us_pound_to_gram)

