from datetime import datetime


class word:
    def __init__(self,type,word,definition,example):
        self.word=word
        self.definition=definition

class Deck:
    def __init__(self,elements,desc):
        self.time=datetime.now()
        self.description=desc
        self.elements=elements
        self.length=len(self.elements)
        self.editHistory=[]
    
    #Helper function to develop edit history
    def updateHistory(self,change,elements):
        edit=(datetime.now(),change,elements)
        self.editHistory.append(edit)

    #Takes a list of words that should be added to a deck and adds them
    def addWords(self,elements):
        self.elements.extend(elements)
        self.updateHistory("addition",elements)
        
    
    #Takes a list of words that should be removed from a deck and removes them (should be safe if list of words to remove contains words unused in the original list) 
    def removeWords(self,elements):
        self.elements=[item for item in self.elements if item not in elements]
        self.updateHistory("deletion",elements)










