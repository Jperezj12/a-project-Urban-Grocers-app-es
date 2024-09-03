import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_kit(new_kit):
    # Hacer la solicitud para crear el usuario
    user_response = post_new_user(data.user_body)
    response_json = user_response.json()
    # Guardar el authToken en una variable
    auth_token = response_json.get("authToken")

    # Concatenar el token de autorización en el encabezado
    autorizacion = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }

    # Hacer la solicitud para crear el kit
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         json=new_kit,
                         headers=autorizacion)
