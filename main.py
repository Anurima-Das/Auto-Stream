import json
import boto3

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    # Example: write data to S3
    s3 = boto3.client('s3')
    bucket = "event-data-bucket-anurima"  # replace with your bucket name
    
    for record in event['Records']:
        body = record['body']
        s3.put_object(
            Bucket=bucket,
            Key=f"events/{record['messageId']}.json",
            Body=body
        )
    
    return {"statusCode": 200, "body": "Data processed"}
