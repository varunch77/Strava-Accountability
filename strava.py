import requests
import urllib3
import credentials
import pytz
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': credentials.client_id,
    'client_secret': credentials.client_secret,
    'refresh_token': credentials.refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activities_url, headers=header, params=param).json()

time_zone = pytz.timezone(my_dataset[0]['timezone'].split(')')[1][1:]) 
local_datetime = datetime.now(time_zone)
local_datetime = local_datetime.strftime("%Y-%m-%d")

#print(local_datetime)
#print(my_dataset[0]["start_date_local"].split('T')[0])

exercised_today = my_dataset[0]["start_date_local"].split('T')[0] == local_datetime
print(exercised_today)
