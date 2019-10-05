# micro-app-2-bbk
Microservice app_2 of web app for MSc Data Science project repo (microservice auto-scaling system)

# Description
Application summary as part of test microservice based web application (seen in 2019 N C Coulson paper: "Adaptive microservice scaling for elastic web applications")

App 2 generates a list of random numbers five times the size of the input integer and then sorts it using the built in Python sort function, which utilises the Tim sort algorithm. The function returns a random number from that list.

# Deployment
This github repo is linked to a DockerHub repo (https://cloud.docker.com/u/certainnathan/repository/docker/certainnathan/micro-app-2-bbk) which is referenced in the Swarm deployment YAML config file. Any accepted changes will be automatically incorporated into the latest Docker image used in the main application.
