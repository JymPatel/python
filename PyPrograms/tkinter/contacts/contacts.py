# code by @JymPatel (editors can put their name here && thanks for contribution :)
# this code uses GPL V3 LICENSE

import tkinter
from text03 import text_array
import functions as fuN


# main window
root_01 = tkinter.Tk()
root_01.title("contacts.py")
root_01.geometry("300x500")

# welcome heading
welcome = tkinter.Label(root_01, text=text_array["welcome"], pady=10, font=("consolas 12"), background="white")
welcome.pack(fill=tkinter.X)

# new contact button
add_contact = tkinter.Button(root_01, text="add new contact", font=("consolas 10"))
add_contact.pack(fill=tkinter.X)

# run
root_01.mainloop()
