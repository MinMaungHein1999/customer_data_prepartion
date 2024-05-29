from downloader_factory import DownloaderFactory
from file_manager import FileManager
import boto3
import zipfile
import os
import logging
import json
logging.basicConfig(level=logging.INFO)

class S3Downloader(DownloaderFactory):

    def __init__(self, bucket, region_name, temp_path):
        self.bucket = bucket
        self.s3_client = boto3.client('s3')
        self.temp_path = temp_path
        self.region_name = region_name

    def download_file_from_s3(self):

        s3 = self.s3_client

        response = s3.list_objects_v2(Bucket=self.bucket, Prefix='', Delimiter='/')

        file_contents = response.get('Contents', [])[:1]
        print(f'Listed files: {len(file_contents)}')

        gzip_files = [file_object for file_object in file_contents if file_object.get('Key', '').endswith('.zip')]

        file_urls = self.extract_file_from_s3(gzip_files)
        
        return file_urls

    def extract_file_from_s3(self, gzip_files):
        s3 = self.s3_client
        bucket = self.bucket
        temp_dir = self.temp_path
        os.makedirs(temp_dir, exist_ok=True)
        csv_files_urls = []

        for file_object in gzip_files:
            file_name = os.path.basename(file_object['Key'])
            print(f'File name is {file_name}.')

            key = file_object['Key']
            gzipped_file_path = os.path.join(temp_dir, file_name)
            s3.download_file(bucket, key, gzipped_file_path)

            with zipfile.ZipFile(gzipped_file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            extracted_files_urls = self.upload_extracted_files_to_s3(temp_dir, "csv_files")
            csv_files_urls.extend(extracted_files_urls)

        return csv_files_urls

    def upload_extracted_files_to_s3(self, directory, original_key_prefix):
        s3 = self.s3_client
        bucket = self.bucket
        s3_urls = []

        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.lower().endswith(".csv"):
                    file_path = os.path.join(root, file_name)
                    s3_key = os.path.join(original_key_prefix, file_name).replace('\\', '/')
                    s3_url = f"s3://{bucket}/{s3_key}"
                    
                    print(f'Uploading {file_path} to {s3_url}')
                    s3.upload_file(file_path, bucket, s3_key)
                    s3_obj = {
                        "file_name": file_name,
                        "s3_url": s3_url
                    }
                    s3_urls.append(s3_obj)

        print(f'Successfully uploaded files : {s3_urls}')
        return s3_urls
        