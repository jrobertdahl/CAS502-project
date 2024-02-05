#tree comparison
#eventually all comparison calculations will be in one function
#a mature tree absorbs 48 lbs CO2 per year = 0.02 mt

def tree_comparison(jet_emission):
  annual_tree_absorption_mt = 0.02 #from arbor day foundation
  trees_needed = jet_emission/annual_tree_absorption_mt
  trees_needed = int(trees_needed)
  tree_output = f"It will take {trees_needed} trees approximately 1 year to remove this CO2 from the atmosphere."
  return tree_output
  


#driving from LA to NY comparison, 2200lbs CO2 = 0.997 mt
#Assumptions:
  #Compact Car
  #using E10 fuel
  #3.396 km between LA and NY
def LA_NY_drive_comparison(jet_emission):
  trip_emissions_mt = 0.997
  trips_needed = jet_emission/trip_emissions_mt
  trips_needed = int(trips_needed)
  trip_output = f"You would have to drive from LA to NY {trips_needed} times to emit this same amount."
  return trip_output


#average person emission calculations
# average american emits 16 tons every year = 14.5 mt