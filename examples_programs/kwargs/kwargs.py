def make_api_call(model,prompt,**params):
    print("Model:",model)
    print("Prompt:",prompt)


    print(params)
    if model =="gemini":
        print(params.get("tokens"),params.get("gemini_api_key"),params.get("precision"))
    elif model =="Claude":
        print(params.get("tokens"),params.get("claude_token"))
    elif model =="Chatgpt":
        print(params.get("Chatgpt_account_id"),params.get("password"),params.get("precision"))
 
make_api_call(
    model="gemini",
    prompt="write python",
    tokens=10,
    gemini_api_key="1234567890",
    precision=1
)
make_api_call(
    model="Claude",
    prompt="write python",
    tokens=10,
    claude_token="12345te54354"       
)
make_api_call(
    model="Chatgpt",
    prompt="write python",
    Chatgpt_account_id="113434343",
    password="233453454",
    precision="2"
)

 
 