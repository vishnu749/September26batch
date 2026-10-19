import json

def call_gemini(geminiInput,prompt):
    print("Model:",geminiInput["model"])
    print("api_token:",geminiInput["api_token"])
    print("tokens:",geminiInput["tokens"])
    print("prompt:",prompt)

#with open("gemini-config.json","r") as file:
   # print(file.read())

#call_gemini(geminiInput,"what is Prompt")
#for read in disctonary to json
with open("gemini-config.json","r") as file:
    geminiInput = json.loads(file.read())

response = call_gemini(geminiInput,"what is Prompt")
print(response)
#for read in json to disctonary
with open("gemini-response.json","w") as file:
    json.dump(response,file,indent=4)