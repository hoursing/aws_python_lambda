# AWS Image LAMBDA

Project is a lambda function that used lambda function with Container

# Technically
    - Python,  
    - AWS Lambda, ECR
    - Circle CI
    - Serverless.com

# AWS
    - Create a ECR report
    - Set permission AmazonEC2ContainerRegistryFullAccess for account or group

# Setting environment on Circle CI
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_REGION
    - AWS_ACCOUNT_ID
    - AWS_ECR_REGISTRY_ID

# Deploy
    User Circle to test function
    When Deploy, run circle CI, approve circle CI will deploy container