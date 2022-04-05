from tkinter import *
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from tkinter import ttk

root = Tk()
root.title("Stuff")
root.geometry("800x700")
root.config(bg="lavender")
language = list(LANGUAGES.values())
title = Label(root, text="Language Translator", bg="lavender", font=("times",20))
label1 = Label(root, text="output", bg="lavender", font=("times",15))
title.place(relx=0.5,rely=0.1,anchor=CENTER)
label1.place(relx=0.75,rely=0.3,anchor=CENTER)
area = Text(root, bg="orchid",font=("times",13),height=11,width=50,wrap=WORD,padx=5,pady=5,bd=0)
area.place(relx=0.75,rely=0.5,anchor=CENTER)
label11 = Label(root, text="Enter Text", bg="lavender", font=("times",15))
label11.place(relx=0.1,rely=0.3,anchor=CENTER)
area1 = Text(root, bg="orchid",font=("times",13),height=11,width=50,wrap=WORD,padx=5,pady=5,bd=0)
area1.place(relx=0.25,rely=0.5,anchor=CENTER)
boxx = ttk.Combobox(root, state = "readonly", values = language)
boxx.set("english")
boxx.place(relx=0.3,rely=0.3,anchor=CENTER)
boxxx = ttk.Combobox(root, state = "readonly", values = language)
boxxx.set("spanish")
boxxx.place(relx=0.7,rely=0.3,anchor=CENTER)
afootersothatppldontcopymycodeandmarkastheirowncode = Label(root, text="This is made by Leo Yan, no ctrl + c and ctrl + v please", bg="wheat",font=("Times New Roman", 15,"bold"))
afootersothatppldontcopymycodeandmarkastheirowncode.place(relx=0.5,rely=1,anchor=S)

def translatedatboi():
    scource1 = boxx.get()
    scource2 = boxxx.get()
    trans = Translator()
    try:
        translated = trans.translate(text = area1.get(1.0,END), src = scource1, dest = scource2, **kwargs)
    except:
        print("error with the translating part, find out what is wrong mah boi")
    
    area.delete(1.0,END)
    try:
        area.insert(END, translate.text)
    except:
        print("error with inserting the text, find out what is wrong mah boi")
    
btn = Button(root, text="translate", command = translatedatboi)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()