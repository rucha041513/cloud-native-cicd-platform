resource "aws_instance" "flask" {

  ami = "ami-0402e980e69d5978b"

  instance_type = var.instance_type

  subnet_id = aws_subnet.public.id

  vpc_security_group_ids = [
    aws_security_group.web.id
  ]

  tags = {

    Name = "Flask-Server"

  }

}