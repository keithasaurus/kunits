from decimal import Decimal

from .base import Unit


def convert_unit(from_unit: Unit, to_unit: Unit) -> Decimal:
    assert from_unit.standard_transform.dimension == to_unit.standard_transform.dimension

    if from_unit.standard_transform == to_unit.standard_transform:
        return from_unit.transform_multiple / to_unit.transform_multiple
    else:
        return (from_unit.transform_multiple * from_unit.standard_transform.to_standard) / \
               (to_unit.transform_multiple * to_unit.standard_transform.to_standard)

