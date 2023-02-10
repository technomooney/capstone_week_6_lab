import requests

api_url = 'https://catfact.ninja/fact'

response = requests.get(api_url)
data = response.json()
fact = data['fact']

print(f'A random Cat fact:\n{fact}')