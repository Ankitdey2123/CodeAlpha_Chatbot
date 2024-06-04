import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import scrolledtext
import datetime
import webbrowser

def bot_reply():
    chat_box.config(state=tk.NORMAL)
    question=question_entry.get()
    chat_box.insert(END,'You: '+question+"\n\n")
    if question=='hi':
        chat_box.insert('end',"Rajni-Bot: Hello,How can I help you?\n\n","blue")
    elif question=='hi rajni':
        chat_box.insert('end',"Rajni-Bot: Hello,How can I help you?\n\n","blue")
    elif question=='how are you':
        chat_box.insert('end',"Rajni-Bot: I am okay.what about you?\n\n","blue")
    elif question=='i am fine':
        chat_box.insert('end',"Rajni-Bot:good,how can i help you\n\n","blue")
    elif question=='how old are you':
        chat_box.insert('end',"Rajni-Bot: My creator just brought me to life in front of you I'm not much older than 10 mins.\n\n","blue")
    elif question=='what is the time':
        now=datetime.datetime.now()
        chat_box.insert('end',"Rajni-Bot: It is"+now.strftime("%H:%M:%S%p")+"\n\n","blue")
    elif question=='how many language you know':
        chat_box.insert('end',"Rajni-Bot: only one language I know that is English\n\n","blue")
    elif question=='what is your name':
        chat_box.insert('end',"Rajni-Bot: My name is Rajni\n\n","blue")
    elif question=='what is god':
        chat_box.insert('end',"Rajni-Bot: Humans creator are known as god,According to me my god is master Ankit.He is my god\n\n","blue")
    elif question=='who created you':
        chat_box.insert('end',"Rajni-Bot: Master Ankit\n\n","blue")
    elif question=='bye':
        chat_box.insert('end',"Rajni-Bot: Goodbye,have a nice day!\n\n","blue")
    elif question=='who is your master':
        chat_box.insert('end',"Rajni-Bot: My master is Ankit\n\n","blue")
    elif question=='what is the name of your master':
        chat_box.insert('end',"Rajni-Bot: My master name is Ankit\n\n","blue")
    elif question=='good morning':
        chat_box.insert('end',"Rajni-Bot: very good morning,how can i help you?\n","blue")
    elif question=='good morning rajni':
        chat_box.insert('end',"Rajni-Bot: very good morning,how can i help you\n\n","blue")
    elif question=='good noon':
        chat_box.insert('end',"Rajni-Bot: good noon,how can i help you\n\n","blue")
    elif question=='good noon rajni':
        chat_box.insert('end',"Rajni-Bot: good noon,how can i help you\n\n","blue")
    elif question=='good afternoon':
        chat_box.insert('end',"Rajni-Bot: good afternoon,how can i help you\n\n","blue")
    elif question=='good afternoon rajni':
        chat_box.insert('end',"Rajni-Bot: good afternoon,how can i help you\n\n","blue")
    elif question=='good night':
        chat_box.insert('end',"Rajni-Bot: good night,have a nice day!\n\n","blue")
    elif question=='good night rajni':
        chat_box.insert('end',"Rajni-Bot:g ood night,have a nice day!\n\n","blue")
    elif question=='open linkedin':
        chat_box.insert('end',"Rajni-Bot: opening linkedin \n\n","blue")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif question=='open  my linkedin account':
        chat_box.insert('end',"Rajni-Bot: opening linkedin \n\n","blue")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif question=='open google':
        chat_box.insert('end',"Rajni-Bot: opening google \n\n","blue")
        webbrowser.open("https://www.google.com")
    elif question=='open youtube':
        chat_box.insert('end',"Rajni-Bot: opening youtube \n\n","blue")
        webbrowser.open("https://www.youtube.com")
    elif question=='open facebook':
        chat_box.insert('end',"Rajni-Bot: opening facebook \n\n","blue")
        webbrowser.open("https://www.facebook.com")
    else:
        chat_box.insert('end',"Rajni-Bot: I'm sorry, I do not understand said it again\n\n","blue")
    question_entry.delete(0,END)
    chat_box.config(state=tk.DISABLED)


chatbot_root=tk.Tk()
chatbot_root.title("Rajni-Chatbot")
chatbot_root.geometry("600x700+350+10")
chatbot_root.resizable(False,False)

chatbot_root.grid_rowconfigure(0,weight=1)
chatbot_root.grid_rowconfigure(1,weight=4)
chatbot_root.grid_rowconfigure(2,weight=1)

top_frame=tk.Frame(chatbot_root,width=600,height=210,bg='antique white')
top_frame.grid(row=0,column=0,sticky=tk.NSEW)

logo_pic=PhotoImage(file='pic.png')
logopic_label=tk.Label(top_frame,image=logo_pic,bg='antique white')
logopic_label.place(x=250,y=14)
title_label=tk.Label(top_frame,text="Rajni-ChatBot",font=('arial',25,'bold'),fg='seagreen',bg='antique white')
title_label.place(x=210,y=150)

middle_frame=tk.Frame(chatbot_root,width=600,height=438,bg='white')
middle_frame.grid(row=1,column=0,sticky=tk.NSEW)


chat_box=scrolledtext.ScrolledText(middle_frame,font=('arial',11,'bold'),fg='black',width=72,height=28)
chat_box.config(state=tk.DISABLED)
chat_box.pack(side=tk.TOP)

buttom_frame=tk.Frame(chatbot_root,width=600,height=100,bg='antique white')
buttom_frame.grid(row=2,column=0,sticky=tk.NSEW)

question_entry=tk.Entry(buttom_frame,font=('arial',14),bg='white',width=48,fg='black',bd=4)
question_entry.pack(side=tk.LEFT,padx=8)

send_button=tk.Button(buttom_frame,text='>>',font=('arial',15,'bold'),bg='seagreen',fg='white',command=bot_reply)
send_button.pack(side=tk.LEFT,padx=2)

chatbot_root.mainloop()
