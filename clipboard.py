import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time
from PyDictionary import PyDictionary
from Tkinter import *
import tkMessageBox
import nltk
from nltk.corpus import wordnet
# nltk.download('wordnet')

def copy_clipboard():
    # pya.hotkey('ctrl', 'c')
    # time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

list = []
var = copy_clipboard()
list.append(var)
file1 = open("Words.txt","a") 
dictionary=PyDictionary()
# print(var+':\n' + str(dictionary.meaning(var))+'\n')
mean = dictionary.meaning(var)
synonyms = [] 
for syn in wordnet.synsets(var): 
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
print(synonyms)
# syn = str(dictionary.synonym(var))
ans = "%s:\n\t%s\n\t%s\n"%(var,str(mean),set(synonyms))
#print(ans)
file1.write(ans)

# beutify text
msg = "\n%s:\n"%(var)
for key,val in mean.items():
    msg+="\n\t%s:\n"%(key)
    for i,v in enumerate(val,1):
        msg+="\t %d. %s\n"%(i,v)
# for val in nouns:
#     msg+="\t %s\n"%(val)
msg+="\n\tSynonyms:\n"
for i,val in enumerate(set(synonyms),1):
    msg+="\t %d. %s\n"%(i,val)
print(msg)

# window = Tk()
# window.wm_withdraw()
# window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))

pya.alert(msg, "My Dictionary")  # always returns "OK"
# tkMessageBox.showinfo(title="My Dictionary", message=msg)

# print(list)
