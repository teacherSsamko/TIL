resource "aws_instance" "app_server" {
  ami           = "ami-03d5c68bab01f3496" // ubuntu 20.04 LTS
  instance_type = "t2.micro"

  tags = {
    Name = var.ec2_name
  }
}