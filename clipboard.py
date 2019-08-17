import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time
from PyDictionary import PyDictionary
import Tkinter as tk
from Tkinter import *
import tkMessageBox
import nltk
from nltk.corpus import wordnet
import json
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
meaning = []
for syn in wordnet.synsets(var): 
	meaning.append(syn.definition())
	for l in syn.lemmas(): 
		synonyms.append(l.name())

print('sysn',synonyms)
print('means',meaning)
# syn = str(dictionary.synonym(var))
# ans = "%s:\n\t%s\n\t%s\n"%(var,str(mean),set(synonyms))
ans = "%s:\n\t%s\n\t%s\n"%(var,set(meaning),set(synonyms))
#print(ans)
file1.write(ans)

wordDict={}
jsonDict = {}
wordDict[var]=jsonDict
# beutify text
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

# window = Tk()
# # window.wm_withdraw()
# window.geometry("500x700+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
# w = Label(window, text=msg, font=("Helvetica", 11), anchor='nw', justify=LEFT)
# w.pack()
# # scrollbar = Scrollbar(w)
# # scrollbar.pack(side=RIGHT, fill=Y)

# mainloop()

# pya.alert(msg, "My Dictionary")  # always returns "OK"
# tkMessageBox.showinfo(title="My Dictionary", message=msg)

# print(list)

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


root = tk.Tk()
root.title("My Dictionary")
# --- create canvas with scrollbar ---
root.geometry("500x700+"+str(root.winfo_screenwidth()/2)+"+"+str(root.winfo_screenheight()/2))
canvas = tk.Canvas(root,width=490, height=690)
# canvas.pack(side=tk.LEFT)
canvas.grid(row=0, column=0)

scrollbary = tk.Scrollbar(root, command=canvas.yview)
# scrollbary.pack(side=tk.LEFT, fill='y')
scrollbary.grid(row=0, column=1, sticky="ns")

scrollbarx = tk.Scrollbar(root, command=canvas.xview)
# scrollbarx.pack(side=tk.RIGHT, fill='x')
scrollbarx.grid(row=1, column=0, sticky="ew")

canvas.configure(xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)
canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
canvas.bind_all('<MouseWheel>', lambda event: canvas.xview_scroll(int(-1*(event.delta/120)), "units"))
# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

l = tk.Label(frame, text=msg, font=("Helvetica", 11), anchor='nw', justify=LEFT)
l.pack()
# txt = Label(subframe, text=msg, font=("Helvetica", 11), anchor='nw', justify=LEFT)

# --- start program ---

root.mainloop()