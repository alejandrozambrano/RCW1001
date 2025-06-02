import requests

#url='http://localhost:8000'
url='http: api-students-rcw-h2gchucugmayhph6.canadaeast-01.azurewebsites.net'
response=requests.get(url)
response=response.json()
print(response['message'])