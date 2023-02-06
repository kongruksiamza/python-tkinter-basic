from tkinter import *

#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)

def selectChoice():
    result = choice.get()
    if result==1:
        root.config(bg="green")
    elif result==2:
        root.config(bg="pink")
    else:
        root.config(bg="purple")

choice = IntVar()
#radio button
Radiobutton(root,text="สีเขียว",value=1,variable=choice,command=selectChoice).grid(row=0,column=0)
Radiobutton(root,text="สีชมพู",value=2,variable=choice,command=selectChoice).grid(row=0,column=1)
Radiobutton(root,text="สีม่วง",value=3,variable=choice,command=selectChoice).grid(row=0,column=2)

root.mainloop()