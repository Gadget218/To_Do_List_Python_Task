from tkinter import *
from tkinter import ttk #database

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')#width, height, "+"=window position

        #let's create a label:
        self.label = Label(self.root, text="To-Do-List-App",
                        font="ariel, 25 bold", width=10, bd=5, bg='orange', fg='black')#bd=border width, bg=background color and foreground color=black
#pack is a widget in the parent widget
        self.label.pack(side='top',fill=BOTH)#BOTH fills both x and y axis


        self.label2 = Label(self.root, text="Add Task",
                        font="ariel, 18 bold", width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)#position of second label, its coordinates


        self.label3 = Label(self.root, text="Tasks",
                        font="ariel, 18 bold", width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text= Listbox(self.root, height=9, bd=5, width=23, font='ariel, 20 italic bold')#creates a listbox, the place where all the to do tasks will be displayed
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')#creates a place to enter the tasks to enter in to do list
        self.text.place(x=20, y=120)
#---add tasks--:
        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file: #opening a file, a is to append the data
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)#each  time we enter the task and add it will get deleted from the text box

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:#to delete from text file
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)#we're deleting the item we selected in our text box
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()
        
        def Mark_item():# Item is marked with blue color
            self.main_text.itemconfig(self.main_text.curselection(), fg="blue")
            self.main_text.selection_clear(1.0, END)
        
        def Unmark_item():#item is unmarked
            self.main_text.itemconfig(self.main_text.curselection(), fg="black")
            self.main_text.selection_clear(1.0, END)
        




            
        #Buttons are added:
        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                    width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
            width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)

        self.button3 = Button(self.root, text="Mark", font='sarif, 20 bold italic',
            width=10, bd=5, bg='orange', fg='black', command=Mark_item)
        self.button3.place(x=30, y=380)

        self.button4 = Button(self.root, text="Remove Mark", font='sarif, 20 bold italic',
            width=10, bd=5, bg='orange', fg='black', command=Unmark_item)
        self.button4.place(x=30, y=480)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
