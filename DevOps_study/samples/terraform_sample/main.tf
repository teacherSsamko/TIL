terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

variable "ec2_name" {
  type = string
}

provider "aws" {
  profile = "default"
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-03d5c68bab01f3496" // ubuntu 20.04 LTS
  instance_type = "t2.micro"

  tags = {
    Name = var.ec2_name
  }
}
