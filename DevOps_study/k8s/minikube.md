# Minikube

## Overview

Minikube is a tool for running Kubernetes in a VM. It is a single-node Kubernetes cluster that runs in a VM.

## How to pull ECR Image in minikube

To pull ECR Image in minikube, you need:

- addons:
  - registry-creds:
    - server: \<your-ecr-server>
    - username: \<your-ecr-username>
    - password: \<your-ecr-password>

- deployment.yaml

    ```yaml
    ...
    spec:
        template:
            spec:
            containers:
            - name: my-container
                image: ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/ECR_REPO:latest
            imagePullSecrets:
            - name: awsecr-cred
    ```
