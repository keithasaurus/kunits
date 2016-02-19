from units.convert import convert_unit


from units.length.us import foot, yard, league, survey_mile, chain, furlong, link
from units.length.metric import kilometer, meter


print(convert_unit(kilometer, yard))

print(convert_unit(yard, kilometer))

print(convert_unit(foot, yard))

print(convert_unit(yard, meter))

print(convert_unit(meter, yard))

print(convert_unit(survey_mile, kilometer))

print(convert_unit(league, kilometer))

print(convert_unit(chain, meter))

print(convert_unit(furlong, meter))

print(convert_unit(link, meter))