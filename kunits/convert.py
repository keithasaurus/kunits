from .types import Unit
from decimal import Decimal


def convert_unit(from_: Unit, to: Unit) -> Decimal:
    assert from_.dimension == to.dimension
    return from_.multiple / to.multiple
