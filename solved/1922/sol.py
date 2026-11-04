import requests

url = "http://host3.dreamhack.games:16599/whoami"

headers = {
    "Authorization": "Basic YWRtaW46MWRlOThlMTM3MDhjMWYxZjYwMjNlMTMxYTdiZDg2NzY=",
}

response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")
print(response.text)