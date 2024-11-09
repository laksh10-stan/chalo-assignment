provider "aws" {
  region = var.region
}

resource "aws_instance" "primary" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "PrimaryPostgres"
  }
}

resource "aws_instance" "replicas" {
  count         = var.num_replicas
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "ReplicaPostgres"
  }
}

resource "aws_security_group" "postgres_sg" {
  name        = "postgres_sg"
  description = "Security group for PostgreSQL"

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
