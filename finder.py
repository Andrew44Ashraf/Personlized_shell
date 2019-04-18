import sys
import os

class Finder():
    def get_paths(self):
        print(os.environ['PATH'])
        return os.environ['PATH'].split(":")
    def search_path(self,cmnd):
        lst = self.get_paths()
        for d in lst:
            for dirName, subdirList, fileList in os.walk(d):
                for fname in fileList:
                    if(fname == cmnd):
                        return dirName+'/'+fname
        return None