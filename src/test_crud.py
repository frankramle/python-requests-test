import requests

_url = "https://api-irso.herokuapp.com"
_id = ""

#Obtengo todos los clientes
def test_get_clientes():
    resp = requests.get(_url + "/clientes")
    customers = resp.json()['customers']
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    assert (len(customers) > 0)
    print(customers)

#Inserto un nuevo cliente
def test_post_insertar_cliente():
    data = \
    {
        'nombres': 'Adrian',
        'apellido': 'Ramos',
        'direccion': 'Peron 2019',
        'cod_postal': '1032',
        'telefono': '65289657485'
    }
    resp = requests.post(url=_url + "/clientes", json=data)
    global _id
    _id = str(resp.json()['id'])
    jsonData = resp.json()
    print(resp.json())
    assert (resp.status_code == 201), "Status code is not 201. Rather found : " + str(resp.status_code)
    assert 'id' in jsonData
    assert 'apellido' in jsonData
    assert 'direccion' in jsonData
    assert 'cod_postal' in jsonData
    assert 'telefono' in jsonData

#Modifico los datos del cliente ingresado
def test_put_modificar_cliente():
    data = \
    {
        'nombres': 'Adrian02',
        'apellido': 'Ramos02',
        'direccion': 'Peron 2019',
        'cod_postal': '1032',
        'telefono': '65289657485'
    }
    resp = requests.put(url=_url + "/clientes/" + _id,  json=data)
    id = str(resp.json()['id'])
    nombres = str(resp.json()['nombres'])
    apellido = str(resp.json()['apellido'])
    direccion = str(resp.json()['direccion'])
    cod_postal = str(resp.json()['cod_postal'])
    telefono = str(resp.json()['telefono'])
    print(resp.json())
    assert (resp.status_code == 200), "Status code is not 201. Rather found : " + str(resp.status_code)
    assert (id == _id), "ID is different al params. Response id is: " + id
    assert (nombres == data['nombres']), "Nombres is different to the request. Response nombres is: " + nombres
    assert (apellido == data['apellido']), "Apellido is different to the request. Response apellido is: " + apellido
    assert (direccion == data['direccion']), "Direccion is different to the request. Response direccion is: " + direccion
    assert (cod_postal == data['cod_postal']), "Cod_postal is different to the request. Response cod_postak is: " + cod_postal
    assert (telefono == data['telefono']), "Telefono is different to the request. Response telefono is: " + telefono

#Elimino el cliente que inserte
def test_delete_cliente():
    resp = requests.delete(_url + "/clientes/" + _id)
    assert (resp.status_code == 204), "Status code is not 201. Rather found : " + str(resp.status_code)

#Verifico que el cliente no este en la BD
def test_get_cliente():
    resp = requests.get(_url + "/clientes" + _id)
    assert (resp.status_code == 404), "Status code is not 200. Rather found : " + str(resp.status_code)