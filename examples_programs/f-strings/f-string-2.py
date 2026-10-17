def ask_gemini_python(values,lines):
    prompt =f"hey can help me write a sample program on {values}, and write it in {lines} lines"
    print(prompt)
ask_gemini_python("python",10)
ask_gemini_python("functions",15)