from tkinter import*
import random

root = Tk()
root.configure(background="cyan")
root.geometry("400x600")
root.title("random_country")

label_country = Label(root,text="enter names of country",fg="black",bg="cyan")
label_country.place(rely=0.2,relx=0.3,anchor=CENTER)

inp_con = Entry(root)
inp_con.place(rely=0.2,relx=0.7,anchor=CENTER)

label_cap = Label(root,text="enter names of capital",fg="black",bg="cyan")
label_cap.place(rely=0.3,relx=0.3,anchor=CENTER)

inp_cap = Entry(root)
inp_cap.place(rely=0.3,relx=0.7,anchor=CENTER)

label_show = Label(root,fg="black",bg="cyan")

country = []
capital =[]

def submit():
    val = inp_con.get()
    val1 = inp_cap.get()
    
    country.append(val)
    capital.append(val1)
    
def random_country() :
    
    
    len_con = len(country)
    len_cap = len(capital)
    

    random_no = random.randint(0,(len_con-1))
    ran_con = country[random_no]
    ran_cap = capital[random_no]
    label_show["text"] = "random country and capital is = "+str(ran_con)+" and its capital is "+str(ran_cap)
   
        
        
btn_submit = Button(root,bg="yellow",fg="black",text = "submit",command=submit)
btn_submit.place(rely=0.4,relx=0.5,anchor=CENTER)

btn = Button(root,bg="yellow",fg="black",text = "see the random country and capital",command=random_country)
btn.place(rely=0.5,relx=0.5,anchor=CENTER)

label_show.place(rely=0.7,relx=0.5,anchor=CENTER)
root.mainloop()