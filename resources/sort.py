import json
file_path = 'resources/vocab.txt'


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
        words = redundancies(content.splitlines())
        words = sorted(words)
        new_list = [item for item in words if item != '']
        obj_list=[]
        i=0
        while(len(new_list)>i):
          obj_list.append(Word(new_list[i]))
          i+=1
          
        
        
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
    


