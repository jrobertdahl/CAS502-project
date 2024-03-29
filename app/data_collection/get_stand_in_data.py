import sys,json
from random import randrange

# this bit of functionality pulls in stand-in data until we build out the web scraping and/or API stuff

def select_data_value(arg_list):
    if (len(arg_list) > 1):
        # this should be refactored obviously
        if arg_list[1] in ['test_data_1','test_data_2','test_data_3','test_data_4']:
            return arg_list[1]
        else:
            print("Please pass a valid test data selection.")
            if (len(arg_list) < 3 and 'test' not in arg_list):
                sys.exit()
    else:
        return "test_data_" + str(randrange(1,4)) 

def get_stand_in_data(test_data_value):

    with open('data_collection/test_data/flight_info.json') as json_file:
        data = json.load(json_file)
 
        name = data[test_data_value]['name']
        km_traveled = data[test_data_value]['km_traveled']

        return name, km_traveled