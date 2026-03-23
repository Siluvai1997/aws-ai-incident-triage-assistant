# AWS AI Incident Triage Assistant

An AWS-native AI application that analyzes incidents, classifies severity and category, and recommends runbook actions to accelerate operational triage.

## Overview

AWS AI Incident Triage Assistant is a portfolio project that demonstrates how generative AI and serverless AWS services can support faster operational triage. The application accepts incident alerts, support tickets, or log snippets, then produces a concise summary, assigns a severity and category, identifies the likely impacted component, and maps the issue to a runbook.

This repository is designed as a **completed MVP** that can be run locally and deployed to AWS for testing. The architecture is intentionally cost-conscious:

- Frontend runs locally with Streamlit
- Backend uses AWS Lambda for serverless inference orchestration
- Amazon Bedrock performs summarization and classification
- Amazon S3 stores sample incidents and deployment artifacts
- CloudWatch captures backend logs
- Terraform provisions reproducible infrastructure

After deployment and testing, AWS resources can be deleted to avoid ongoing cost.

## Problem Statement

Operational teams often lose time manually reviewing alerts, log fragments, and incident descriptions before deciding:

- How severe is this issue?
- What category does it belong to?
- Which component is likely impacted?
- What runbook should be followed first?

This project demonstrates a lightweight AI-assisted workflow that reduces the manual triage burden and provides faster first-response guidance.

## Features

- Paste incident text or load a sample incident
- Generate an AI-assisted incident summary
- Classify severity: Critical / High / Medium / Low
- Classify category: Infrastructure / Networking / Kubernetes / CI-CD / Authentication / Application outage
- Identify likely impacted component
- Recommend runbook steps based on the classified category
- View sample incident library and runbook mappings
- Run locally with a mock mode or a real Amazon Bedrock call
- Deploy backend resources to AWS with Terraform

## Architecture

1. User submits incident text from the Streamlit UI
2. Streamlit calls the backend triage service
3. Triage service sends the incident prompt to Amazon Bedrock
4. The model returns structured triage output
5. Backend maps the category to runbook actions from local JSON or S3
6. Results are displayed in the UI
7. Lambda execution logs are captured in CloudWatch

### AWS Services Used

- **Amazon Bedrock** – incident summarization and classification
- **AWS Lambda** – serverless backend orchestration
- **Amazon S3** – sample incidents and deployment artifacts
- **Amazon CloudWatch** – logs and troubleshooting
- **Terraform** – infrastructure as code
- **GitHub Actions** – linting and validation workflows

## Repository Structure

```text
aws-ai-incident-triage-assistant/
├── app/
│   ├── Home.py
│   ├── pages/
│   └── utils/
├── backend/
├── data/
│   ├── sample_incidents/
│   └── runbooks/
├── infra/
│   └── terraform/
├── tests/
├── .github/
│   └── workflows/
├── docs/
├── Dockerfile
├── requirements.txt
└── README.md
```

## Current Status

**MVP completed.**

This repository includes:

- working Streamlit frontend scaffold
- backend triage service with mock mode and Bedrock integration points
- sample incident dataset
- runbook mapping logic
- Lambda handler
- Terraform starter files for AWS deployment
- GitHub Actions CI and Terraform validation workflows
- architecture notes

Recommended usage for a portfolio:

- run locally for demo purposes
- deploy to AWS for validation and screenshots
- delete resources afterward to avoid ongoing charges

## Local Setup

### Prerequisites

- Python 3.11+
- pip
- virtual environment tool
- AWS CLI configured only if you want to test Bedrock or deploy to AWS

### Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run locally in mock mode

```bash
export TRIAGE_MODE=mock
streamlit run app/Home.py
```

### Run locally with Bedrock mode

```bash
export TRIAGE_MODE=bedrock
export AWS_REGION=us-east-1
streamlit run app/Home.py
```

> Make sure your AWS credentials and Bedrock model access are configured before using Bedrock mode.

## AWS Deployment

### Suggested low-cost deployment pattern

- Keep the Streamlit frontend local
- Deploy only the backend AWS resources
- Test with 5–10 sample incidents
- Capture screenshots and logs
- Delete resources after validation

### Terraform deployment steps

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

### What gets created

- S3 bucket
- IAM role and policy for Lambda
- Lambda function
- CloudWatch log group

## Cost Control and Cleanup

To keep cost low:

- use a small number of Bedrock test calls
- keep CloudWatch logging minimal
- avoid always-on frontend hosting in AWS
- avoid extra managed services in the MVP
- delete resources after testing

### Cleanup

```bash
cd infra/terraform
terraform destroy
```

Also delete any test objects from S3 if needed.

## Sample Incident Flow

1. Open the Streamlit app
2. Load a sample incident from the sidebar
3. Review the incident details
4. Click **Run Triage**
5. Review summary, severity, category, impacted component, and runbook steps

## Limitations

- MVP uses sample incidents rather than live integrations
- Bedrock output depends on prompt quality and model selection
- Runbook retrieval is category-based in v1 and not semantic
- Streamlit frontend is intended for demo

## Future Enhancements

- Add API Gateway for a public backend endpoint
- Add semantic runbook retrieval with embeddings
- Integrate with PagerDuty or ServiceNow test payloads
- Add incident history storage in DynamoDB
- Add automated evaluation against labeled incident samples

## License

This project is provided for portfolio and educational use.
