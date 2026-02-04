import json
file_path = 'resources/input/vocab.txt'
file2 = "resources/input/vocab2.txt"



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


"""
El testing twin
x=Word("stupidity")
y=Word("stupid")
if y.vocab in x.vocab:
    x.add_Composition(y)

print(x.compositions[0].vocab)
"""

obj_list=[]
def run(filep):
    try:
        with open(filep, 'r') as file:
            content = file.read()
            content = sorted(redundancies(content.splitlines()))
            new_list = [item for item in content if item != '']
            
            #List of Word instances generation
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


    except Exception as e:
        print(f"An error occurred: {e}")




run(file_path)
run(file2)

for x in obj_list:
    print(x.vocab)
    
#Need to implement redundancy functionality (if their are words in the new file that were already RAN from the initial file)
#Need to implement JSON implementation for nonvolatile storage saving 