# Testing Restful API with Python Pytest

## Purpose
- For testing, which using 
  - Pytest framework 
  - Jenkins 
  - Allure report 
  - Docker 
- Support testing 
  - Restful api testing (Testing resouces : https://fakerestapi.azurewebsites.net)

## Directory Structure
```
git ls-tree -r --name-only HEAD | tree --fromfile
.
├── .gitignore
├── README.md
├── business
│   ├── api_request.py
│   ├── books
│   │   ├── books_api.py
│   │   └── books_database.py
│   ├── database_execution.py
│   └── users
│       ├── users_api.py
│       └── users_database.py
├── configurations
│   ├── __init__.py
│   ├── api_domain.py
│   └── database.py
├── conftest.py
├── deployments
│   ├── Dockerfile
│   ├── Jenkinsfile
│   └── job_configurations.json
├── logger.py
├── requirements.txt
└── test_suites
    ├── test_books
    │   └── test_get_books_id.py
    └── test_users
        ├── test_get_users.py
        └── test_post_users.py

```

## Step-by-step
### Option 1: Build up a simple Docker
Input the command
```
docker build -t pytest_learn_image -f ./deployments/Dockerfile .
```
### Option 2: Build up Jenkins Docker
_Ref: [How to Run Jenkins Container as Systemd Service with Docker](https://discuss.circleci.com/t/how-can-i-extract-the-junit-xml-files-from-within-a-docker-container-in-docker/24089/2)_
1. Build a Jenkins run in Docker
- `--name jenkins` : Container naming
- `-p 8080:8080` : Container 8080 port mapping to localhost 8080 port, which for jenkins administrator login.
- `-p 50000:50000` Container 50000 port mapping to localhost 50000 port, which for jenkins slave node's JNLP (Java Web Start) port.
- `-v ~/jenkins_home:/var/jenkins_home` : Build up docker volume. Container /var/jenkins_home mapping to localhost ~/jenkins_home.
- `-v /var/run/docker.sock:/var/run/docker.sock` : Let containers can use docker daemon.
```
$ docker run --name jenkins -p 8080:8080 -p 50000:50000 -v ~/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
```

2. Started the container and command for installation
```
$ apt-get update
$ apt install python3
$ apt install python3.11-venv
$ apt-get install -y wget
$ wget https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip
$ unzip allure-2.14.0.zip
$ export PATH=$PATH:/path/to/allure-2.14.0/bin
```
_Note: If docker cli encountering no permission_
```
$ docker exec -u 0 -it {#CONTAINER_ID} /bin/bash
```

3. Launch browser way to http://localhost:8080/ \
a. Unlock the Jenkins with password. The password form container's logs when u started the container.\
b. Install suggested plugins.
_Ref. [How to Run Jenkins Container as Systemd Service with Docker](https://www.linuxtechi.com/run-jenkins-docker-container-systemd/)_

4. Change Jenkinsfile configurations \
a. `GIT_REPO` : Ur repo \
b. `_GIT_CREDENTIALS_ID` : From Jenkins credentials setting Ref How To Add Git Credentials In Jenkins \
_Ref. [Configuring the Git Credentials in Jenkins](https://medium.com/@nikhil.nagarajappa/configuring-the-git-credentials-in-jenkins-4b584a797b45)_
![Jenkinsfile_config.png](readme%2FJenkinsfile_config.png)

5. Change job configurations
In this case, the pipeline job will separate by services. \
Thus, We may create the pipeline by services. \
Before create the Jenkins pipeline, we need to add job in `job_configuration.json`. \ 
```
└── test_suites
    ├── test_books
    │   └── test_get_books_id.py
    └── test_users
        ├── test_get_users.py
        └── test_post_users.py
```
![job_config_json.png](readme%2Fjob_config_json.png)

6. Build Jenkins pipeline, select [new items] build a new job.
![jenkins_new_item.png](readme%2Fjenkins_new_item.png)

7. Give a job naming and select pipeline
![jenkins_choose_pipeline.png](readme%2Fjenkins_choose_pipeline.png)

8. Do the config
- `Repository URL` : # Git repo
- `Credentials` : _Ref. [Configuring the Git Credentials in Jenkins](https://medium.com/@nikhil.nagarajappa/configuring-the-git-credentials-in-jenkins-4b584a797b45)_
- `Branches to build` : */master
- `Script Path` : deployments/Jenkinsfile
![jenkins_pipeline_config.png](readme%2Fjenkins_pipeline_config.png)

9. Okieee, then run the job. Click [Build parameters]
![jenkins_job_builds_params.png](readme%2Fjenkins_job_builds_params.png)

10. Input parameters (optional, if didn't input then run as default)
![job_run_build.png](readme%2Fjob_run_build.png)

11. Job complete
![jenkins_job_complete.png](readme%2Fjenkins_job_complete.png)

12. May way to allure report to check the result :)
![allure_report.png](readme%2Fallure_report.png)
