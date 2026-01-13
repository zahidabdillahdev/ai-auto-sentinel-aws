import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def test_aws_connection():
    """
    Validates the connection between GitHub Codespaces and AWS Singapore.
    It lists all available S3 buckets in the account.
    """
    try:
        # Initializing the S3 client
        s3 = boto3.client('s3')
        
        # Fetching the list of buckets
        response = s3.list_buckets()
        
        print("--- [SUCCESS] AWS Connectivity Established ---")
        print(f"Buckets found: {len(response['Buckets'])}")
        
        for bucket in response['Buckets']:
            print(f" -> {bucket['Name']}")
            
    except (NoCredentialsError, PartialCredentialsError):
        print("[ERROR] AWS Credentials not found. Please run 'aws configure'.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_aws_connection()