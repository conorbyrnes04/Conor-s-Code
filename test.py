#%%

import json

with open('airports_filtered.json', 'r') as file:
    airports = json.load(file)

print(len(airports))
# %%

for airport in airports:
    if airport['name'] == '':
        airport['name'] = airport['city'] + ' Airport'

# Save the updated airports data back to the file
with open('airports.json', 'w') as file:
    json.dump(airports, file, indent=2)

print("Updated airports with missing names and saved to file")
# %%

import json

# Load the airports dictionary
with open('airports2.json', 'r') as file:
    airports_dict = json.load(file)

# Convert to list and filter for only airports with IATA codes
airports_list = []
for airport_id, airport_data in airports_dict.items():
    if airport_data['iata'] and airport_data['iata'] != "":
        airports_list.append(airport_data)

# Save the filtered list to a new file
with open('airports_filtered.json', 'w') as file:
    json.dump(airports_list, file, indent=2)

print(f"Converted and filtered {len(airports_list)} airports with IATA codes")
# %%
