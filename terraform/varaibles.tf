variable "aws_region" {
  default = "eu-north-1"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "bucket_name" {
  description = "Unique S3 bucket name"
}
variable "db_password" {
  type = string

  sensitive = true
}