import requests
import secret
from datetime import datetime

time = datetime.now()
body_nutritionix = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":20
}

header_nutritionix = {
    "x-app-id": secret.nutritionix_app_id,
    'x-app-key': secret.nutritionix_api_key
}

response_nutritionix = requests.post(url=secret.nutritionix_app_endpoint, json=body_nutritionix, headers=header_nutritionix)
response_nutritionix.raise_for_status()
result_nutritionix = response_nutritionix.json()["exercises"][0]

peyload_sheety = {
    "workout": {
        "date": time.strftime('%d/%m/%Y'),
        "time": time.strftime('%H:%M:%S'),
        "exercise": result_nutritionix["user_input"].capitalize(),
        "duration": result_nutritionix["duration_min"],
        "calories": result_nutritionix["nf_calories"],
    }
}

response_sheety = requests.post(url=secret.sheety_endpont, json=peyload_sheety, headers=secret.sheety_breat)
response_sheety.raise_for_status()

