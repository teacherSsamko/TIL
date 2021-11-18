resource "aws_instance" "app_server" {
  ami           = var.ami_ubuntu
  instance_type = "t3.medium"

  tags = {
    Name = var.ec2_name
  }

  user_data = <<EOF
		#! /bin/bash
    sudo apt-get update
		sudo apt-get install -y nginx npm
		sudo systemctl start nginx
		sudo systemctl enable nginx
	EOF

  network_interface {
    network_interface_id = aws_network_interface.hitsweb.id
    device_index         = 0
  }

}
