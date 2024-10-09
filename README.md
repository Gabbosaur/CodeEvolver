# CodeEvolver

**CodeEvolver** is a powerful AI-powered code transformation and enhancement tool designed to continuously optimize software quality through iterative improvement.

## Key Features

- **Code Transformation**: Utilizes advanced AI algorithms to analyze and automatically improve existing code.
- **Continuous Improvement**: Integrates feedback and test results to refine the code continuously.
- **Automated Testing**: Executes functional and unit tests to ensure that changes do not compromise the stability of the project.

## Installation Requirements

Ensure you are in Linux environment and you have Docker installed on your system to run the application.
1. Clone this repository:
  ```bash
   git clone https://github.com/Gabbosaur/CodeEvolver.git
  ```
2. Enter the project and configure the environment:
  ```bash
   cd CodeEvolver
   python -m venv venv
   source venv/bin/activate
  ```
3. Install tkinter:
  ```bash
   sudo apt-get install python3-tk
  ```

## Deploy

To start **CodeEvolver**, use the following commands:

1. Run the Jenkins Docker container:
  ```bash
   sudo docker run -p 8080:8080 -p 50000:50000 -v $(pwd)/jenkins_home:/var/jenkins_home -v $(pwd)/jenkins_home/workspace:/var/jenkins_home/workspace -v $(pwd)/jenkins_home/users:/var/jenkins_home/users -v $(pwd)/jenkins_home/jobs:/var/jenkins_home/jobs --restart=on-failure jenkins/jenkins:lts-jdk17
  ```
2. Start the FastAPI application:
  ```bash
   nohup uvicorn app:app --host 0.0.0.0 --port 8000 --reload &
  ```
3. Start CodeEvolver UI:
  ```bash
   nohup streamlit run ui.py &
  ```
3. Go to CodeEvolver UI via browser http://localhost:8501

## Accessing Services
- **CodeEvolver UI**: http://localhost:8501
- **API Service**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Jenkins Platform**: http://localhost:8080
  - ***user***: Izanagi
  - ***pwd***: Izanagi95


<!-- 
## Contributing
If you wish to contribute to CodeEvolver, feel free to open an issue or submit a pull request. Every contribution is welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
-->
