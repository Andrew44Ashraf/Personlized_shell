import os
import finder
class Executer():
    def __init__(self):
        self.finder = finder.Finder()
    def exec_command(self,cmnd):
        pid = os.fork()
        if(pid == 0):
            if(cmnd[0] == True):
                path = self.finder.search_path(cmnd[1])
                if(path == None):
                    print("Not Found")
                else:
                    os.execv(path,cmnd[2])
            else:
                os.execv(cmnd[0],cmnd[2])

            

