import requests

url = 'https://fakestoreapi.com/products/category/jewelery'

try:
    response= requests.get(url)#sūta GET pieprasījumu
    response.raise_for_status()#pārbauda
    data = response.json()#ja pieprasijums ir veiksmigs tad trurpinas
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")