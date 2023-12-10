import requests,json

response = requests.get('https://dummyjson.com/products/1')

result = response.json()

for key, value in result.items():
    print(f"{key}:{value}")
# print("=============================================")
# print(type(response))
