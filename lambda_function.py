import json
import boto3
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    rekognition_client = boto3.client('rekognition')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('sentinel-analysis-metadata')
    
    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # 1. AI Analysis
        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': bucket_name, 'Name': file_key}},
            MaxLabels=5, MinConfidence=80
        )
        
        labels = [label['Name'] for label in response['Labels']]
        
        # 2. Prepare Data for Database
        item = {
            'image_id': file_key,
            'timestamp': str(time.time()),
            'labels': labels,
            'bucket': bucket_name,
            'status': 'PROCESSED'
        }
        
        # 3. Save to DynamoDB
        table.put_item(Item=item)
        logger.info(f"Successfully saved {file_key} analysis to DynamoDB")
        
        return {'statusCode': 200, 'body': json.dumps(item)}
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return {'statusCode': 500}