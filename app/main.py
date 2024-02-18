from calculation.comparison import get_emissions_comparison_text
from data_collection.get_stand_in_data import get_stand_in_data,select_data_value
from posting.postToX import post_to_x

name = ""
km_traveled = 0
metric_tons_co2_emitted = 0
comparison_text = ""
post_text = ""

# returns either the argument passed to the script or a random selection from the four items in flight_info
temp_data_value = select_data_value()

# pull in the individual's name and the distance of a recent flight - stand in data for now
name,km_traveled = get_stand_in_data(temp_data_value)

# pull in the comparison text
comparison_text = get_emissions_comparison_text(1000)

# build the full post text
post_text = f'TEST - {name} just flew {km_traveled} km in their private jet, emitting {metric_tons_co2_emitted} metric tons of CO₂ into the atmosphere. ' + comparison_text

# post it to x
post_to_x(post_text)









