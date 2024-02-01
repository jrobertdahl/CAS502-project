import json
from posting.postToX import testPostFunction

name = ""
milesTraveled = 0

#this bit of functionality pulls in stand-in data until we build out the web scraping and/or API stuff
with open('testData/flightInfo.json') as json_file:
    data = json.load(json_file)
 
    name = data['name']
    milesTraveled = data['milesTraveled']

testPostFunction(name, milesTraveled)

