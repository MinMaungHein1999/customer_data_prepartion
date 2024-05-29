import boto3
import logging
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FileManager:
    def __init__(self, file_path, region_name, table_name, bucket):
        self.file_path = file_path
        self.region_name = region_name
        self.table_name = table_name
        self.bucket = bucket

    def move_files_to_dynamodb(self, file_urls):
        self.file_to_save_db(file_urls)

    def file_to_save_db(self, file_urls):
        client = boto3.client('lambda', region_name=self.region_name)

        function_name = 'pn2_customer_to_db'

        for data in file_urls:
            payload = {
                "table_name": self.table_name,
                "region_name": self.region_name,
                "bucket": self.bucket,
                "body": {
                    "csv_file_path": data["s3_url"],
                    "file_name": data["file_name"]
                }
            }
            print("Calling Lambda function 'pn2_customer_to_db' asynchronously")
            print(f"Payload body: {json.dumps(payload)}")

            try:
                response = client.invoke(
                    FunctionName=function_name,
                    InvocationType='Event',
                    Payload=json.dumps(payload)
                )
                print(f"Invocation request sent for 'pn2_customer_to_db': {response}")
            except Exception as e:
                print(f"Error calling Lambda function: {e}")
