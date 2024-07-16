from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DataBase import Database  



root = Tk ()
root.title('Employee Managent System')
root.geometry('1240x615+0+0')
root.resizable (False, False)
root.configure (bg='#900C3F')



db = Database("Employee.db")

name = StringVar ()
age = StringVar ()
job = StringVar ()
gender = StringVar()
email = StringVar() 
mobile =  StringVar()


# Add all of these variables to the Entry functions ,
# except the address function , 
#  it is not entry



logo = PhotoImage (file='Assets\\logo4.png')
lbl_logo= Label (root, image=logo, bg='#900C3F')
lbl_logo.place (x= 25 , y= 500 , width= 300 , height=110 )




#Entries Frame
entries_frame = Frame (root, bg='#900C3F')
entries_frame.place(x=1,y=1,width=360,height=510)
title = Label (entries_frame
               ,text='Employee Company'
               , font=('Calibri',18,'bold')
                  , bg = '#900C3F'
                  , fg = 'white' )
title.place (x=10, y=1)


def Name_of_the_employee() :
    lblName = Label (entries_frame
                    ,text="Name"
                    , font=('Calibri',16)
                    ,bg='#900C3F'
                ,fg='white' )

    lblName.place (x=10, y=50)

    global txtName
    txtName = Entry (entries_frame
                    ,textvariable=name 
                    , width=20
                    , font=('Calibri',16)
                    )

    txtName.place (x=120, y=50)

def Job_of_the_employee() :
    lbljob = Label(entries_frame
                ,text="Job"
                ,font=('Calibri',16)
                ,bg='#900C3F'
                ,fg='white' )

    lbljob.place (x=10, y=90)

    global txtjob
    txtjob = Entry (entries_frame 
                    ,textvariable= job
                    , width=20
                    , font=('Calibri',16)
                    )
    txtjob.place (x=120,y=90)


def Gender_of_the_employee() :
    lblGender = Label (entries_frame
                    , text="Gender"
                    , font=('Calibri', 16)
                    , bg='#900C3F' 
                    , fg = 'white')
    lblGender.place (x=10, y=130)


    global comboGender
    comboGender = ttk.Combobox(entries_frame 
                            , state= 'readonly'
                            , width= 18
                                , font=('Calibri', 16)
                    #    , bg='#2c3e5' 
                    #    , fg = 'white'
                    )

    comboGender['values'] = ("Male" , "Female")
    comboGender.place(x=120, y=130)


def Age_of_the_employee() :
    lblAge= Label(entries_frame
                ,text="Age"
                ,font=('Calibri',16)
                ,bg='#900C3F'
                ,fg='white' )

    lblAge.place (x=10, y=170)


    global txtAge
    txtAge = Entry (entries_frame
                    ,textvariable=age
                    , width=20
                    , font=('Calibri',16)
                    )
    txtAge.place (x=120,y=170)


def Email_of_the_employee() :
    lblemail= Label(entries_frame
                ,text="Email"
                ,font=('Calibri',16)
                ,bg='#900C3F'
                ,fg='white' )

    lblemail.place (x=10, y=210)

    global txtemail
    txtemail = Entry (entries_frame
                    ,textvariable=email
                    , width=20
                    , font=('Calibri',16)
                    )
    txtemail.place (x=120,y=210)

def MobilePhone_of_the_employee() :
    lblcontact= Label(entries_frame
                ,text="Mobile"
                ,font=('Calibri',16)
                ,bg='#900C3F'
                ,fg='white' )

    lblcontact.place (x=10, y=250)


    global txtcontact
    txtcontact = Entry (entries_frame
                        , textvariable=mobile
                    , width=20
                    , font=('Calibri',16)
                    )
    txtcontact.place (x=120,y=250)



def Address_of_the_employee() :
    lbladdress= Label(entries_frame
                ,text="Address"
                ,font=('Calibri',16)
                ,bg='#900C3F'
                ,fg='white' )

    lbladdress.place (x=10, y=290)
     


    global txtaddress
    txtaddress = Text(entries_frame
                    , width= 30
                    ,height=2
                    ,font=('Calibri',16))

    txtaddress.place(x= 10 , y= 330)




if True : 
    Name_of_the_employee()
    Job_of_the_employee()
    Gender_of_the_employee() 
    Age_of_the_employee() 
    Email_of_the_employee()
    MobilePhone_of_the_employee()
    Address_of_the_employee() 


#  [Define]  Hide and Show Buttons
def Hide_button():
    def hide():
        root.geometry("360x515+0+0")

    btnhide = Button(entries_frame,text='HIDE'
                 , cursor='hand2'
                 , command=hide
                 , bg='white'
                 , bd = 1
                 , relief=SOLID) 


    btnhide.place (x=270,y=10)


def Show_button() : 
    def show():

        # to resize the window to the previous basic geometry
        root.geometry ('1240x615+0+0')





    btnshow = Button(entries_frame
                    , text='SHOW'
                    , cursor='hand2'
                    , command=show
                    , bg='white'
                    , bd = 1
                    , relief=SOLID) 

    btnshow.place (x=310, y=10)



if True :
    Hide_button()
    Show_button() 






# Free the fields after addding the user 
# to overcome the display issue

def Clear():
    name.set("") 
    age.set("") 
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    comboGender.set("")
    txtaddress.delete(1.0, END)






def getData(event):
    # to get data or show it in the boxes which were pre-specified to it
    selected_row = tv.focus()  
    data = tv.item(selected_row) 


    global row
    # to retrive the values of the data only
    # not keys
    # 

    row = data["values"]
    name.set(row[1]) #put name in field 1
    age.set(row [2])
    job.set(row [3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])

    txtaddress.delete(1.0, END)
    # insert row 7 
    txtaddress.insert(END, row[7])





def displayAll():
    # tv --> tree view (the table of the DB)


    # children --> the stored data itself
    # delete everything 
    tv.delete(*tv.get_children())

    # from our Database
    # to retrive everything of the database

    for row in db.fetch():
        tv.insert("",END, values=row)


# to make sure that every time your data 
# is up to date
# delete then retrive every time


def delete():


    # the error was : you must call the getdata function
    # to declare "row" variable


    # who is row
    if True :
        selected_row = tv.focus()  
        data = tv.item(selected_row)
        row = data["values"]


    #   to remove using the ID 
    #   remember : row [0] means the first col
    db.remove(row[0])
    Clear ()
    #   to update the data after removing
    displayAll()




def update() :
    # check for empty fiels first

    if (txtName.get() == "" 
        or txtAge.get() == "" 
        or txtjob.get() == "" 
        or txtcontact.get() == "" 
        or txtemail.get() == "" 
        or comboGender.get() == "" 
        or txtaddress.get(1.0 , END) == "" ):

        messagebox.showerror("Error", "Please Fill all the Entries" )
        return
    

    db.update(row[0]
              ,txtName.get()
            , txtAge.get()
            , txtjob.get()
            , txtemail.get()
            , comboGender.get()
            , txtcontact.get()
            , txtaddress.get(1.0 , END)
            )
    
    

    messagebox.showinfo('Success', 'The data of the employee has been updated recently' )
    Clear ()
    displayAll()





def add_employee() :

    # check for empty fiels first

    if (txtName.get() == "" 
        or txtAge.get() == "" 
        or txtjob.get() == "" 
        or txtcontact.get() == "" 
        or txtemail.get() == "" 
        or comboGender.get() == "" 
        or txtaddress.get(1.0 , END) == "" ):

        messagebox.showerror("Error", "Please Fill all the Entries , there is a missing one" )
        return


    # then add the values entered by the
    # use to the database
    db.insert(

        txtName.get()
        , txtAge.get()
        , txtjob.get()
        , txtemail.get()
        , comboGender.get()
        , txtcontact.get()
        , txtaddress.get(1.0 , END)

    )

    messagebox.showinfo("success" , "New employee has been added recently")
    Clear()
    displayAll()





# we must take the functions to 
# the buttons







# Buttons Frame
btn_frame = Frame (entries_frame,bg='#900C3F',bd=1,relief=SOLID)
btn_frame.place (x=10, y=400, width=335, height=100)


def Add_button() :
        
    btnAdd = Button (btn_frame,
                        text='Add Details',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#30ECCB',
                        bd=0 ,

                        command = add_employee
    ).place (x=4, y=5)



    # btnAdd.place (x=4, y=5)




def Edit_button() :
    btnEdit= Button (btn_frame,
            text='Update Details',
            width=14,
            height=1,
            font=('Calibri',16),
            fg='white',
            bg='#1B7565',
            bd=0 ,

            command = update
    ).place (x=4,y=50)

    # btnEdit.place (x=4,y=50)




# select the row then delete it 
def Delete_button() :
    btnDelete = Button (btn_frame,
                text='Delete Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#7F7F7F',
                bd=0 , 


                command= delete
    ). place (x=170,y=5)




def Clear_button() :
    btnClear = Button(btn_frame,
                text='Clear Details',
                width=14,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#044136',
                bd=0 ,
                

                command= Clear
    ).place (x=170,y=50)


if True :
    Add_button()
    Edit_button()
    Delete_button()
    Clear_button()







# [Table Frame]
tree_frame = Frame (root, bg='white') 
tree_frame.place(x=365,y=1,width=875,height=610)
style= ttk.Style()
style.configure ("mystyle.Treeview"
                 , font=('Calibri',13)
                 , rowheight=50)

style.configure("mystyle.Treeview.Heading"
                , font=('Calibri',13)
                )
tv = ttk.Treeview (tree_frame
                   , columns=(1,2,3,4,5,6,7,8)
                   , style="mystyle.Treeview" 
                   
                   )

def Constructing_the_table() :
    if True : 
        tv.heading("1", text="ID")
        tv.column ("1",width="40")


    if True : 
        tv.heading ("2", text="Name") 
        tv.column ("2",width="140")


    # tv.heading("2", text="Name")
    # tv.column("2",width="140")

    if True : 
        tv.heading("3", text="Age")
        tv.column("3",width="50")


    if True : 
        tv.heading("4", text="Job")
        tv.column("4",width="120")


    if True : 
        tv.heading("5", text="Email")
        tv.column("5",width="150")


    if True : 
        tv.heading("6", text="Gender")
        tv.column("6",width="90")

    if True : 
        tv.heading ("7", text="Mobile")
        tv.column("7",width="150")

    if True : 
        tv.heading ("8", text="Address")
        tv.column("8",width="150")


    # to show the headings correctly
    tv['show'] = 'headings'


    # tv.pack()
    tv.place(x = 1 , y = 1 , height= 610 , width= 875)


if True :
    Constructing_the_table()
    


if True :
    # to show the data in the table
    displayAll()
    root.mainloop() 