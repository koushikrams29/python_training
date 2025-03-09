import os
from datetime import datetime

class File:
    def __init__(self,dir):
        self.dir=dir

    def getMaxsizeFiles(self,n):
        files=[(f,os.path.getsize(os.path.join(self.dir,f)))
               for f in os.listdir(self.dir)if os.path.isfile(os.path.join(self.dir,f))]
        files.sort(key=lambda x:x[1],reverse=True)
        return [file[0]for file in files[:n]]
    
    def getLatestFiles(self,date):
        result=[]
        for f in os.listdir(self.dir):
            file_path=os.path.join(self.dir,f)
            if os.path.isfile(file_path):
                time=datetime.fromtimestamp(os.path.getmtime(file_path)).date()
                if time>date:
                    result.append(f)
        return result