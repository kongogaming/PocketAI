import requests 
url= "http://192.168.29.142:11434/api/generate" #Here you can change the url to your phone server url
def ask_ai(prompt):
    data = {
    "model": "gemma3:270m", #Here you can change the model to your desired model
    "prompt": prompt,
    "stream": False
}
    response = requests.post(url, json=data)
    result = response.json()
    return result["response"]

