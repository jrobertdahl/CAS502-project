import random

# This function takes the amont of CO2 emitted from a jet flight, randomly selects a comparison, and then outputs a string that
# gets addended to the end of the tweet.

def get_emissions_comparison_text(metric_tons_co2_emitted):
  comparisons = ['tree_comparison', 'LA_NY_drive_comparison', 'average_american_emissions_comparison']
  selection = random.choice(comparisons)
  if selection == 'tree_comparison':
    #calculating how many trees are needed to absorb metric_tons_co2_emitted
    
    annual_tree_absorption_mt = 0.02 #from arbor day foundation: a mature tree absorbs 48 lbs CO2 per year = 0.02 mt CO2
    trees_needed = metric_tons_co2_emitted/annual_tree_absorption_mt
    trees_needed = int(trees_needed)
    tree_output = f"It will take {trees_needed} tree{ '' if trees_needed == 1 else 's' } approximately 1 year to remove this CO2 from the atmosphere."
    
    return tree_output
  
  elif selection == 'LA_NY_drive_comparison':
    #one trip from LA to NY emits 2200lbs CO2 = 0.997 mt CO2
    #Assumptions: compact car, using E10 fuel, there are 3,396 km between LA and NY
    
    trip_emissions_mt = 0.997
    trips_needed = metric_tons_co2_emitted/trip_emissions_mt
    trips_needed = int(trips_needed)
    trip_output = f"You would have to drive from LA to NY {trips_needed} time{ '' if trips_needed == 1 else 's' } to emit this same amount."
    
    return trip_output
 
  else:
    
    #an average american emits 16 tons CO2 every year = 14.5 mt
    
    american_emissions_mt = 14.5
    years_needed = metric_tons_co2_emitted/american_emissions_mt
    #If it would take an average American less than 1 year to emit the same amount as the jet trip, we want the output
    # to be in terms of months (ex: 6 months instead of 0.5 years)
    if years_needed <1:
      months_needed = years_needed * 12
      months_needed = int(months_needed)
      months_output = f"It would take an average American {months_needed} month{ '' if months_needed == 1 else 's' } to emit the same amount."
      return months_output
    #If it takes longer than a year for an American to emit the same amount as the jet trip, we want the output to be in terms of years.
    else:
      years_needed = round(years_needed,2)
      years_output = f"It would take an average American {years_needed} year{ '' if years_needed == 1 else 's' } to emit the same amount."
      return years_output
