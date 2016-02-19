from units.length.transforms import meter_to_meter
from ..base import generate_metric_units


for unit in generate_metric_units(name='meter', abbrev='m', metric_transform=meter_to_meter):
    globals()[unit.name] = unit

