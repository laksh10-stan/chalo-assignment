variable "region" {
  description = "The AWS region to deploy in."
  default     = "us-west-2"
}

variable "ami_id" {
  description = "The AMI ID to use for EC2 instances."
}

variable "instance_type" {
  description = "The EC2 instance type."
}

variable "num_replicas" {
  description = "Number of PostgreSQL replica instances."
  default     = 1
}
