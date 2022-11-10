import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "Token"
USERNAME = "Username"
To_view = "https://pixe.la/v1/users/avasarala/graphs/graph1.html"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpoint, json=user_params)

#-------------------------
#Creating Graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

#--------------------
#Creating a pixel
input_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()
required_format = today.strftime("%Y%m%d")

input_config = {
    "date": required_format,
    "quantity": "2.5"
}

# response = requests.post(url=input_endpoint, json=input_config, headers=headers)

#----------------------

#Updating pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{required_format}"

update_config = {
    "quantity": "10.0"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)

#-------------------------

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
