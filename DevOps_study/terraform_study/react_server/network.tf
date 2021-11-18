resource "aws_vpc" "main" {
  cidr_block       = "172.16.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "hitsweb"
  }
}


resource "aws_subnet" "main_subnet" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "172.16.10.0/24"
  availability_zone = "us-west-2a"

  tags = {
    Name = "hits_web"
  }
}

resource "aws_network_interface" "hitsweb" {
  subnet_id   = aws_subnet.main_subnet.id
  private_ips = ["172.16.10.100"]

  tags = {
    Name = "hitsweb_primary_network_interface"
  }
}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "TLS from VPC"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.main.cidr_block]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}
