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




