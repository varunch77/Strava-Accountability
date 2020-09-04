import requests
import credentials

client_id = cred.client_id
client_secret = cred.client_secret
authorization_code = cred.authorization_code

url = "https://www.strava.com/oauth/token?client_id=" + client_id + "&client_secret=" + client_secret + "&code=" + authorization_code + "&grant_type=authorization_code"

payload = {}
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

new_access_token = response.json()["access_token"]
new_refresh_token = response.json()["refresh_token"]

file1 = open("cred.py", "a")  # append mode 
file1.write("\nrefresh_token = " + '"' + new_refresh_token + '"') 
file1.close()
