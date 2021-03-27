import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "keltoom"
TOKEN = "hkfjdlihkgrnkdlgjldkg"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_params = {
    "id": "test-graph",
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "ajisai"}
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_params,headers=headers)
# print(response.text)

# today = datetime(year=2021, month=3, day=26)
today = datetime.now()
pixel_params = {"date": today.strftime("%Y%m%d"),
                "quantity": input("How many pages did you read today? ")}

pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_data = {
    "quantity": "10",
}
update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_endpoint, json=update_data,headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint,headers=headers)
# print(response.text)
