data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/../.."
  output_path = "${path.module}/lambda_function.zip"
}

resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${var.lambda_function_name}"
  retention_in_days = 7
  tags              = local.common_tags
}

resource "aws_lambda_function" "triage" {
  function_name = var.lambda_function_name
  role          = aws_iam_role.lambda_role.arn
  handler       = "backend.lambda_handler.handler"
  runtime       = "python3.11"
  timeout       = 30
  memory_size   = 256

  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  environment {
    variables = {
      TRIAGE_MODE       = "bedrock"
      AWS_REGION        = var.aws_region
      BEDROCK_MODEL_ID  = var.bedrock_model_id
    }
  }

  depends_on = [aws_cloudwatch_log_group.lambda]
  tags       = local.common_tags
}
