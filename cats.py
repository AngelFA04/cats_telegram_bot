import requests
import os

def get_cat():
    response = requests.get(
                'https://api.thecatapi.com/v1/images/search?format=json',
                headers={
                    'Content-Type': 'application/json',
                    'x-api-key': 'a45568e8-407b-47b1-8082-481a8a5cb7e1'
                })
    print('Respuesta: ', response.content)
    print('JSON: ', response.json())
    print('URL: ', response.json()[0]['url'])
    
    return response.json()[0]['url']
get_cat()