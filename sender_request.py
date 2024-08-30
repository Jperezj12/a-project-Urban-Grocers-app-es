import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
            json=body,
            headers=data.headers)
    return response


# Hacer la solicitud para crear el usuario
user_response = post_new_user(data.user_body)
print(user_response.status_code)
response_json = user_response.json()
print(response_json)
# Guardar el authToken en una variable
auth_token = response_json.get("authToken")
# Imprimir el authToken
print("authToken:", auth_token)


autorizacion = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
    }

def post_kit(new_kit):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
            json=new_kit,
            headers=autorizacion)

kit_response = post_kit(data.kit_body)
print(kit_response.status_code)
print(kit_response.json())