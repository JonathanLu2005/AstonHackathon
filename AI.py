import google.generativeai as genai

genai.configure(api_key='AIzaSyDl-uTs1Fj8bAMQHuiIUWJzTsWN09efumw')

model = genai.GenerativeModel('gemini-pro')

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.parts[0].text
