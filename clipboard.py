import pyperclip  # handy cross-platform clipboard text handler
import time
from PyDictionary import PyDictionary
from nltk.corpus import wordnet
import json
from clipboardGUI import clipboardGUI
# import nltk
# nltk.download('wordnet') #if you want offline database

# copy content of clipboard to local variable for further process
def copy_clipboard():
    return pyperclip.paste()

var = copy_clipboard()
# file1 = open("Words.txt","a") 
dictionary=PyDictionary()
mean = dictionary.meaning(var)

synonyms = []
meaning = []
for syn in wordnet.synsets(var): 
	meaning.append(syn.definition())
	for l in syn.lemmas(): 
		synonyms.append(l.name())

print('sysn',synonyms)
print('means',meaning)
# syn = str(dictionary.synonym(var))
# ans = "%s:\n\t%s\n\t%s\n"%(var,str(mean),set(synonyms))
# ans = "%s:\n\t%s\n\t%s\n"%(var,set(meaning),set(synonyms))
# print(ans)
# file1.write(ans)

# Dictionary for JSON data 
wordDict={}
jsonDict = {}
wordDict[var]=jsonDict

# beutify text
# msg is for printing GUI lable

msg = "\n%s:\n"%(var)
if meaning !=[]:
	msg+="\n\tNoun:\n"
	jsonDict['Noun']={}
	for i,val in enumerate(set(meaning),1):
		msg+="\t %d. %s\n"%(i,val)
		temp={}
		temp[i]=val
		jsonDict['Noun'].update(temp)

for key,val in mean.items():
	if key!='Noun':
		msg+="\n\t%s:\n"%(key)
		jsonDict[key]={}
		for i,v in enumerate(val,1):
			msg+="\t %d. %s\n"%(i,v)
			temp={}
			temp[i]=v
			jsonDict[key].update(temp)

# for val in nouns:
#     msg+="\t %s\n"%(val)
msg+="\n\tSynonyms:\n"
jsonDict['Synonyms']={}
for i,val in enumerate(set(synonyms),1):
	msg+="\t %d. %s\n"%(i,val)
	temp={}
	temp[i]=val
	jsonDict['Synonyms'].update(temp)

print(msg)
print(wordDict)
with open('Words.js', 'a+') as json_file:
  json.dump(wordDict, json_file)

clipboardGUI(msg)