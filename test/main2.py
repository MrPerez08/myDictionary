from compartmentalizer import *

#open text documents
vocabtext=open("vocab.txt","r")
definitionstext=open("simpledefinitions.txt","r")

#turn the text documents into lists with each element corresponding to a vocab word
vocab = vocabtext.readlines()
definitions=definitionstext.readlines()

bigContainer=[]
for i in range(len(vocab)):
    bigContainer.append(word(vocab[i],definitions[i]))








