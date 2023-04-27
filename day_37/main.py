import requests
import secret
from datetime import datetime
GRAPH_ID = "day38"
is_register = True
is_created = True

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": secret.pixela_api,
    "username": secret.pixela_user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
if not is_register:
    response = requests.post(url=pixela_endpoint, json=user_params)

graph_api = pixela_endpoint + "/" + secret.pixela_user + "/graphs"

graphs_params = {
    "id": GRAPH_ID,
    "name": "init",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": secret.pixela_api
}

if not is_created:
    response = requests.post(url=graph_api, json=graphs_params, headers=headers)
now = datetime.now()
point_params = {
    "date": now.strftime("%Y%m%d"),
    "quantity": "12",
}
board_api = graph_api+ "/" + GRAPH_ID
if False:
    response = requests.post(url=board_api, json=point_params, headers=headers)

if None:
    response = requests.put(url=board_api.point_paramsp["date"], json=point_params, headers=headers)

if is_created:
    response = requests.delete(url=board_api.point_paramsp["date"], headers=headers)