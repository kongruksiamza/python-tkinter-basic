from tkinter import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="pink")

#แสดงข้อความ
label1=Label(root,text="สวัสดี",font=("Arial",30,"bold"),bg="red",fg="white")
label1.pack(fill="x",padx=(5,10),pady=(5,10))

label2=Label(root,text="Python",font=("Arial",30,"bold"),bg="blue",fg="white")
label2.pack(pady=5,ipadx=50,ipady=10)

label3=Label(root,text="Tkinter",font=("Arial",30,"bold"),bg="green",fg="white")
label3.pack(fill=BOTH,expand=True)

label4=Label(root,text="GUI",font=("Arial",30,"bold"),bg="black",fg="white")
label4.pack(fill=BOTH,expand=True,ipadx=10,ipady=10)

root.mainloop()