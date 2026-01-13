# ai-auto-sentinel-aws
Automated image recognition and notification system built with AWS Lambda, Amazon Rekognition, and S3 using Python.

# AI Auto-Sentinel AWS 🛡️

An automated image recognition system built on AWS using Python. This project demonstrates how to integrate Cloud Infrastructure (S3) with Artificial Intelligence (Amazon Rekognition) to analyze images and detect objects with high confidence scores.

## 🚀 Features
- **Cloud Connectivity**: Validates secure programmatic access to AWS Singapore region.
- **Infrastructure as Code (IaC)**: Automated S3 bucket provisioning using Boto3.
- **AI Analysis**: Real-time object and label detection using Amazon Rekognition.
- **Professional Logging**: Integrated Python logging for monitoring and debugging.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **SDK**: Boto3 (AWS SDK for Python)
- **Cloud Provider**: AWS (S3, Rekognition, IAM)
- **Environment**: GitHub Codespaces / VS Code

## 📋 Prerequisites
1. **AWS Account**: Active AWS account with an IAM User.
2. **IAM Permissions**: `AdministratorAccess` or specific permissions for S3 and Rekognition.
3. **AWS CLI**: Installed and configured via `aws configure`.

## ⚙️ Installation & Setup
1. **Clone this repository**:
   git clone [https://github.com/zahidabdillahdev/ai-auto-sentinel-aws.git](https://github.com/zahidabdillahdev/ai-auto-sentinel-aws.git)
   cd ai-auto-sentinel-aws

2. **Install dependencies**:
pip install boto3

3. **Configure your AWS credentials**:
aws configure

## 🖥️ Usage
Execute the scripts in the following order:
1. **Test Connection**: Ensure your environment can talk to AWS.
python connection_test.py

2. **Create Resources**: Provision your dedicated S3 bucket.
python create_resources.py

3. **Analyze Image**: Upload and analyze your first image.
python analyze_image.py

## 📸 How to Test with Your Own Image
You can test the AI with any image you like!

1. **Upload your image**: Drag and drop your image (JPG/PNG) into the project folder in VS Code.
2. **Rename the file**: Rename it to my-test-image.jpg.
3. **Update the script**: Open analyze_image.py and change the IMAGE_TO_ANALYZE variable:
IMAGE_TO_ANALYZE = "my-test-image.jpg"
4. **Run the analysis**:
python analyze_image.py

## 📝 License
This project is licensed under the MIT License.