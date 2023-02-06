from tkinter import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
root.iconbitmap("icons/logo.ico")
root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="blue")
#การสร้างเฟรม
frame1 = Frame(root,bg="pink")
frame2 = LabelFrame(root,text="Frame Title")

#แสดงเฟรม
frame1.pack(fill=BOTH,expand=True)
Button(frame1,text="Button 1").pack()
Button(frame1,text="Button 2").pack()
Button(frame1,text="Button 3").pack()

frame2.pack(fill=BOTH,expand=True)
Button(frame2,text="Button 4").grid(row=0,column=0)
Button(frame2,text="Button 5").grid(row=0,column=1)
Button(frame2,text="Button 6").grid(row=0,column=2)


root.mainloop()