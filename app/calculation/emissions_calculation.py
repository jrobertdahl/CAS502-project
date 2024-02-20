def calculate_emissions(km_traveled):

#source: [https://flybitlux.com/what-is-the-carbon-footprint-of-a-private-jet/]
# 4.9 kg per mile = 0.003045 mt per km

    average_metric_tons_co2_emitted_per_km = 0.003045
    metric_tons_co2_emitted = average_metric_tons_co2_emitted_per_km * km_traveled

    return metric_tons_co2_emitted