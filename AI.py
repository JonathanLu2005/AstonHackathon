import google.generativeai as genai

genai.configure(api_key='AIzaSyDl-uTs1Fj8bAMQHuiIUWJzTsWN09efumw')

model = genai.GenerativeModel('gemini-pro')

prompt = """ """

response = model.generate_content(prompt)

print(response.parts[0].text)