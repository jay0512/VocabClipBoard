import pyperclip  # handy cross-platform clipboard text handler
import time
from PyDictionary import PyDictionary
from nltk.corpus import wordnet
import json
from clipboardGUI import clipboardGUI,clipboardNotFoundGUI
from clipboardMongo import jsonToMongo
from options import createOption

# import nltk
# nltk.download('wordnet') #if you want offline database


# Hypernym,hyponym,antonym,random
# copy content of clipboard to local variable for further process
def copy_clipboard():
    return pyperclip.paste()

def clean_Clipboard(var):
	# var.strip()  #remove whitespaces from beggining and end
	return var.split(' ')[0].strip().capitalize() #pick 1st word and capialize

var = copy_clipboard()
var = clean_Clipboard(var)
# print('var:',var)

if var == '':
	clipboardNotFoundGUI()
	exit(0)

dictionary=PyDictionary()
mean = dictionary.meaning(var)

# print('mean',mean)

# if word is not found in PyDIctionary then return not found
if mean == None :
	clipboardNotFoundGUI()
	exit(0)

createOption(var)
synonyms = []
meaning = []
for syn in wordnet.synsets(var): 
	meaning.append(syn.definition())
	for l in syn.lemmas(): 
		synonyms.append(l.name())

# print('sysn',synonyms)
# print('means',meaning)

# Dictionary for JSON data 
wordDict={}
jsonDict = {}
wordDict[var]=jsonDict
jsonDict['VocabWord']=var

# beutify text
# msg is for printing GUI lable

msg = "\n%s:\n"%(var)
if meaning !=[]:
	msg+="\n\tNoun:\n"
	jsonDict['Noun']={}
	for i,val in enumerate(set(meaning),1):
		msg+="\t %d. %s\n"%(i,val)
		temp={}
		temp[str(i)]=val
		jsonDict['Noun'].update(temp)

for key,val in mean.items():
	if key!='Noun':
		msg+="\n\t%s:\n"%(key)
		jsonDict[key]={}
		for i,v in enumerate(val,1):
			msg+="\t %d. %s\n"%(i,v)
			temp={}
			temp[str(i)]=v
			jsonDict[key].update(temp)

# for val in nouns:
#     msg+="\t %s\n"%(val)
msg+="\n\tSynonyms:\n"
jsonDict['Synonyms']={}
for i,val in enumerate(set(synonyms),1):
	msg+="\t %d. %s\n"%(i,val)
	temp={}
	temp[str(i)]=val
	jsonDict['Synonyms'].update(temp)

# print(msg)
# print(wordDict)
# print("JSon")
# print(jsonDict)

# jsonToMongo(jsonDict)
# with open('Words.js', 'a+') as json_file:
#   json.dump(wordDict, json_file)

clipboardGUI(msg)
