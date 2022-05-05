from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x400")
window.title("Login")
window.resizable(False, False)

#----------------------------SAVE-----------------------------------------------

def save():
    savemail = mail2.get()
    saveuser = user.get()
    savepassword2 = password2.get()
    filemail = open(r'''accountmail.txt''', "w")
    filemail.write(savemail)
    filemail.close()
    fileuser = open(r'''accountuser.txt''', "w")
    fileuser.write(saveuser)
    fileuser.close()
    filepassword = open(r'''accountpassword.txt''', "w")
    filepassword.write(savepassword2)
    filepassword.close()
    savetext = Label(window2, text = "You are now registered")
    savetext.pack()

def exit():
    newwindow.destroy()

def read():
    global newwindow
    global mail
    global logintext
    getmail = mail.get()
    filemail = open(r'''accountmail.txt''', "r")
    filepassword = open(r'''accountpassword.txt''', "r")
    getpassword = password.get()
    if getmail in filemail:
        if getpassword in filepassword:
            logintext['text'] = "Welcome"
            newwindow = Toplevel(window)
            newwindow.title("Program")
            newwindow.geometry("200x200")
            signout = Button(newwindow, text = "Sign out", command = exit)
            signout.pack()
        else:
            logintext['text'] = "Incorrect password"
    else:
        logintext['text'] = "Mail not registered"

#----------------------------INTERFACE------------------------------------------

menu = ttk.Notebook(window)
menu.pack(fill="both")
window = ttk.Frame(menu)
menu.add(window, text ="Login")
window2 = ttk.Frame(menu)
menu.add(window2, text ="Register")

mailtext = Label(window, text = "Mail")
mailtext.pack()
mail = Entry(window)
mail.pack(padx =10, pady =10, ipadx=100, ipady=10)

passwordtext = Label(window, text = "Password")
passwordtext.pack()
password = ttk.Entry(window,show = "*")
password.pack(padx =10, pady =10,ipadx=100, ipady=10)

login = Button(window, text = "Login", command = read)
login.pack(ipadx=25, ipady=10)

mailtext2 = Label(window2, text = "Mail")
mailtext2.pack()
mail2 = Entry(window2)
mail2.pack(padx =10, pady =10, ipadx=100, ipady=10)

usertext = Label(window2, text = "Nickname")
usertext.pack()
user = Entry(window2)
user.pack(padx =10, pady =10, ipadx=100, ipady=10)

passwordtext2 = Label(window2, text = "Password")
passwordtext2.pack()
password2 = ttk.Entry(window2,show = "*")
password2.pack(padx =10, pady =10,ipadx=100, ipady=10)

register = Button(window2, text = "Register", command = save)
register.pack(ipadx=25, ipady=10)

logintext = Label(window, text = " ")
logintext.pack()

window.mainloop()
