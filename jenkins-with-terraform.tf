provider "aws" {
  region = "us-west-2"
}

resource "aws_key_pair" "jenkins_key" {
  key_name   = "jenkins_key"
  public_key = file("~/.ssh/jenkins_key.pub")
}

resource "aws_security_group" "jenkins" {
  name        			= "jenkins_sg"
  description 			= "Jenkins Security Group"

  ingress {
    from_port   		= 22
    to_port     		= 22
    protocol    		= "tcp"
    cidr_blocks 		= ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   		= 8080
    to_port     		= 8080
    protocol    		= "tcp"
    cidr_blocks 		= ["0.0.0.0/0"]
  }
}

resource "aws_instance" "jenkins" {
  ami           			= "ami-0ff8a91507f77f867"
  instance_type 			= "t2.micro"
  key_name      			= aws_key_pair.jenkins_key.key_name
  vpc_security_group_ids 	= [aws_security_group.jenkins.id]

  # Add Jenkins user-data script to install and configure Jenkins
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y java-1.8.0-openjdk-devel
              wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
              rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
              yum install -y jenkins
              systemctl start jenkins
              systemctl enable jenkins
              EOF
  
  # Launching the instance
  provisioner "remote-exec" {
    inline = [
      "sleep 30",
      "curl http://localhost:8080"
    ]
  }
}
