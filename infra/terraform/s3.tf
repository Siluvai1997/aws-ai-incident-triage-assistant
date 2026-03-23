resource "aws_s3_bucket" "artifacts" {
  bucket_prefix = "${var.project_name}-"
  tags          = local.common_tags
}

resource "aws_s3_bucket_versioning" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id

  versioning_configuration {
    status = "Enabled"
  }
}
