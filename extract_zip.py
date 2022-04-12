import zipfile

class ExtractZip:
    def __init__(self,path_to_zip_file,directory_extract):
        self.path_to_zip_file = path_to_zip_file
        self.directory_extract = directory_extract
        
    def extractZip(self):
        with zipfile.ZipFile(self.path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(self.directory_extract)