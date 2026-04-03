import requests

URL = "https://6738d32b4eb22e24fca919c0.mockapi.io/Grupo1"

def apiget(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        print('Successful request')
        print('Data:', data)
    else:
        print('Error in the request, details:', response.text)


apiget(URL)

# a function that makes two requests to the APIone to get all the data and another to get a specific data
def apiget(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        print('Successful request')
        print('Data:', data)
    else:
        print('Error in the request, details:', response.text)

    response = requests.get(URL + '/1')
    if response.status_code == 200:
        data = response.json()

        print('Successful request')
        print('Data:', data)
    else:
        print('Error in the request, details:', response.text)


apiget(URL)
`