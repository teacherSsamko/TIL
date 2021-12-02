# Continuous Integration & Continuous Delivery

## CD

### Architecture

- IaC repository
- App repository
- When App repository is changed, IaC repository's github actions is triggered.

### IaC repository

- Create AMI using Packer
- Use Ansible for provisiong Packer AMI
- Using terraform to deploy new Packer AMI
