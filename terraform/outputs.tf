output "instance_ip" {

  value = aws_instance.flask.public_ip

}

output "bucket_name" {

  value = aws_s3_bucket.backup.bucket

}