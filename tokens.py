class Parsing(object):

    specialCharacters = ['>', '<','|','*']

    def __init__(self,text):
        self.line = text
        self.commandsArgument = []
        self.specialChar = 0
        self.commands = ''
        self.arg = []

    def tokens(self):
        self.commandsArgument = self.line.split()
        self._seperateCommandsArgs()
        self.getCommandsArgsExc()
  
   

    def _seperateCommandsArgs(self):
        self.commands= self.commandsArgument[0]
        self.arg =self.commandsArgument[1:]

    def excutable(self):
        if self.commands[0]== '.' and self.commands[1] == '/':
            return False 
        else : 
            return True 

    def specialChars (self):
        for word in self.commandsArgument:
            if word in self.specialCharacters:
                return True , word  
        else: 
            return False 

    def getCommandsArgsExc(self):
        return  self.excutable(), self.commands , self.arg













if __name__=="__main__" :
    '''
    debugging 
    text = 'cd ..'

    par = Parsing(text)
    par.tokens()
    
    x,c,r = par.getCommandsArgsExc()
    print(str(x)+' '+str(c)+' '+str(r))
    ss = par.specialChars()
    print(str(ss))
    '''
   
