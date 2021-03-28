import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 45
HEIGHT_CM = 158
AGE = 25

# https://www.nutritionix.com/business/api
APP_ID = "APP_ID"
API_KEY = "API_KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()
print(result)

# https://sheety.co
sheety_endpoint = "sheet endpoint"

today = datetime.now()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }
    # No Authentication
    # sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    # Basic Authentication
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, auth=("username", "password",))
    print(sheet_response.text)

# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
