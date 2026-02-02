import json
file_path = 'resources/vocab.txt'



        

class Word:
    def __init__(self,word,definition=""):
        self.vocab = word
        self.definition = definition
        
    compositions = [[],[]]
    #First list contains the OBJECTS of the composed words and the second list contains the STRINGS of the composed words
    
    def add_Composition(self,vocab):
        self.compositions[0].append(vocab)
        self.compositions[1].append(vocab.word)


def redundancies(list):
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    return new_list





x=Word("stupidity")
y=Word("stupid")

x.add_Composition(y)

print(x.compositions[1])





"""
try:
    with open(file_path, 'r') as file:
        content = file.read()
        content = sorted(redundancies(content.splitlines()))
        new_list = [item for item in content if item != '']
        obj_list=[]
        i=0
        while(len(new_list)>i):
            obj_list.append(Word(new_list[i]))
            i+=1
        
        for word in obj_list:
            print(word.vocab)
except Exception as e:
    print(f"An error occurred: {e}")
"""
    
    
    


