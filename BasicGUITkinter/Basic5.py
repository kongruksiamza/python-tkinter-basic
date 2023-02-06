from tkinter import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="blue")

#สร้างปุ่ม
btn1=Button(root,text="ปุ่มที่ 1")
btn1.pack(side=TOP)

btn2=Button(root,text="ปุ่มที่ 2",fg="red")
btn2.pack(side=LEFT)

btn3=Button(root,text="ปุ่มที่ 3",bg="black",fg="white")
btn3.pack(side=RIGHT)

btn4=Button(root,text="ปุ่มที่ 4",bg="green",fg="white",activebackground="red",activeforeground="white")
btn4.pack(side=BOTTOM)


root.mainloop()