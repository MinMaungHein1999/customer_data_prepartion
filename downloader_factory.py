from abc import ABC, abstractmethod

class DownloaderFactory(ABC):
    @abstractmethod
    def download_file_from_s3(self):
        pass