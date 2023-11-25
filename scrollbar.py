from tkinter import *
root=Tk()
root.geometry("700x400")
root.title("Scrollbar")

#for connectin a Scrollbar in widget learn the two steps that:
#1- widget(yscrollcommand=Scrollbar.set)
#2- scrollbar.config(command = widget.yview)

Scrollbar=Scrollbar(root)
Scrollbar.pack(side=RIGHT ,fill=Y)
# listbox = Listbox(root,yscrollcommand=Scrollbar.set)
# for i in range (350):
#     listbox.insert(END,f"item{i}")
# listbox.pack(fill=BOTH,padx=29)
# Scrollbar.config(command=listbox.yview)


text= Text(root,yscrollcommand=Scrollbar.set)
text.pack(fill=Y)

root.mainloop()