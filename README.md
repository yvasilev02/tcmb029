# Project: docker/mininet task 

## Project Description

This project was developed as a final assignment for the TCMB029 , taught by Nikolay Milovanov at New Bulgarian University. The goal of this assignment is to demonstrate a comprehensive understanding of network simulations using Mininet, software-defined networking (SDN) with Floodlight, and Docker containerization technologies.

### Task Requirements:

- Install Docker and familiarize with it following the Docker curriculum.
- Understand Docker Compose and the ability to compose an application stack in containers.
- Learn about Mininet, a network simulator for prototyping a virtual network.
- Get acquainted with the SDN controller, Floodlight.
- Create a GitHub repository.
- Develop a Mininet Python script that creates a network topology with a specific number of switches and hosts, connected in a custom topology.
- Set up a Docker Compose environment containing Mininet and Floodlight along with your script.
- Demonstrate the configuration of bi-directional traffic rules between the two most distant hosts in your network using a script to the Floodlight API.
- Show that your script works by executing a ping test between the two hosts for which you have set up rules.



## Getting Started

### Prerequisites

Ensure that Docker and Docker Compose are installed on your machine. For installation instructions, visit [Docker's official site](https://docs.docker.com/get-docker/).

### Installation

1. Clone the repository to your local machine using:

   git clone https://github.com/yourusername/yourrepositoryname.git
   
2. Navigate into the project directory:

   cd yourrepositoryname

3. Start the Docker containers:

  docker-compose up -d

### Running the Network Simulation

1. Access the Mininet container. This step will open a bash shell inside the running Mininet container:

 docker exec -it mininet bash

2. Once inside the container, run the network script to initiate your custom topology:

 python /scripts/custom_topology.py
### YouTube video available at:
https://youtu.be/HseviOCYx_w
