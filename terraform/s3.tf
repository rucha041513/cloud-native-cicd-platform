# Backup Bucket
resource "aws_s3_bucket" "backup" {
  bucket = var.bucket_name
}

# Project Bucket
resource "aws_s3_bucket" "project_bucket" {
  bucket ="rucha-devops-project-213348783655"
}

# Enable Server-Side Encryption for Project Bucket
resource "aws_s3_bucket_server_side_encryption_configuration" "project_bucket_encryption" {

  bucket = aws_s3_bucket.project_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Enable Server-Side Encryption for Backup Bucket
resource "aws_s3_bucket_server_side_encryption_configuration" "backup_bucket_encryption" {

  bucket = aws_s3_bucket.backup.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}