file_path = 'resources/vocab.txt'


"""
def redundantcies(list):
  temp=[]
  i=0
  length=len(list)
  while(i < length-1):
    if list[i] == list[i+1]:
      temp.append(list.pop(i))
    length=len(list)
    i+=1
  return temp
"""

def redundancies(lst):
    new_list = []
    for word in lst:
        if word not in new_list:
            new_list.append(word)
    return new_list



try:
    with open(file_path, 'r') as file:
        content = file.read()
        words = redundancies(content.splitlines())
        words = sorted(words)
        new_list = [item for item in words if item != '']
        print(new_list)
        
        
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
    


