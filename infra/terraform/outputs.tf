output "s3_bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.triage.function_name
}

output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.lambda.name
}
