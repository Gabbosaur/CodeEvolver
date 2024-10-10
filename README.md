# CodeEvolver

**CodeEvolver** is a powerful AI-powered code transformation and enhancement tool designed to continuously optimize software quality through iterative improvement.

## Key Features

- **Code Transformation**: Utilizes advanced AI algorithms to analyze and automatically improve existing code.
- **Continuous Improvement**: Integrates feedback and test results to refine the code continuously.
- **Automated Testing**: Executes functional and unit tests to ensure that changes do not compromise the stability of the project.

## Installation Requirements

Ensure you are in **`Linux`** environment and you have **`Docker`** installed on your system to run the application.
1. Clone this repository:
  ```bash
   git clone https://github.com/Gabbosaur/CodeEvolver.git
  ```
2. Navigate into the project, create a virtual environment and activate it:
  ```bash
   cd CodeEvolver
   python -m venv venv
   source venv/bin/activate
  ```
3. Install the libraries:
  ```bash
   pip install -r requirements.txt
  ```

## Deploy

To start **CodeEvolver**, open 3 different terminals and use the following commands (otherwise append " &" for running in the background):

1. Run the Jenkins Docker container:
  ```bash
   sudo docker run -p 8080:8080 -p 50000:50000 -v $(pwd)/jenkins_home:/var/jenkins_home -v $(pwd)/jenkins_home/workspace:/var/jenkins_home/workspace -v $(pwd)/jenkins_home/users:/var/jenkins_home/users -v $(pwd)/jenkins_home/jobs:/var/jenkins_home/jobs --restart=on-failure jenkins/jenkins:lts-jdk17
  ```
2. Start the FastAPI application (you will see here the relevant logs processing in background):
  ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
  ```

3. Start CodeEvolver UI:
  ```bash
   streamlit run ui.py
  ```
3. Go to CodeEvolver UI via browser http://localhost:8501

## Accessing Services
- **CodeEvolver UI**: http://localhost:8501
- **API Service**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Jenkins Platform**: http://localhost:8080
  - ***user***: Izanagi
  - ***pwd***: Izanagi95

## Notes
Normally, the env file should not be saved in the repository, but to facilitate those who will need to test our solution, it has been included. Similarly, data such as the jenkins_home folder should not be saved either.

In the `.env` file, we can manage how the Large Language Model (LLM) is executed:

- **LLM_MODE** (default: **GROQ**):
  - **OLLAMA**: The LLM runs locally using the Ollama tool installed on your machine, utilizing local resources. Before running the application in this mode, you must first install the Ollama tool locally.
  - **GROQ**: The LLM runs on a cloud service via an API key, meaning it is executed remotely and does not rely on local resources. However, this introduces potential risks to the security and privacy of the data being generated.

<!-- 
## Contributing
If you wish to contribute to CodeEvolver, feel free to open an issue or submit a pull request. Every contribution is welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
-->
