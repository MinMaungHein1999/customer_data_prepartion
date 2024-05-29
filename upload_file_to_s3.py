from s3_downloader import S3Downloader
from pn2_customer_table_creator import Pn2CustomerTableCreator
from file_manager import FileManager

class UploadFileToS3:
    def __init__(self, bucket, temp_path, table_name, region_name):
        self.pn2_customer_table_creator = Pn2CustomerTableCreator(table_name, region_name)
        self.s3_downloader = S3Downloader(bucket, region_name, temp_path)
        self.file_manager = FileManager(temp_path, region_name, table_name, bucket)

    def call(self):
        self.pn2_customer_table_creator.create_table()
        file_urls = self.s3_downloader.download_file_from_s3()
        self.file_manager.move_files_to_dynamodb(file_urls)