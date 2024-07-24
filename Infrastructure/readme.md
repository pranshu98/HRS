
# Terraform AWS Infrastructure for Java Microservices

## Overview

This project sets up a basic AWS infrastructure using Terraform to deploy Java-based microservices. The setup is designed to be repeatable and scalable, enabling easy deployment of new services.

## Why Terraform?

- Declarative Syntax: Simplifies defining infrastructure.
- Version Control: Facilitates collaboration and change tracking.
- Provider Support: Supports multiple cloud providers.
- State Management: Ensures consistent and predictable infrastructure provisioning.

## Infrastructure Components

### VPC and Networking

- VPC: Provides network isolation.
- Subnet: Public subnet for hosting services.
- Internet Gateway: Enables internet access for resources in the public subnet.

### ECS Cluster

- ECS Cluster: Manages Docker containers for running microservices.
- IAM Roles: Provides necessary permissions for ECS tasks.

### ECS Service and Task Definition

- Task Definition: Defines the Docker container and its configuration.
- ECS Service: Manages the deployment and scaling of the tasks.

### Security Group

- Security Group: Controls inbound and outbound traffic to the ECS tasks.

## Deployment Steps

1. Initialize Terraform:
    terraform init


2. Plan the Infrastructure:
    
    terraform plan
    

3. Apply the Configuration:
    
    terraform apply
    

This setup uses AWS free tier resources to avoid incurring costs.
