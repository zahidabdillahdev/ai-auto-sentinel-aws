import boto3
import logging

# Configure logging to track the resource creation process
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def create_s3_bucket(bucket_name, region='ap-southeast-1'):
    """
    Automates the creation of an S3 bucket in the Singapore region.
    This bucket will store the images for AI analysis.
    """
    try:
        # Create an S3 client
        s3_client = boto3.client('s3', region_name=region)
        
        # Configuration needed for regions outside of US-East-1 (N. Virginia)
        location = {'LocationConstraint': region}
        
        logging.info(f"Attempting to create bucket: {bucket_name}...")
        
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration=location
        )
        
        logging.info(f"Success! Bucket '{bucket_name}' is now active in {region}.")
        
    except Exception as e:
        logging.error(f"Failed to create bucket: {e}")

if __name__ == "__main__":
    # IMPORTANT: S3 bucket names must be globally unique.
    # I recommend using 'sentinel-raw-[yourname]-[random-numbers]'
    # Change the name below to be unique to your account.
    UNIQUE_BUCKET_NAME = "sentinel-raw-images-zahid-2026" 
    
    create_s3_bucket(UNIQUE_BUCKET_NAME)