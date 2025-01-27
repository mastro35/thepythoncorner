import requests

response = requests.get('https://stephen-king-api.onrender.com/api/books')

if response.status_code == 200:
    books = response.json()['data']
    for book in books:
        print(f"{book['Year']} - {book['Title']}")
else:
    print("an errore occured")
