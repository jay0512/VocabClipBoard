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
mean = str(dictionary.meaning(var))
synonyms = [] 
for syn in wordnet.synsets(var): 
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
print(synonyms)
# syn = str(dictionary.synonym(var))
ans = "%s:\n\t%s\n\t%s\n"%(var,mean,synonyms)
#print(ans)
file1.write(ans)
window = Tk()
window.wm_withdraw()
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="My Dictionary", message=ans)

# print(list)
