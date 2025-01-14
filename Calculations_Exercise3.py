import json
import csv

# This will load in the stations csv as a list of dictionaries
with open("stations.csv") as file:
    station_codes = list(csv.DictReader(file))

# Defines and splits all the months so we can use it for our "starts with" function
all_dates = "01 02 03 04 05 06 07 08 09 10 11 12".split()

# Loads the .json contents into a variable
with open("precipitation.json") as file:
    measurements = json.load(file)

# Creates an empty dictionary to store the precipitation calculation results of separate cities
results = {}

cities_yearly_precipitation = 0

# For loop for each individual station's precipitation observations
for station in station_codes:
    station_code = station['Station']

    # Creates empty dictionary to store the filtered station dictionaries in
    city_precipitation = {}

    # Defines variable for total yearly precipitation for later use in loop
    total_yearly_precipitation=0
    
    # Defines empty dictionary for precipitation per month
    precipitation_per_month = {}

    # Creates empty dictionary for relative precepitation per month
    relative_monthly_precipitation = {}

    # Defines empty keys within the "precipitaton_per_month" dictionary
    for date in all_dates:
        precipitation_per_month[date] = 0
        relative_monthly_precipitation[date] = 0

    for stations in measurements:
        if stations["station"] == station_code:
            total_yearly_precipitation += stations["value"]
            for date in all_dates:
                if stations["date"].startswith(f"2010-{date}"):
                    precipitation_per_month[date] += stations["value"]

    for date in precipitation_per_month:
        relative_monthly_precipitation[date] = precipitation_per_month[date] / total_yearly_precipitation
    
    city_precipitation["precipitation_per_month"] = precipitation_per_month # Adds the above calculations into the larger dictionary so it's more verbose
    city_precipitation["total_yearly_precipitation"] = total_yearly_precipitation
    city_precipitation["relative_monthly_precipitation"] = relative_monthly_precipitation

    cities_yearly_precipitation += city_precipitation["total_yearly_precipitation"] 

    results[station["Location"]] = city_precipitation

for station in station_codes:
    city_precipitation = results[station["Location"]]

    relative_yearly_precipitation = city_precipitation["total_yearly_precipitation"] / cities_yearly_precipitation
    city_precipitation["relative_yearly_precipitation"] = relative_yearly_precipitation

    results[station["Location"]] = city_precipitation

#print(Seattle_precipitation)

# Saves the outputted results into a .json file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent = 2)