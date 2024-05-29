import json
import os
from upload_file_to_s3 import UploadFileToS3
from botocore.exceptions import ClientError
from datetime import datetime

def lambda_handler(event, context):
    env = event['env']
    bucket = os.environ['BUCKET']
    temp_path = os.environ['TEMP_PATH']
    table_name = env +"_"+ os.environ['PN2_CUST_DATA_TABLE']
    region_name = os.environ['REGION_NAME']

    try:
        
        upload_file_to_s3 = UploadFileToS3(bucket, temp_path, table_name, region_name)
        upload_file_to_s3.call()
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully imported PN2 Customer Data from S3 into DynamoDb')
        }
            
    except ClientError as e:
        
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error occurred while importing : {e}')
        }
 

