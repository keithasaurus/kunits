from .base import Unit
from decimal import Decimal


def convert_unit(from_: Unit, to: Unit) -> Decimal:
    assert from_.standard_transform.dimension == to.standard_transform.dimension

    if from_.standard_transform == to.standard_transform:
        return from_.transform_multiple / to.transform_multiple
    else:
        return (
            from_.transform_multiple *
            from_.standard_transform.to_standard
        ) / (
            to.transform_multiple *
            to.standard_transform.to_standard
        )
