variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix for AWS resources"
  type        = string
  default     = "aws-ai-incident-triage-assistant"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  type        = string
  default     = "incident-triage-handler"
}

variable "bedrock_model_id" {
  description = "Bedrock model identifier"
  type        = string
  default     = "amazon.nova-lite-v1:0"
}
