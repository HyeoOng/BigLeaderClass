from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo("제목", "나 불렀어?")

window = Tk()
window.geometry('400x500')
window.title('여기가 제목')
label1 = Label(window, text='나 글자다', font=("궁서체", 20))
button1 = Button(window, text='나를 클릭해줘', command=clickButton)


label1.pack()
button1.pack()




window.mainloop()