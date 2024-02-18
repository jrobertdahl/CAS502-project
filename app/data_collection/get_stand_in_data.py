import json

# this bit of functionality pulls in stand-in data until we build out the web scraping and/or API stuff

def get_stand_in_data(test_data_value):

    with open('data_collection/test_data/flight_info.json') as json_file:
        data = json.load(json_file)
 
        name = data[test_data_value]['name']
        km_traveled = data[test_data_value]['km_traveled']

        return name, km_traveled