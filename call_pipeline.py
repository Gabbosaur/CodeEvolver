import requests
from requests.auth import HTTPBasicAuth

# URL and credentials
url = "http://localhost:8060/job/test/build"
username = "Izanagi"
api_token = "11220636890f16b515ccaf259a205f448c"

# Data to be sent in the POST request
data = {"token": api_token}

# Sending the POST request
response = requests.post(url, auth=HTTPBasicAuth(username, api_token), data=data)

# Check the response
if response.status_code == 201:
    print("Build triggered successfully!")
else:
    print(f"Failed to trigger build. Status code: {response.status_code}, Response: {response.text}")
