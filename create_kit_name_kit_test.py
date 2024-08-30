import sender_request
import data


# esta función cambia los valores en el parámetro "Name"
def get_user_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    current_kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_kit_body

def positive_asser_kit_body(kit_body):
    kit_response = sender_request.post_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] ==kit_body['name']
    print(kit_response.status_code)
    print(kit_response.json())

def negative_assert_code400(kit_body):
    kit_response = sender_request.post_kit(kit_body)
    assert kit_response.status_code == 400

# Test 1 El número permitido de caracteres (1) Response 201
def test_numero_caracter_1():
    kit_body = get_user_body("a")
    positive_asser_kit_body(kit_body)

# Test 2 El número permitido de caracteres (511) Response Failed
def test_numero_caracter_511():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_asser_kit_body(kit_body)

# Test 3 	El número de caracteres es menor que la cantidad permitida (0) Response 201
def test_numero_caracter_0():
    kit_body = get_user_body("")
    positive_asser_kit_body(kit_body)

# Test 4 El número permitido de caracteres (512) Response Failed
def test_numero_caracter_512():
    kit_body = get_kit_body("AgbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_asser_kit_body(kit_body)

# Test 5 Se permiten caracteres especiales:  Response 201
def test_caracter_especiales():
    kit_body = get_user_body("@%&/,")
    positive_asser_kit_body(kit_body)

# Test 6 Se permiten espacios:  Response 201
def test_espacios():
    kit_body = get_user_body("Aaa AA")
    positive_asser_kit_body(kit_body)

# Test 7 Se permiten numeros:  Response 201
def test_numeros_espacios_numeros():
    kit_body = get_user_body("Aaa AA 999")
    positive_asser_kit_body(kit_body)

# Test 8 El parámetro no se pasa en la solicitud:  Response 400
def test_blank():
    kit_body = get_user_body( { })
    positive_asser_kit_body(kit_body)

# Test 9 Se ha pasado un tipo de parámetro diferente (número):  Response 201
def test_numeros1():
    kit_body = get_user_body(123)
    positive_asser_kit_body(kit_body)