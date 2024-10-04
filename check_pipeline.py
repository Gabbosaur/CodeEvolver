import time
import requests

def is_job_finished(job_url, base_build_url, username, api_token):
    # Poll Jenkins to check the status of the last build
    while True:
        response = requests.get(job_url, auth=(username, api_token))
        if response.status_code == 200:
            job_info = response.json()
            last_build_number = job_info['lastBuild']['number']
            print(last_build_number)
            build_url = f"{base_build_url}/{last_build_number}/api/json"
            #print(build_url)
            # Get build status
            build_response = requests.get(build_url, auth=(username, api_token))
            build_info = build_response.json()

            # Check if build is still running
            if build_info['building']:
                print("Job is still running...")
            else:
                print(f"Job finished with status: {build_info['result']}")
                break
        else:
            print(f"Failed to get job status. Status code: {response.status_code}")

        # Wait before polling again
        time.sleep(10)

    console_url = f"{base_build_url}/{last_build_number}/consoleText"

    # Fetch the console output for the latest build
    console_response = requests.get(console_url, auth=(username, api_token))
    print(console_url)
    if console_response.status_code == 200:
        print(console_response.text)
        return console_response.text
    else:
       return f"Failed to get console output. Status code: {console_response.status_code}"


username = "Izanagi"
api_token = "1133c548af7366c093ec56d1152234a9b6"
jenkins_job_url = "http://localhost:8080/job/test/api/json"
jenkins_build_url = "http://localhost:8080/job/test"
is_job_finished(jenkins_job_url, jenkins_build_url, username, api_token)
