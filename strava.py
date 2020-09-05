import requests
import urllib3
import credentials_actual
import pytz
from datetime import datetime
import getpass
from fbchat import Client
from fbchat.models import *
from helium import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': credentials_actual.client_id,
    'client_secret': credentials_actual.client_secret,
    'refresh_token': credentials_actual.refresh_token,
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

if not exercised_today:

    '''
    client = Client(credentials_actual.messenger_email, credentials_actual.messenger_password)
    client.send(Message(text="I'm trash and I didn't workout today!"), thread_id=credentials_actual.friend_uid, thread_type=ThreadType.USER)
    client.logout()
    '''
    driver = start_chrome('messenger.com/login', headless=True)
    write(credentials_actual.messenger_email, into='Email')
    write(credentials_actual.messenger_password, into='Password')
    click('Continue')   
    go_to('messenger.com/t/' + credentials_actual.friend_uid)
    write("I'm trash and I didn't workout today!", into='Type a message...')
    press(ENTER)
    kill_browser()

