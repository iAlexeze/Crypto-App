# Crypto-App Repository
This application fetches the current prices of selected cryptocurrencies using the Coingecko API.

## Contents

This repository contains the following directories:

**main.py:** This python file contains the source code for the flask-based application.

**k8s:** This file contains sample configurations of the YAML file for running the application in a kubernetes cluster.
 
**Dockerfile:** This is a simple Dockerfile for building a Docker image that runs a basic web application.

## Getting Started
To get started, clone this repository to your local machine:

git clone https://github.com/iAlexeze/Crypto-App.git

Once you have cloned the repository, you can explore the contents of the directories and files and use them as a starting point for your own Docker projects.

To build the Docker image using the Dockerfile, follow the instructions below:

## Build the Docker image:

docker build -t my-crypto-app .

This will create a Docker image named my-crypto-app based on the instructions in the Dockerfile.

Or, **Pull the image directly from Dockerhub**

Run:

docker pull ialexeze/cryptoprices:1.0.0

This will pull the application image from DockerHub into your local docker machine.

Either wyas, you should be able to see the images built or pulled, using the command:

docker images

## Run the Docker container:

docker run -p 5000:5000 my-crypto-app

This will start a Docker container based on the  my-crypto-app image and map port 5000 on your local machine to port 80 in the container.

## Access the web application in your browser:

http://localhost:5000  (you can replace the **localhost** with your **Node_IP** if your kubernetes cluster is in the cloud)
 
You should see a web page displaying the current prices of top cryptocurrencies.
Also, you would see the container ID of the docker container running the application as well as the your IP address 

## To run in Kubernetes Cluster

Kubectl apply -f k8s.yml

This will create a new deployment named **crypto-prices** as well as a Nodeport service named **crypto-svc** for external access

Access the application using http://localhost:31000  (you can replace the **localhost** with your **Node_IP** if your kubernetes cluster is in the cloud) 


## Contributing

Contributions to this repository are welcome. If you have diagrams, sample configurations, or code that you would like to contribute, please fork this repository and create a pull request with your changes.

## License

This repository is licensed under the MIT License. See the LICENSE file for more information and contribution.




