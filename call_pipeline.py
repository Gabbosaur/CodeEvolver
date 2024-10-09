import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# URL and credentials from environment variables
url = os.getenv("JENKINS_BUILD_BASE_URL") + "/build"
username = os.getenv("JENKINS_USERNAME")
api_token = os.getenv("JENKINS_API")

def main():
    # Data to be sent in the POST request
    data = {"token": api_token}

    # Sending the POST request
    response = requests.post(url, auth=HTTPBasicAuth(username, api_token), data=data)

    # Check the response
    if response.status_code == 201:
        print("Build triggered successfully!")
    else:
        print(f"Failed to trigger build. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    main()
