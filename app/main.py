import json
from calculation.comparison import get_emissions_comparison_text
from posting.postToX import post_to_x

name = ""
miles_traveled = 0
tons_co2_emitted = 0
base_post_text = ""
comparison_text = ""

# this bit of functionality pulls in stand-in data until we build out the web scraping and/or API stuff
with open('dataCollection/testData/flightInfo.json') as json_file:
    data = json.load(json_file)
 
    name = data['test_data_1']['name']
    miles_traveled = data['test_data_1']['miles_traveled']

# pull in the comparison text
comparison_text = get_emissions_comparison_text(1000)

# build the full post text
base_post_text = f'TEST - {name} just flew {miles_traveled} miles in their private jet, emitting {tons_co2_emitted} tons of CO₂ into the atmosphere. ' + comparison_text

# post it to x
post_to_x(base_post_text)










