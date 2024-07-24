# intro_devops
This repo is created to show how to run an action in a session. Test change to show CI

To Build the dockerfile:

    sudo docker build -t python_app .


Run the Docker Container:

    sudo docker run -p 4000:80 python_app



#Jenkins_docker image


To Build the dockerfile:

    sudo docker build -t jenkins-with-tf /path/to/dockerfile/


Run the Docker Container:

    sudo docker run -d -p 8080:8080 -p 50000:50000 jenkins-with-tf

Take the admin password

    sudo docker logs <container_id>

