class History(object):
    def __init__(self):
        self.command = []
        self.pos = 0
        self.saved = [[]]*100

    def addToHistory(self,command):
        self.command = command
        
        if self.pos < 100:
            self.saved[self.pos]= self.command
            self.pos +=1
        else:
            print('history is reseted')
            self.command = []
            self.pos = 0
            self.saved = [[]]*100
            
    def getPreviousCmmd(self):
        self.addToHistory(self.saved[self.pos-2])
        return self.saved[self.pos-1]

    def getNext(self):
        if self.pos < 100 :
            if self.saved[self.pos] == []:
                self.addToHistory(self.saved[0])
            return self.saved[self.pos-1] 

    def clearHistory(self):
        self.command = []
        self.pos = 0
        self.saved = [[]]*100

if __name__=="__main__" :
    '''
    debugging
    h =History()
    h.addToHistory('cd')
    h.addToHistory('ls')
    h.addToHistory('ss')
    hh = h.getNext()
    hhh = h.getPreviousCmmd()
    print(hh)
    print(h.saved)

    print(h.pos)
    '''  




    
        