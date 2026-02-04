import json
file_path = 'resources/vocab.txt'



        

class Word:
    def __init__(self,word,definition=""):
        self.vocab = word
        self.definition = definition
        self.compositions = []  # ← Make it an INSTANCE variable!
    #First list contains the OBJECTS of the composed words and the second list contains the STRINGS of the composed words
    #Is it necessary to contain that second list? no
    
    def add_Composition(self,vocab):
        self.compositions.append(vocab)


def redundancies(list):
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    return new_list



#El testing twin
x=Word("stupidity")
y=Word("stupid")
if y.vocab in x.vocab:
    x.add_Composition(y)

#print(x.compositions[0].vocab)



try:
    with open(file_path, 'r') as file:
        content = file.read()
        content = sorted(redundancies(content.splitlines()))
        new_list = [item for item in content if item != '']
        
        #List of Word instances generation
        obj_list=[]
        i=0
        while(len(new_list)>i):
            obj_list.append(Word(new_list[i]))
            i+=1
        
        i=0
        #Checking for word compositions
        while(len(new_list)>i):
            t=1
            while(len(new_list)>t):
                if(obj_list[t].vocab in obj_list[i].vocab):
                    obj_list[i].add_Composition(obj_list[t])
                t+=1
            i+=1
            
        for word in obj_list:
            print(word.vocab)
            
        
except Exception as e:
    print(f"An error occurred: {e}")

    
    
    


