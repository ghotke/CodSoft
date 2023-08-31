from tkinter import*
from tkinter import ttk

class todo:
    def __init__(self,root):
        self.root=root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label=Label(self.root,text='To-Do-List-App', font='ariel, 25 bold',width=10,bd=7,bg='black', fg='red')
        self.label.pack(side='top', fill=BOTH)

        self.label2=Label(self.root,text='Add Task', font='ariel, 18 bold',width=10,bd=5,bg='black', fg='red')
        self.label2.place(x=43, y=59)

        self.label3=Label(self.root,text='Tasks', font='ariel, 18 bold',width=10,bd=5,bg='black', fg='red')
        self.label3.place(x=310, y=59)

        self.main_text = Listbox(self.root,height=9, bd=5, width=23, font='ariel,20  ')
        self.main_text.place(x=300,y=110)

        self.text=Text(self.root, bd=7, height=2, width=30, font='ariel, 10 ')
        self.text.place(x=25,y=120)
        #==========================add task================#
        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a')as file:
                file.write(content)
                file.seek(0)
                file.close()
                self.text.delete(1.0,END)
        #==============delete task=============#
        def delete():
            delete_= self.main_text.curselection()
            look=self.main_text.get(delete)
            with open('data.txt','r+')as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt','r') as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)
            file.close()

        self.button1=Button(self.root,text="Add",font='sarif,20',
                width=10,bd=10,bg='black',fg='red',command=add)
        self.button1.place(x=40,y=170)

        self.button2=Button(self.root,text="Delete",font='sarif,20',
                width=10,bd=10,bg='black',fg='red',command=delete)
        self.button2.place(x=40,y=250)
                    

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()
        
if __name__== "__main__":
    main()
