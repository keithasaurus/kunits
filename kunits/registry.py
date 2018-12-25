from decimal import Decimal
from kunits.types import Dimension, Unit
from types import SimpleNamespace
from typing import Dict, List

import csv
import os

units_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'units.csv')

str_to_dimension: Dict[str, Dimension] = {
    s.name: s for s in Dimension
}


with open(units_csv) as f:
    reader = csv.reader(f)
    units_prelim: List[Unit] = []
    for id, name, name_plural, abbrev, multiple, dimension in reader:
        units_prelim.append(Unit(id=id,
                                 name=name,
                                 name_plural=name_plural,
                                 abbrev=abbrev,
                                 multiple=Decimal(multiple),
                                 dimension=str_to_dimension[dimension]))

units = SimpleNamespace(**{
    unit.id: unit for unit in units_prelim
})

assert len(vars(units)) == len(units_prelim)
