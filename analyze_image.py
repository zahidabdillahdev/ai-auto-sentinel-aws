import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def upload_and_detect(bucket_name, image_path, region='ap-southeast-1'):
    """
    Uploads an image to S3 and uses Amazon Rekognition to detect labels (objects).
    """
    s3_client = boto3.client('s3', region_name=region)
    rekognition_client = boto3.client('rekognition', region_name=region)
    
    file_name = image_path.split('/')[-1]

    try:
        # Step 1: Upload image to S3
        logging.info(f"Uploading {file_name} to bucket {bucket_name}...")
        s3_client.upload_file(image_path, bucket_name, file_name)
        logging.info("Upload successful!")

        # Step 2: Call Amazon Rekognition
        logging.info("Analyzing image using Amazon Rekognition...")
        response = rekognition_client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': file_name
                }
            },
            MaxLabels=10,
            MinConfidence=75 # Only show results with 75% confidence or higher
        )

        # Step 3: Print AI Results
        print("\n--- [AI ANALYSIS RESULTS] ---")
        for label in response['Labels']:
            print(f"Detected: {label['Name']} | Confidence: {label['Confidence']:.2f}%")
            
    except Exception as e:
        logging.error(f"Error during AI analysis: {e}")

if __name__ == "__main__":
    # Use the bucket name you created earlier
    TARGET_BUCKET = "sentinel-raw-images-zahid-2026"
    IMAGE_TO_ANALYZE = "test-image.jpg"
    
    upload_and_detect(TARGET_BUCKET, IMAGE_TO_ANALYZE)