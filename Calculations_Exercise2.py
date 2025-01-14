import json

# Loads the .json contents into a variable
with open("precipitation.json") as file:
    measurements = json.load(file)

# Creates empty list to store the filtered station dictionaries in
Seattle_precipitation = {}

# Defines and splits all the months so we can use it for our "starts with" function
all_dates = "01 02 03 04 05 06 07 08 09 10 11 12".split()
# Defines empty dictionary for precipitation per month
precipitation_per_month = {}

# Creates empty dictionary for relative precepitation per month
relative_monthly_precipitation = {}

# Defines empty keys within the "precipitaton_per_month" dictionary
for date in all_dates:
    precipitation_per_month[date] = 0
    relative_monthly_precipitation[date] = 0

# Defines variable for total yearly precipitation for later use in loop
total_yearly_precipitation=0

# For loop to filter specifically the Seattle station observations into the empty list from before
for stations in measurements:
    if stations["station"] == "GHCND:US1WAKG0038":
        total_yearly_precipitation += stations["value"]
        for date in all_dates:
            if stations["date"].startswith(f"2010-{date}"):
                precipitation_per_month[date] += stations["value"]
            relative_monthly_precipitation[date] = precipitation_per_month[date] / total_yearly_precipitation
        Seattle_precipitation["precipitation_per_month"] = precipitation_per_month # Adds the above calculations into the larger dictionary so it's more verbose
        Seattle_precipitation["total_yearly_precipitation"] = total_yearly_precipitation
        Seattle_precipitation["relative_monthly_precipitation"] = relative_monthly_precipitation

#print(Seattle_precipitation)

# Saves the outputted results into a .json file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Seattle_precipitation, file, indent = 4)