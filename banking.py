import tkinter
from tkinter import*
from tkinter import messagebox
from time import gmtime, strftime

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	main_menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

def Cr_Amt(accnt,name):
	creditwn=Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="orange")
	title=Message(creditwn,text="VK's BANK",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	title.config(font=("Courier","50","bold"))
	title.pack(side="top")
	l1=Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
	e1=Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
	debitwn=Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="orange")
	title=Message(debitwn,text="VK's BANK",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	title.config(font=("Courier","50","bold"))
	title.pack(side="top")
	l1=Label(debitwn,relief="raised",text="Enter Amount to be debited: ")
	e1=Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(debitwn,text="Debit",relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))

def balance(accnt):
	fdet=open(accnt+".txt",'r')
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)

def tran_hist(accnt):
	disp_wn=Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="orange")
	fr1=Frame(disp_wn,bg="blue")
	title=Message(disp_wn,text="VK's BANK",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	title.config(font=("Courier","50","bold"))
	title.pack(side="top")
	l1=Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	fr=Frame(disp_wn)
	fr.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for i in frec:
		l=Message(disp_wn,anchor="w",text=i,relief="groove",width=2000)
		l.pack(side="top")
	b=Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def loggedin_menu(accnt,name):
	rootwn=Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Livewire BANK-"+name)
	rootwn.configure(background='orange')
	title=Message(rootwn,text="VK's BANKING",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	title.config(font=("Courier","50","bold"))
	title.pack(side="top")
	label=Label(text="Logged in as: "+name,relief="raised",bg="black",fg="white",anchor="center",justify="center")
	label.pack(side="top")
	b2=Button(text="current Amount",command=lambda: Cr_Amt(accnt,name))
	b2.place(x=200,y=200)
	b3=Button(text="Dep Amount",command=lambda: De_Amt(accnt,name))
	b3.place(x=200,y=400)
	b4=Button(text="Balance Amaount",command=lambda: balance(accnt))
	b4.place(x=900,y=200)
	b5=Button(text="Transaction History",command=lambda: tran_hist(accnt))
	b5.place(x=900,y=400)
	b6=Button(text="LogOut",relief="raised",command=lambda: logout(rootwn))
	b6.place(x=500,y=600)
	
	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	main_menu()

def check_login(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		main_menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials")
		master.destroy()
		main_menu()
	else:
		master.destroy()
		loggedin_menu(acc_num,name)



def login(master):
	master.destroy()
	loginwn=Tk()
	loginwn.geometry("600x300")
	loginwn.title("Log in")
	loginwn.configure(bg="blue")
	l_title=Message(loginwn,text="VK's BANK",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=Label(loginwn,text="Enter Name:",relief="raised")
	l1.pack(side="top")
	e1=Entry(loginwn)
	e1.pack(side="top")
	l2=Label(loginwn,text="Enter account number:",relief="raised")
	l2.pack(side="top")
	e2=Entry(loginwn)
	e2.pack(side="top")
	l3=Label(loginwn,text="Enter your PIN:",relief="raised")
	l3.pack(side="top")
	e3=Entry(loginwn,show="+")
	e3.pack(side="top")
	b=Button(loginwn,text="Submit",command=lambda: check_login(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=Button(text="HOME",relief="raised",bg="cyan",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_login(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	



def create():
    crwn=Tk()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.configure(bg="red")
    l_title=Message(crwn,text="VK's BANK",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","50","bold"))
    l_title.pack(side="top")
    l1=Label(crwn,text="Enter Name:",relief="groove")
    l1.pack(side="top")
    e1=Entry(crwn)
    e1.pack(side="top")
    l2=Label(crwn,text="Enter opening credit:",relief="groove")
    l2.pack(side="top")
    e2=Entry(crwn)
    e2.pack(side="top")
    l3=Label(crwn,text="Enter desired PIN:",relief="groove")
    l3.pack(side="top")
    e3=Entry(crwn,show="+")
    e3.pack(side="top")
    b=Button(crwn,text="Submit",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side="top")
    crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    return



def main_menu() :
    window=Tk()
    window.geometry("1280x720")
    window.title("Banking")
    bgm=PhotoImage(file="Mbg1.gif")
    bgm1=bgm.zoom(2)
    x=Label(image=bgm1)
    x.place(y=0)

    l_title=Label(text="VK's Banking System",width=2000,padx=600,pady=0,fg="Red",bg="black",justify="center",anchor="center")
    l_title.config(font=("Courier","60","bold"))
    l_title.pack(side="top")

    imgca=PhotoImage(file="ca1.gif")
    imglo=PhotoImage(file="login1.gif")
    imge=PhotoImage(file="exit.gif")
    imgca1=imgca.subsample(2,2)
    imglo1=imglo.subsample(2,3)
    imge1=imge.subsample(2,2)

    b1=Button(image=imgca1,relief="groove",command=create)
    b1.place(x=500,y=200)
    b2=Button(image=imglo1,command=lambda: login(window))
    b2.place(x=500,y=350)
    b3=Button(image=imge1,command=window.destroy)
    b3.place(x=500,y=500)


    window.mainloop()

main_menu()