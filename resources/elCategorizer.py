import json
file_path = 'resources/vocab.txt'


class Composition:
    def __init__(self,vocab):
        self.root=vocab
        self.compositions=[]





class Word:
    def __init__(self,vocab,definition=""):
        self.vocab = vocab
        self.definition = definition


def redundancies(list):
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    return new_list




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
    
    
    
    


