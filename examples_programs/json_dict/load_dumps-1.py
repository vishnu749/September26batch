import json
params="""
{
    "model":"3.7-flash",
    "api_token":"43422335434345455",
    "tokens" :100

} 
"""
dict1 = json.loads(params)#whenever you are taking input from API 
print(dict1)
params = json.dumps(dict1)
print(params)#whenever you are sending data to api