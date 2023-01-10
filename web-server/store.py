import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print('Status Code:',r.status_code)
    print('Contenido:',r.text)
    print('Tipo de dato:',type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])