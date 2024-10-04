# CodeEvolver

**CodeEvolver** is a powerful AI-powered code transformation and enhancement tool designed to continuously optimize software quality through iterative improvement.

## Key Features

- **Code Transformation**: Utilizes advanced AI algorithms to analyze and automatically improve existing code.
- **Continuous Improvement**: Integrates feedback and test results to refine the code continuously.
- **Automated Testing**: Executes functional and unit tests to ensure that changes do not compromise the stability of the project.

## Installation Requirements

Ensure you have Docker installed on your system to run the application.

## How to Run

To start **CodeEvolver**, use the following commands:

1. Run the Jenkins Docker container:
  ```bash
   docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --restart=on-failure izanagi95/jenkins_rebirth:latest
  ```
2. Start the FastAPI application:
  ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
  ```


## Accessing Services
- **API Service**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Jenkins Platform**: http://localhost:8080

<!-- 
## Contributing
If you wish to contribute to CodeEvolver, feel free to open an issue or submit a pull request. Every contribution is welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
-->
