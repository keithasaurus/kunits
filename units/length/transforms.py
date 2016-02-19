from decimal import Decimal

from ..base import MetricTransform, Dimension

inch_to_meter = MetricTransform(
    to_metric=Decimal('.0254'),
    dimension=Dimension.length,
)

survey_foot_to_meter = MetricTransform(
    to_metric=Decimal(1200)/Decimal(3937),
    dimension=Dimension.length,
)


meter_to_meter = MetricTransform(
    to_metric=Decimal("1"),
    dimension=Dimension.length,
)
