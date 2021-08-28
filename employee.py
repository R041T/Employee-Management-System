# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:18:40 2019

@author: Rohit
"""
import mysql.connector
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
import array as arr
app = tk.Tk()


mydb = mysql.connector.connect(user='root',
                               password='mysql',
                              host='127.0.0.1',
                              auth_plugin='mysql_native_password')

mycursor = mydb.cursor(buffered=True)                   

mycursor.execute("use employee")
mycursor.execute("select * from login ")

##########################Creating the UI#######################################################

class mainframe(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (Login_Page,HomePage,Employeepage,Payrollpage,Clerkpage,Projectpage,RemoveEntry):
        
            frame = F(container, self)
    
            self.frames[F] = frame
    
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login_Page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Login_Page(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent,background="light blue")
        usernamelabel=tk.Label(self,text="Name",font=("times new roman",11),background="light blue")
        passwordlabel=tk.Label(self,text="Password",font=("times new roman",11),background="light blue")
        self.user_entry=tk.Entry(self)
        self.pass_entry=tk.Entry(self,show="*")
        
        usernamelabel.grid(row=0,column=17)
        passwordlabel.grid(row=2,column=17)
        self.user_entry.grid(row=0,column=15)
        self.pass_entry.grid(row=2,column=15)
        
        login_button=tk.Button(self,text="Login",command=self.loginbuttonclick,font=("times new roman",11))
        login_button.grid(row=4,column=15)
    
    def loginbuttonclick(self):
        username=self.user_entry.get()
        password=self.pass_entry.get()
        mycursor.execute("Select password from login where username=%s",[str(username)])
        result = mycursor.fetchall()
        if(int(result[0][0])==int(password)):   
            self.controller.show_frame(HomePage)
        else:
            print("Invalid Password")
        
        
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        Employeebutton=tk.Button(self,text="Employee data",command=lambda:controller.show_frame(Employeepage),font=("times new roman",11))
        Employeebutton.grid(row=1,column=1)
        Clerkbutton=tk.Button(self,text="Clerk data",command=lambda:controller.show_frame(Clerkpage),font=("times new roman",11))
        Clerkbutton.grid(row=1,column=5)
        Projectsbutton=tk.Button(self,text="Projects data",command=lambda:controller.show_frame(Projectpage),font=("times new roman",11))
        Projectsbutton.grid(row=1,column=9)
        Payroll=tk.Button(self,text="Payroll",command=lambda:controller.show_frame(Payrollpage),font=("times new roman",11))
        Payroll.grid(row=1,column=14)
        Removepagebutton=tk.Button(self,text="Remove data",command=lambda:controller.show_frame(RemoveEntry),font=("times new roman",11))
        Removepagebutton.grid(row=1,column=19)
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=1, column=23)
        
class Employeepage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        Addlabel1=tk.Label(self,text="Enter Employee id",font=("times new roman",11),background="light blue")
        Addlabel1.grid(row=0,column=0)
        Addlabel2=tk.Label(self,text="Enter Employee name",font=("times new roman",11),background="light blue")
        Addlabel2.grid(row=1,column=0)
        Addlabel3=tk.Label(self,text="Enter Sex(Male/Female)",font=("times new roman",11),background="light blue")
        Addlabel3.grid(row=2,column=0)
        Addlabel4=tk.Label(self,text="Enter Date of birth in (YYYY-MM-DD)",font=("times new roman",11),background="light blue")
        Addlabel4.grid(row=3,column=0)
        Addlabel5=tk.Label(self,text="Enter Contact number",font=("times new roman",11),background="light blue")
        Addlabel5.grid(row=4,column=0)
        Addlabel6=tk.Label(self,text="Enter Designation",font=("times new roman",11),background="light blue")
        Addlabel6.grid(row=5,column=0)
        Addlabel7=tk.Label(self,text="Enter Department",font=("times new roman",11),background="light blue")
        Addlabel7.grid(row=6,column=0)
        Addlabel8=tk.Label(self,text="Enter Hire date in (YYYY-MM-DD)",font=("times new roman",11),background="light blue")
        Addlabel8.grid(row=7,column=0)
        
        self.AddEntry1=tk.Entry(self)
        self.AddEntry2=tk.Entry(self)
        self.AddEntry3=tk.Entry(self)
        self.AddEntry4=tk.Entry(self)
        self.AddEntry5=tk.Entry(self)
        self.AddEntry6=tk.Entry(self)
        self.AddEntry7=tk.Entry(self)
        self.AddEntry8=tk.Entry(self)
        self.AddEntry1.grid(row=0,column=1)
        self.AddEntry2.grid(row=1,column=1)
        self.AddEntry3.grid(row=2,column=1)
        self.AddEntry4.grid(row=3,column=1)
        self.AddEntry5.grid(row=4,column=1)
        self.AddEntry6.grid(row=5,column=1)
        self.AddEntry7.grid(row=6,column=1)
        self.AddEntry8.grid(row=7,column=1)
        
        Addbutton=tk.Button(self,text="Add to database",command=self.addentry,font=("times new roman",11))
        Addbutton.grid(row=1,column=8)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage),font=("times new roman",11))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=4,column=8)
        
        Viewbutton=tk.Button(self,text="Display values",command=self.disp,font=("times new roman",11))
        Viewbutton.grid(row=2,column=8)
        
    def addentry(self):
        emp_id = self.AddEntry1.get()
        name = self.AddEntry2.get()
        sex = self.AddEntry3.get()
        dob = self.AddEntry4.get()
        contact = self.AddEntry5.get()
        desig = self.AddEntry6.get()
        depart = self.AddEntry7.get()
        hire = self.AddEntry8.get()
        
        mycursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)",[str(emp_id),str(name),str(sex),str(dob),
                         int(contact),str(desig),str(hire),str(depart)])
        mydb.commit()
    
    def disp(self):
        mycursor.execute("select count(*) from employee")
        n=mycursor.fetchall()[0][0]
        b=tk.Listbox(self)
        for i in range (n):
            mycursor.execute("select * from employee")
            b.insert(i,mycursor.fetchall()[i])
            b.grid(row=8,column=1)
        

        
class Clerkpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        
        Addlabel1=tk.Label(self,text="Enter clerk id",font=("times new roman",11),background="light blue")
        Addlabel1.grid(row=0,column=0)
        Addlabel2=tk.Label(self,text="Enter clerk name",font=("times new roman",11),background="light blue")
        Addlabel2.grid(row=1,column=0)
        Addlabel3=tk.Label(self,text="Enter contact number",font=("times new roman",11),background="light blue")
        Addlabel3.grid(row=2,column=0)
        
        self.AddEntry1=tk.Entry(self)
        self.AddEntry2=tk.Entry(self)
        self.AddEntry3=tk.Entry(self)
        self.AddEntry1.grid(row=0,column=1)
        self.AddEntry2.grid(row=1,column=1)
        self.AddEntry3.grid(row=2,column=1)
        
        Addbutton=tk.Button(self,text="Add to database",command=self.addentry,font=("times new roman",11))
        Addbutton.grid(row=1,column=8)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage),font=("times new roman",11))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=4,column=8)
        
        Viewbutton=tk.Button(self,text="Display values",command=self.disp,font=("times new roman",11))
        Viewbutton.grid(row=2,column=8)
        
    def addentry(self):
        c_id = self.AddEntry1.get()
        clerk_name = self.AddEntry2.get()
        contact_num = self.AddEntry3.get()
        mycursor.execute("insert into clerk values(%s,%s,%s)",[str(c_id),str(clerk_name),int(contact_num)])
        mydb.commit()
        
    def disp(self):
        mycursor.execute("select count(*) from clerk")
        n=mycursor.fetchall()[0][0]
        b=tk.Listbox(self)
        for i in range (n):
            mycursor.execute("select * from clerk")
            b.insert(i,mycursor.fetchall()[i])
            b.grid(row=4,column=1)
        
        
        
class Projectpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        
        Updatelabel1=tk.Label(self,text="Enter Project ID",font=("times new roman",11),background="light blue")
        Updatelabel1.grid(row=0,column=0)
        Updatelabel2=tk.Label(self,text="Enter Project Name",font=("times new roman",11),background="light blue")
        Updatelabel2.grid(row=1,column=0)
        Updatelabel3=tk.Label(self,text="Enter Eligibility",font=("times new roman",11),background="light blue")
        Updatelabel3.grid(row=2,column=0)
        Updatelabel4=tk.Label(self,text="Enter Availability",font=("times new roman",11),background="light blue")
        Updatelabel4.grid(row=3,column=0)
        
        
        self.UpdateEntry1=tk.Entry(self)
        self.UpdateEntry2=tk.Entry(self)
        self.UpdateEntry3=tk.Entry(self)
        self.UpdateEntry4=tk.Entry(self)
        self.UpdateEntry1.grid(row=0,column=1)
        self.UpdateEntry2.grid(row=1,column=1)
        self.UpdateEntry3.grid(row=2,column=1)
        self.UpdateEntry4.grid(row=3,column=1)
        
        Updatebutton=tk.Button(self,text="Add to database",command=self.addentry,font=("times new roman",11))
        Updatebutton.grid(row=1,column=8)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage),font=("times new roman",11))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=4,column=8)
        
        Viewbutton=tk.Button(self,text="Display values",command=self.disp,font=("times new roman",11))
        Viewbutton.grid(row=2,column=8)
        
    def addentry(self):
        proj_id = self.UpdateEntry1.get()
        proj_name = self.UpdateEntry2.get()
        elig = self.UpdateEntry3.get()
        avail = self.UpdateEntry4.get()
        mycursor.execute("insert into project value(%s,%s,%s,%s)",[str(proj_id),str(proj_name),str(elig),str(avail)])
        mydb.commit()        
        
    def disp(self):
        mycursor.execute("select count(*) from project")
        n=mycursor.fetchall()[0][0]
        b=tk.Listbox(self)
        for i in range (n):
            mycursor.execute("select * from project")
            b.insert(i,mycursor.fetchall()[i])
            b.grid(row=5,column=1)
        
        
class RemoveEntry(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        
        Tablelabel1=tk.Label(self,text="Enter name of Table You'd like to remove details of",font=("times new roman",11),background="light blue")
        Tablelabel1.grid(row=0,column=0)
        self.TableEntry1=tk.Entry(self)
        self.TableEntry1.grid(row=0,column=1)
        IDlabel1=tk.Label(self,text="Enter ID You'd like to remove details of",font=("times new roman",11),background="light blue")
        IDlabel1.grid(row=1,column=0)
        self.IDEntry1=tk.Entry(self)
        self.IDEntry1.grid(row=1,column=1)
        
        Updatebutton=tk.Button(self,text="Remove the entry",command=self.removeentry,font=("times new roman",11))
        Updatebutton.grid(row=1,column=8)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage),font=("times new roman",11))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=2,column=8)
        
    def removeentry(self):
        table = self.TableEntry1.get()
        idval = self.IDEntry1.get()
        mycursor.execute("show columns from employee")
        column=mycursor.fetchall()[0][0]
        if table=='employee':
            mycursor.execute("delete from employee where emp_id=%s",[str(idval)])
            mydb.commit()
        elif table=='clerk':
            mycursor.execute("delete from clerk where c_id=%s",[str(idval)])
            mydb.commit()
        elif table=='project':
            mycursor.execute("delete from project where project_id=%s",[str(idval)])
            mydb.commit()
        elif table=='payroll':
            mycursor.execute("delete from payroll where emp_id=%s",[str(idval)])
            mydb.commit()
        
class Payrollpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,background="light blue")
        
        Addlabel1=tk.Label(self,text="Enter Employee ID",font=("times new roman",11),background="light blue")
        Addlabel1.grid(row=0,column=0)
        Addlabel2=tk.Label(self,text="Enter Salary",font=("times new roman",11),background="light blue")
        Addlabel2.grid(row=1,column=0)
        Addlabel3=tk.Label(self,text="Enter Travel Allowance",font=("times new roman",11),background="light blue")
        Addlabel3.grid(row=2,column=0)
        Addlabel4=tk.Label(self,text="Enter House Rent Allowance",font=("times new roman",11),background="light blue")
        Addlabel4.grid(row=3,column=0)
        Addlabel5=tk.Label(self,text="Enter Medical Allowance",font=("times new roman",11),background="light blue")
        Addlabel5.grid(row=4,column=0)
        Addlabel6=tk.Label(self,text="Enter Type of Bonus",font=("times new roman",11),background="light blue")
        Addlabel6.grid(row=5,column=0)
        Addlabel7=tk.Label(self,text="Enter Bonus amount",font=("times new roman",11),background="light blue")
        Addlabel7.grid(row=6,column=0)
        Addlabel8=tk.Label(self,text="Enter Loan to be deducted",font=("times new roman",11),background="light blue")
        Addlabel8.grid(row=7,column=0)

        
        self.AddEntry1=tk.Entry(self)
        self.AddEntry2=tk.Entry(self)
        self.AddEntry3=tk.Entry(self)
        self.AddEntry4=tk.Entry(self)
        self.AddEntry5=tk.Entry(self)
        self.AddEntry6=tk.Entry(self)
        self.AddEntry7=tk.Entry(self)
        self.AddEntry8=tk.Entry(self)
 
        self.AddEntry1.grid(row=0,column=1)
        self.AddEntry2.grid(row=1,column=1)
        self.AddEntry3.grid(row=2,column=1)
        self.AddEntry4.grid(row=3,column=1)
        self.AddEntry5.grid(row=4,column=1)
        self.AddEntry6.grid(row=5,column=1)  
        self.AddEntry7.grid(row=6,column=1)
        self.AddEntry8.grid(row=7,column=1)
        
        Addbutton=tk.Button(self,text="Add to database",command=self.addentry,font=("times new roman",11))
        Addbutton.grid(row=1,column=8)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage),font=("times new roman",11))
        Backbutton.grid(row=0,column=8)
                
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy(),font=("times new roman",11))
        Exitbutton.grid(row=4,column=8)
        
        Viewbutton=tk.Button(self,text="Display values",command=self.disp,font=("times new roman",11))
        Viewbutton.grid(row=2,column=8)
        
    def addentry(self):
        emp_id = self.AddEntry1.get()
        basic_sal = self.AddEntry2.get()
        ta = self.AddEntry3.get()
        hra = self.AddEntry4.get()
        medical = self.AddEntry5.get()
        B_type = self.AddEntry6.get()
        b_amt = self.AddEntry7.get()
        loan = self.AddEntry8.get()
        Net_salary = int(basic_sal)+float(ta)+float(hra)+float(medical)+int(b_amt)-float(loan)
        mycursor.execute("insert into payroll values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[str(emp_id),int(basic_sal)
        ,float(ta),float(hra),float(medical),str(B_type),int(b_amt),float(loan),float(Net_salary)])
        mydb.commit()
    
    def disp(self):
        mycursor.execute("select count(*) from payroll")
        n=mycursor.fetchall()[0][0]
        b=tk.Listbox(self)
        for i in range (n):
            mycursor.execute("select * from payroll")
            b.insert(i,mycursor.fetchall()[i])
            b.grid(row=9,column=1)




        
app=mainframe()
app.mainloop()