# This function is taking the km traveled by a jet and converting it to metric tons of CO2 emitted into the atmosphere. It assumes
# that all people are flying the same jet

def calculate_emissions(km_traveled):

#source: [https://flybitlux.com/what-is-the-carbon-footprint-of-a-private-jet/]
# 4.9 kg per mile = 0.003045 mt per km

    average_metric_tons_co2_emitted_per_km = 0.003045
    metric_tons_co2_emitted = round(average_metric_tons_co2_emitted_per_km * km_traveled, 2)

    return metric_tons_co2_emitted
