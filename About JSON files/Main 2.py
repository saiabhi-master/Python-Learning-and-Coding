import json

#load method - loads a file into a python object

with open("states.json") as f:
    data = json.load(f)
    #print(data) -- > prints as a dictionary

for state in data["states"]:
    print(state["name"], state["abbreviation"]) #prints name and abb
    del state["area_codes"]  #deletes area code column

with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)

# python object to be appended
y = {"pin": 110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))


