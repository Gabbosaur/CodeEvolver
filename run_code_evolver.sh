 docker run -d -p 8080:8080 -p 50000:50000 -v $(pwd)/jenkins_home:/var/jenkins_home -v $(pwd)/jenkins_home/workspace:/var/jenkins_home/workspace -v $(pwd)/jenkins_home/users:/var/jenkins_home/users -v $(pwd)/jenkins_home/jobs:/var/jenkins_home/jobs --restart=on-failure jenkins/jenkins:lts-jdk17
 nohup uvicorn app:app --host 0.0.0.0 --port 8000 --reload &
 nohup streamlit run ui.py &
