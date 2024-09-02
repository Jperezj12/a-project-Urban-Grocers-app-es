import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Hacer la solicitud para crear el usuario
user_response = post_new_user(data.user_body)

response_json = user_response.json()

# Guardar el authToken en una variable
auth_token = response_json.get("authToken")


def post_kit(new_kit):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         json=new_kit,
                         headers=autorizacion)


autorizacion = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}
