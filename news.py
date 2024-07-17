import requests
from keys import NEWS_API

country_code=input('Enter the country code in ISO 2-Alpha format\n')

response=requests.get(f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={NEWS_API}')

if response.status_code==200 :
    data=response.json()
    articles=data['articles']
    n=data['totalResults']
    print("Top headlines")
    for i in range(n) :
        print(f"{i+1} : '{articles[i]['title']}'")