import random

def get_emissions_comparison_text(jet_emission):
  comparisons = ['tree_comparison', 'LA_NY_drive_comparison', 'average_american_emissions_comparison']
  selection = random.choice(comparisons)
  if selection == 'tree_comparison':
    #calculating how many trees are needed to absorb jet_emission
    #from arbor day foundation: a mature tree absorbs 48 lbs CO2 per year = 0.02 mt CO2
   
    annual_tree_absorption_mt = 0.02
    trees_needed = jet_emission/annual_tree_absorption_mt
    trees_needed = int(trees_needed)
    tree_output = f"It will take {trees_needed} tree{ "" if trees_needed == 1 else "s" } approximately 1 year to remove this CO2 from the atmosphere."
    
    return tree_output
  
  elif selection == 'LA_NY_drive_comparison':
    #driving from LA to NY comparison, 2200lbs CO2 = 0.997 mt
    #Assumptions: compact car, using E10 fuel, there are 3,396 km between LA and NY
    
    trip_emissions_mt = 0.997
    trips_needed = jet_emission/trip_emissions_mt
    trips_needed = int(trips_needed)
    trip_output = f"You would have to drive from LA to NY {trips_needed} time{ "" if trips_needed == 1 else "s" } to emit this same amount."
    
    return trip_output
 
  else:
    
    #an average american emits 16 tons CO2 every year = 14.5 mt
    
    american_emissions_mt = 14.5
    years_needed = jet_emission/american_emissions_mt
    if years_needed <1:
      months_needed = years_needed * 12
      months_needed = int(months_needed)
      months_output = f"It would take an average American {months_needed} month{ "" if months_needed == 1 else "s" } to emit the same amount."
      return months_output
    else:
      years_needed = round(years_needed,2)
      years_output = f"It would take an average American {years_needed} year{ "" if years_needed == 1 else "s" } to emit the same amount."
      return years_output