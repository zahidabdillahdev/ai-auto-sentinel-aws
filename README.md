# AI Auto-Sentinel AWS 🛡️

An automated, serverless image recognition system built on AWS. This project integrates Cloud Storage, Event-Driven Functions, and AI to analyze and log object detection data in real-time.



## 🏗️ Architecture
1. **S3 Bucket**: Stores raw images.
2. **S3 Trigger**: Detects new uploads and pokes AWS Lambda.
3. **AWS Lambda**: The "Brain" that runs Python code on-demand.
4. **Amazon Rekognition**: The "Eye" (AI) that identifies objects.
5. **DynamoDB**: The "Memory" (Database) that stores analysis history.

## 🚀 Features
- **Serverless Automation**: No manual script execution required after setup.
- **AI-Powered**: High-confidence object detection using Amazon Rekognition.
- **Data Persistence**: Analysis results are stored permanently in DynamoDB.
- **Infrastructure as Code (IaC)**: Provisioning scripts included for S3.

## 📋 Tech Stack
- **Language**: Python 3.12
- **Infrastructure**: AWS (S3, Lambda, DynamoDB, IAM)
- **AI Service**: Amazon Rekognition
- **SDK**: Boto3

## 🛠️ Components
- `connection_test.py`: Initial connectivity check.
- `create_resources.py`: Automated S3 bucket creation.
- `analyze_image.py`: Manual testing script for AI analysis.
- `lambda_function.py`: Production-grade serverless code for AWS Lambda.

## ⚙️ How It Works
1. Upload an image to your S3 bucket.
2. The S3 Trigger automatically fires the `lambda_function`.
3. The function sends the image to Rekognition and receives labels.
4. The results are saved into a DynamoDB table named `sentinel-analysis-metadata`.

## 📸 Testing with Your Own Image
Simply drag and drop any `.jpg` or `.png` file into your S3 bucket via the AWS Console, then check your DynamoDB table for the results!

## 📝 License
MIT License