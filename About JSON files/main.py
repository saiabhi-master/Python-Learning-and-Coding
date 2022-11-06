# Working with JavaScript Object Notation (JSON ) Files
import json



#to load into a python object
people_string = '''
    {
        "people": [
            {
                "name": "john smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@gmail.com", "js@gmail.com"],
                "has_license": False
            },
            {
                "name": "jane doe",
                "phone": "560-555-5153",
                "emails": None,
                "has_license": True
            }
        ]
    }
'''

# to load as json object or python dict
data = json.loads(people_string)  #load(s) because it is an object and not file
# type(data) ==> Dictionary
# type(data["people"]) is a list

# to delete phone number column and load into JSON object again
for person in data["people"]:
    del person["phone"]

new_string = json.dumps(data, indent=2) # for each level it indents two levels