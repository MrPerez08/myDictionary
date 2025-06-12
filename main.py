#open text documents
vocabtext=open("vocab.txt","r")
definitionstext=open("definitions.txt","r")

#turn the text documents into lists with each element corresponding to a vocab word
vocab = vocabtext.readlines()
definitions=definitionstext.readlines()


deck=""

