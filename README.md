# AWS Bill Scanner Project

## Overview

This project automatically extracts the total amount from bill images using AWS serverless services.

## Architecture

Bill Image Upload → Amazon S3 → AWS Lambda → Amazon Rekognition (OCR) → Extract Total Amount → Amazon DynamoDB

## AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon Rekognition
* Amazon DynamoDB
* Amazon CloudWatch

## Workflow

1. Upload a bill image to S3.
2. Lambda is triggered automatically.
3. Rekognition extracts text from the bill.
4. Python logic identifies the total amount.
5. Results are stored in DynamoDB.

## DynamoDB Record Example

| image_name | total_amount | upload_time |
| ---------- | ------------ | ----------- |
| bill1.jpg  | 450          | 2026-06-08  |

## Project Screenshots

### Architecture Diagram
### S3 Bucket
### Lambda Function
### DynamoDB Output
## Learning Outcomes

* Event-driven architecture
* OCR using Amazon Rekognition
* AWS Lambda automation
* DynamoDB integration
* Serverless application development

## Author

Sanika Pawar

