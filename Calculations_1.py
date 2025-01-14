import json

# Reads the content of the .csv into a variable
with open("stations.csv") as file:
    contents = file.read()

#print(contents)

# Loads the .json contents into a variable
with open("precipitation.json") as file:
    measurements = json.load(file)

# Creates empty list to store the filtered station dictionaries in
Seattle_precipitation = []

# Defines and splits all the months so we can use it for our "starts with" function
all_dates = "01 02 03 04 05 06 07 08 09 10 11 12".split()
# defines empty dictionary to put empty info in
precipitation_per_month = {}

#
for date in all_dates:
    precipitation_per_month[date] = 0

# For loop to filter specifically the Seattle station observations into the empty list from before
for stations in measurements:
    if stations["station"] == "GHCND:US1WAKG0038":
        for date in all_dates:
            if stations["date"].startswith(f"2010-{date}"):
                precipitation_per_month[date] += stations["value"]    

#Seattle_precipitation.append(stations)

#print(f" for {date} precipitation is {precipitation_per_month}")

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(precipitation_per_month, file, indent = 4)

#Seattle_precipitation.append(stations)