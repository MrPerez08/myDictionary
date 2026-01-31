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

def redundancies(list):
  originallist=list
  current=list[0]
  new_list=[]
  while(len(list)>0):
    i=0
    while(i<len(originallist)):
      
      if (current == list[i+1]):
        list.pop(i+1)
        
    new_list.append(current)
    i+=1
    
    print(i)
    
  return new_list



try:
    with open(file_path, 'r') as file:
        content = file.read()
        words = redundancies(content.splitlines())
        words = sorted(words)
        print(words)
        new_list = [item for item in words if item != '']
        #print(new_list)
        
        
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
    


