provider "aws" {
  profile = "default"
  region = "us-east-1"
}
resource "aws_instance" "ec2_test" {
  ami = "ami-b374d5a5"
  instance_type = "t2.micro"
}
