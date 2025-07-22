import requests
from datetime import datetime

USERNAME="amitk"
TOKEN="ahvbjsfdv33onyuf343r1dod"
GRAPHID= "graph1"

pixela_endpoint="https://pixe.la/v1/users"

#step 1-----------Create your user account

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

#step 2:------------------Create a graph definition

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPHID,
    "name":"Cycling Graph",
    "unit":"Kn",
    "type":"float",
    "color":"ajisai",
}

header={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint, json=graph_config,headers=header)
# print(response.text)

#-------------------- step 3: Browse  https://pixe.la/v1/users/amitk/graphs/graph1.html

#-------------------- step 4: /v1/users/<username>/graphs/<graphID>

datetime=datetime.now()
today_date=datetime.strftime("%Y%m%d")

Post_value_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
test_date=20250110
Post_value_config={
"date":test_date,
"quantity":'11.5',
}

# response=requests.post(url=Post_value_endpoint, json=Post_value_config,headers=header)
# print(response.text)

#---------------------- step 5:  (put)/v1/users/<username>/graphs/<graphID>/<yyyyMMdd> (Update user)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{test_date}"
print(update_endpoint)
update_config={
"quantity":"5.6"
}
print(update_config)
# responses=requests.put(url=update_endpoint,json=update_config,headers=header)
# print(responses.text)
#-------------------- step 6:(delete) DELETE - /v1/users/<username>/graphs/<graphID>

# responses=requests.delete(url=update_endpoint,headers=header)
# print(responses.text)