from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x400")
window.title("Login")
window.resizable(False, False)

#----------------------------SAVE-----------------------------------------------

def save():
    savemail = mail.get()
    saveuser = user.get()
    savepassword2 = password2.get()
    file = open(r'''accounts.txt''', "w")
    file.write(savemail)
    file.write("//")
    file.write(saveuser)
    file.write("//")
    file.write(savepassword2)
    savetext = Label(window2, text = "You are now registered")
    savetext.pack()

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

login = Button(window, text = "Login")
login.pack(ipadx=25, ipady=10)

mailtext2 = Label(window2, text = "Mail")
mailtext2.pack()
mail = Entry(window2)
mail.pack(padx =10, pady =10, ipadx=100, ipady=10)

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


window.mainloop()
