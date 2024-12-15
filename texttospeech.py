from tkinter import *
import os
from gtts import gTTS

root=Tk()
frame1=Frame(root,bg="grey",height="150")
frame1.pack(fill=X)
frame2=Frame(root,bg="red",height="750")
frame2.pack(fill=X)
label=Label(frame1,text="Text to speech",font="bold,40",bg="orange")
label.place(x=180,y=70)
entry=Entry(frame2,width=45,font=14)
entry.place(x=130,y=50)

def play():
    language="en"
    myobject=gTTS(text=entry.get(),lang=language,slow=False)
    myobject.save("convert.wav")
    os.system("convert.wav")
btn=Button(frame2,text="submit",width=15,command=play,bg="orange")
btn.place(x=250,y=130)
    





root.mainloop()

