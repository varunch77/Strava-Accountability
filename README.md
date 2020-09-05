![Strava](https://www.ride25.com/wp-content/uploads/2014/10/strava_rgb_logotype.png)
# Strava Accountability
Many of us make commitments to exercise each day. However, if you’re only accountable to yourself, it's easy to let those commitments slide. Telling someone else about your goals and having someone to be accountable to makes you much more likely to follow through. That's why I wrote this program. It checks Strava everyday at 11 PM and messages a friend if you didn't exercise that day. Just set it up once and let it run everyday.

## Summary

  - [Getting Started](#getting-started)
  - [Runing the tests](#running-the-tests)
  - [Automation](#automation)
  - [Built With](#built-with)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a working  copy of the project up and running on your computer. All you need is a Strava account and Python.

[Create a Strava Account](https://www.strava.com/register/free)

[Download Python](https://www.python.org/downloads/)

### Create a Strava Application
*Note: Check to see if the location on your Strava profile is accurate. It seems that the default for an account created in the US is Los Angeles and uses the Pacific Time Zone. If the time zones do not match, the program will not always work.*

After logging into your Strava account, navigate to [API Settings](https://www.strava.com/settings/api) page to create a developer account.

You should see a screen like this:

![Blank Strava App Form](https://user-images.githubusercontent.com/48163435/92311694-702f6880-ef87-11ea-9f56-5785ceb7d0ed.png)

These fields can be filled out randomly except for the Authorization Callback Domain. **Make sure to set the callback domain to localhost**.

On the next screen you should see a screen that asks you to upload an app icon. Select any image you desire and continue.

Once you're finished you should see the following screen:

![Application Keys](https://user-images.githubusercontent.com/48163435/92311883-30698080-ef89-11ea-9f8b-9622105308e1.png)

### Authorizing Your Application

Copy and paste the following URL (make sure to replace [CLIENT_ID] with your application's client id) into your browser:

https://www.strava.com/oauth/authorize?client_id=[CLIENT_ID]&redirect_uri=http://localhost&response_type=code&scope=activity:read_all

Authorize the application:

![Authorize](https://user-images.githubusercontent.com/48163435/92311924-abcb3200-ef89-11ea-82e9-a22ae3cec5fd.png)

You should see this after you authorize:

![image](https://user-images.githubusercontent.com/48163435/92311961-0b294200-ef8a-11ea-8878-61a447f48a31.png)

Copy the URL you see in the browser. It should be in this format:

http://localhost/?state=&code=[ALPHANUMERIC_CODE]&scope=read,activity:read_all

Make sure to store this code somewhere. If you lose it, you will have to re-authorize the application and get a new code.

Now, clone this repo if you haven't already:

```bash
git clone https://github.com/VarunChilukuri/Strava-Accountability.git
```

Open `credentials.py` and fill out the first three fields (`authorization_code`, `client_id`, and `client_secret`).

Now choose a friend to be your accountability partner and navigate to their  Facebook profile page. Copy and paste the URL into [this website](https://commentpicker.com/find-facebook-id.php) to find their Facebook User ID.

Go back to `credentials.py` and fill out the `friend_uid`, `messenger_email`, and `messenger_password` fields.

*Note: Some of you might be worried about the safety of openly storing your Messenger credentials in a plain text file. The part of the program that messages a friend is all done locally and no data is sent.*

## Running the Tests

Before running the main file (`strava.py`), you need to run `init.py` once to finish the setup. Install the requests package:

```bash
pip install requests
```

*Note: If you don't have pip installed, download it [here](https://pip.pypa.io/en/stable/installing/).*
<br>

Now run `init.py`. Once it's finished, you should notice that a new `refresh_token` has been added to your `credentials.py` file.

Now it's time to run `strava.py`. Once again, you need to install a few packages before doing so:

Install urllib3:

```bash
pip install urllib3
```
Install pytz:
```bash
pip install pytz
```
Install helium:

```bash
pip install helium
```
Finally, go to line 42 and add a custom message for your friend. Now run `strava.py`. If everything goes well, your friend should get a message if you didn't upload an activity to Strava today.


## Automation

In order to have `strava.py` run everyday at a set time, you need to tell your computer to automate it. The procedures are different for each operating system.

### Windows
Open notepad and create a file that follows this format: 

![Windows BAT file](https://user-images.githubusercontent.com/48163435/92312784-39128480-ef92-11ea-8512-6841a160dd4c.png)

**Important**: Save it as a BAT file.

Open Task Scheduler and click on 'Create Task'

![Create Task on Task Scheduler](https://user-images.githubusercontent.com/48163435/92312810-7a0a9900-ef92-11ea-8ec4-45202b08201f.png)

Fill in information:

![Create Task - General](https://user-images.githubusercontent.com/48163435/92313396-74648180-ef99-11ea-8608-8ad1ca5db233.png)

Create a new trigger:

![Create Task - Triggers](https://user-images.githubusercontent.com/48163435/92313013-8859b480-ef94-11ea-8ce8-f684f5612ccf.png)

Create a new action:

![Create Task - Actions](https://user-images.githubusercontent.com/48163435/92313071-2ea5ba00-ef95-11ea-86a0-46aca2c8a06f.png)

### MacOS
Instructions coming soon.

### Linux
Instructions coming soon.

That's it! Your computer will automatically run the file everyday and message your friend if you don't exercise.

## Built With

  - [Python](https://www.python.org/)
  - [Strava API](https://developers.strava.com/)
  - [Helium](https://github.com/mherrmann/selenium-python-helium)


## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

  - Fran Polignano ([fpolignano](https://github.com/fpolignano))
  - Dev Patel ([moonbeam87](https://github.com/moonbeam87))
