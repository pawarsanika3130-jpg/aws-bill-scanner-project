import json
import boto3
import re
from datetime import datetime

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('invoicetable')   # Change if your table name is different

def lambda_handler(event, context):

    try:
        # Get S3 details
        bucket = event['Records'][0]['s3']['bucket']['name']
        image_name = event['Records'][0]['s3']['object']['key']

        print(f"Processing image: {image_name}")

        # Detect text from image
        response = rekognition.detect_text(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': image_name
                }
            }
        )

        # Extract all detected lines
        text = ""

        for item in response['TextDetections']:
            if item['Type'] == 'LINE':
                text += item['DetectedText'] + "\n"

        print("===== DETECTED TEXT =====")
        print(text)

        # Find all numbers in bill
        amounts = []

        numbers = re.findall(r'\d+(?:\.\d{1,2})?', text)

        for num in numbers:
            try:
                amounts.append(float(num))
            except:
                pass

        # Choose largest value as total amount
        if amounts:
            total_amount = str(max(amounts))
        else:
            total_amount = "Not Found"

        print("Detected Amounts:", amounts)
        print("Final Total Amount:", total_amount)

        # Save to DynamoDB
        table.put_item(
            Item={
                "image_name": image_name,
                "total_amount": total_amount,
                "upload_time": datetime.now().isoformat()
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Bill processed successfully",
                "image_name": image_name,
                "total_amount": total_amount
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
