import json


#open text documents
vocabtext=open("vocab.txt","r")
definitionstext=open("simpledefinitions.txt","r")

#turn the text documents into lists with each element corresponding to a vocab word
vocab = vocabtext.readlines()
definitions=definitionstext.readlines()

for i in range (len(vocab)):
    vocab[i]=vocab[i].replace("\n","")
    definitions[i]=definitions[i].replace("\n","")


#Create a dict that allows each word to 'contain' its vocabulary
dictionary = {v: d for v, d in zip(vocab,definitions)}


#Easily prints specific elements from the dict to allows for the simple copy paste of information into Quizlets import cards feature
keys=list(dictionary.keys())
values=list(dictionary.values())
string=""

for i in range (len(dictionary)):
    string+=keys[i]+"="+values[i]+"+"

print(string)

jsonString=json.dumps(string)

with open("deck.json", 'w') as f:
    f.write(jsonString)




#Save to a json




#Add a GUI which allows for a quick import of vocabulary words (allows drag and drop text documents)



#Ability to save dictionary in a document (i dont know what kind of file type it should be??) so it can be reopened



'''We need to make sure that the user doesnt create a copy of the same vocabulary word, write script to remove redundancies 
(ALSO CONSIDER: if the user is adding a word that he/she/they dont understand again, that means compared to other words in their present dictionary, 
they have a harder time understanding that specific word) 
(To add this functionality, propose a counter system that dictates the number of times the user imports the same word?)
'''


#Utilize Gemini API to generate definitions based off of an imported vocabulary list

