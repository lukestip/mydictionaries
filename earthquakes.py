import json
'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes
'''

infile = open('eq_data.json', 'r')
eq_data = json.load(infile)

eq_count = 0
for i in eq_data["features"]:
    if i['properties']['type'] == ('earthquake'):
        eq_count += 1

print(f"Number of earthquakes: {eq_count}.")


'''
2) iterate through the dictionary and extract the location NOTE(does this mean place?), magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.
'''
eq_dict = {}

num_eq = 1
for i in eq_data["features"]:
    if i["properties"]["mag"] > 6:
        eq_id = i["id"]
        eq_dict[eq_id] = {"location": i["properties"]["place"], "magnitude": i["properties"]["mag"],
                          "longitude": i["geometry"]["coordinates"][0], "latitude": i["geometry"]["coordinates"][1]}
        num_eq += 1

print(eq_dict)

'''
3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

for v in eq_dict.values():
    print(f"\nLocation: {v['location']}")
    print(f"Magnitude: {v['magnitude']}")
    print(f"Longitude: {v['longitude']}")
    print(f"Latitude: {v['latitude']}\n")
