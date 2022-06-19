# using tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login ():
    email=email_input.get()
    password=password_input.get()
    print(email,password)

    if email =='sudeep@gmail.com' and password=='1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('error','login failed')
    

root=Tk()
root.title('login form')
root.iconbitmap('favicon.ico')
root.geometry('350x500')
root.configure(background='#0096DC')
img=Image.open('flipkart-logo.png')
img_resize=img.resize((70,70))
img=ImageTk.PhotoImage(img_resize)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))
text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))
email_label=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack()
email_label.config(font=('verdana',12))
email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack()
password_label.config(font=('verdana',12))
password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

#button
login_btn=Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))
root.mainloop()

