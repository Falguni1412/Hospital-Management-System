import tkinter as tk
from tkinter import messagebox, ttk, Frame, PhotoImage, LEFT
import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk, Frame, PhotoImage, LEFT
import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk
import random
import time
import datetime

# Dummy credentials for demonstration
USERNAME = "admin"
PASSWORD = "password123"

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Page")
        self.window.geometry("1280x700+0+0")
        
        # Load background image and keep a reference
        self.backgroundImage = ImageTk.PhotoImage(file=('bg.jpg'))
        self.bgLabel = Label(window, image=self.backgroundImage)
        self.bgLabel.place(x=0, y=0)  # Set the background size and position

        # Create login frame
        self.loginFrame = Frame(window, bg='white')
        self.loginFrame.place(x=400, y=150)

        # Load and place logo image
        self.logoImage = PhotoImage(file='logo.png')  # Ensure you have a logo.png file
        self.logoLabel = tk.Label(self.loginFrame, image=self.logoImage, bg='white')
        self.logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

        # Load and place username label with icon
        self.usernameImage = PhotoImage(file='user.png')  # Ensure you have a user.png file
        self.usernameLabel = tk.Label(self.loginFrame, image=self.usernameImage, text='Username', compound=LEFT,
                                      font=('times new roman', 20, 'bold'), bg='white')
        self.usernameLabel.grid(row=1, column=0, pady=10, padx=20)

        # Create and place entry for username
        self.usernameEntry = tk.Entry(self.loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
        self.usernameEntry.grid(row=1, column=1, pady=10, padx=20)

        # Load and place password label with icon
        self.passwordImage = PhotoImage(file='password.png')  # Ensure you have a password.png file
        self.passwordLabel = tk.Label(self.loginFrame, image=self.passwordImage, text='Password', compound=LEFT,
                                      font=('times new roman', 20, 'bold'), bg='white')
        self.passwordLabel.grid(row=2, column=0, pady=10, padx=20)

        # Create and place entry for password
        self.passwordEntry = tk.Entry(self.loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue', show='*')
        self.passwordEntry.grid(row=2, column=1, pady=10, padx=20)

        # Create and place login button
        self.loginButton = tk.Button(self.loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15,
                                     fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                                     activeforeground='white', cursor='hand2', command=self.login)
        self.loginButton.grid(row=3, column=1, pady=10)

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        # Validate credentials
        if username == USERNAME and password == PASSWORD:
            messagebox.showinfo("Login Success", "Welcome to the system!")
            self.window.destroy()  # Close the login window
            self.open_hospital_management()  # Open the hospital management window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_hospital_management(self):
        # Create a new root window for the hospital management system
        new_root = tk.Tk()
        HospitalManagement(new_root)
        new_root.mainloop()  # Start the new mainloop for the hospital management window


class HospitalManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        # Variables
        self.Nametable = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.nooftab = StringVar()
        self.lot = StringVar()
        self.issuedate = StringVar()
        self.issuedate1 = StringVar()
        self.DDose = StringVar()
        self.SE = StringVar()
        self.info = StringVar()
        self.BP = StringVar()
        self.StorageAdvice = StringVar()
        self.Medication = StringVar()
        self.PatientID = StringVar()
        self.NHS = StringVar()
        self.PatientName = StringVar()
        self.DOB = StringVar()
        self.Address = StringVar()
        
        # Title Label
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframes
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=120, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # Button Frame
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # Details Frame
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)
        # Labels and Entries for patient info
        lblNameTable = Label(DataframeLeft, text="Names of Tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTable.grid(row=0, column=0)

        comNameTable = ttk.Combobox(DataframeLeft, textvariable=self.Nametable, state="readonly", font=("times new roman", 12, "bold"), width=33)
        comNameTable["values"] = ("abc", "efg", "eif", "fhu", "fgj", "hjg")
        comNameTable.current(0)
        comNameTable.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Reference no.", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Dose", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblnooftab = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="No of tablets", padx=2, pady=6)
        lblnooftab.grid(row=3, column=0, sticky=W)
        txtnooftab = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.nooftab, width=35)
        txtnooftab.grid(row=3, column=1)

        lbllot = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Lot:", padx=2, pady=6)
        lbllot.grid(row=4, column=0, sticky=W)
        txtlot = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.lot, width=35)
        txtlot.grid(row=4, column=1)

        lblissuedate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Issue date:", padx=2, pady=6)
        lblissuedate.grid(row=5, column=0, sticky=W)
        txtissuedate = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.issuedate, width=35)
        txtissuedate.grid(row=5, column=1)

        lblissuedate1 = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Expiry date:", padx=2, pady=6)
        lblissuedate1.grid(row=6, column=0, sticky=W)
        txtissuedate1 = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.issuedate1, width=35)
        txtissuedate1.grid(row=6, column=1)

        lblDDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Daily Dose", padx=2, pady=4)
        lblDDose.grid(row=7, column=0, sticky=W)
        txtDDose = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.DDose, width=35)
        txtDDose.grid(row=7, column=1)

        lblSE = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Side Effect", padx=2, pady=4)
        lblSE.grid(row=8, column=0, sticky=W)
        txtSE = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.SE, width=35)
        txtSE.grid(row=8, column=1)

        # New fields
        lblinfo = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Further Information", padx=2)
        lblinfo.grid(row=0, column=2, sticky=W)
        txtinfo = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.info, width=35)
        txtinfo.grid(row=0, column=3)

        lblBP = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBP.grid(row=1, column=2, sticky=W)
        txtBP = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.BP, width=35)
        txtBP.grid(row=1, column=3)

        lblStorageAdvice = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Storage Advice", padx=2, pady=6)
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        txtStorageAdvice = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.Medication, width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientID = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient ID", padx=2, pady=6)
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.PatientID, width=35)
        txtPatientID.grid(row=4, column=3)

        lblNHS = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNHS.grid(row=5, column=2, sticky=W)
        txtNHS = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.NHS, width=35)
        txtNHS.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Date of Birth", padx=2, pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.DOB, width=35)
        txtDOB.grid(row=7, column=3)

        lblAddress = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblAddress.grid(row=8, column=2, sticky=W)
        txtAddress = Entry(DataframeLeft, font=("times new roman", 13, "bold"), textvariable=self.Address, width=35)
        txtAddress.grid(row=8, column=3)


        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=43, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # Button Widgets
        btnPData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6,command=self.iPrescriptionData)
        btnPData.grid(row=0, column=1)

        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6,command=self.iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6,command=self.idelete)
        btnDelete.grid(row=0, column=2)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6,command=self.iclear)
        btnClear.grid(row=0, column=3)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6,command=self.update)
        btnUpdate.grid(row=0, column=4)

        btnexit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("times new roman", 12, "bold"), width=27, padx=2, pady=6, command=self.root.quit)
        btnexit.grid(row=0, column=5)

                # Table for details

        
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("Nametable", "ref", "Dose", "nooftab", "lot", "issuedate", "issuedate1", "DDose", "SE", "info", "BP", "StorageAdvice", "Medication", "PatientID", "NHS", "PatientName", "DOB", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("Nametable", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("nooftab", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("issuedate1", text="Expiry Date")
        self.hospital_table.heading("DDose", text="Daily Dose")
        self.hospital_table.heading("StorageAdvice", text="Storage Advice")
        self.hospital_table.heading("NHS", text="NHS Number")
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("DOB", text="DOB")
        self.hospital_table.heading("Address", text="Patient Address")
        self.hospital_table.heading("SE", text="Side Effects")
        self.hospital_table.heading("info", text="Additional Info")
        self.hospital_table.heading("BP", text="Blood Pressure")
        self.hospital_table.heading("Medication", text="Medication Info")
        self.hospital_table.heading("PatientID", text="Patient ID")


        self.hospital_table["show"] = "headings"

        self.hospital_table.column("Nametable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("nooftab", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("issuedate1", width=100)
        self.hospital_table.column("DDose", width=100)
        self.hospital_table.column("StorageAdvice", width=100)
        self.hospital_table.column("NHS", width=100)
        self.hospital_table.column("PatientName", width=100)
        self.hospital_table.column("DOB", width=100)
        self.hospital_table.column("Address", width=100)
        self.hospital_table.column("SE", width=100)
        self.hospital_table.column("info", width=100)
        self.hospital_table.column("BP", width=100)
        self.hospital_table.column("Medication", width=100)
        self.hospital_table.column("PatientID", width=100)


        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # Prescription Data Function
    def iPrescriptionData(self):
        if self.Nametable.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
               self.Nametable.get(),
               self.ref.get(),
               self.Dose.get(),
               self.nooftab.get(),
               self.lot.get(),
               self.issuedate.get(),
               self.issuedate1.get(),
               self.DDose.get(),
               self.SE.get(),
               self.info.get(),
               self.BP.get(),
               self.Medication.get(),
               self.PatientID.get(),
               self.NHS.get(),
               self.PatientName.get(),
               self.DOB.get(),
               self.Address.get(),
               self.StorageAdvice.get()
           ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("sucess","inserted sucessfullly")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())  # Clear existing data
            for i in rows:
                self.hospital_table.insert("", END, values=i)  # Insert each row into the Treeview
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
            cursor_row = self.hospital_table.focus()  # Get the focused/selected row
            contents = self.hospital_table.item(cursor_row)  # Get the content of the selected row
            row = contents['values']  # Extract the values from the selected row

            # Now populate the data into the entry fields
            try:
                self.Nametable.set(row[0])        # First column: Name of the medicine/table
                self.ref.set(row[1])              # Second column: Reference number
                self.Dose.set(row[2])             # Third column: Dose
                self.nooftab.set(row[3])          # Fourth column: Number of tablets
                self.lot.set(row[4])              # Fifth column: Lot number
                self.issuedate.set(row[5])        # Sixth column: Issue date
                self.issuedate1.set(row[6])       # Seventh column: Expiry date or another date
                self.DDose.set(row[7])            # Eighth column: Daily dose
                self.SE.set(row[8])               # Ninth column: Side effects
                self.info.set(row[9])             # Tenth column: Additional information
                self.BP.set(row[10])              # Eleventh column: Blood pressure (if applicable)
                self.Medication.set(row[11])      # Twelfth column: Medication details
                self.PatientID.set(row[12])       # Thirteenth column: Patient ID
                self.NHS.set(row[13])             # Fourteenth column: NHS number (if applicable)
                self.PatientName.set(row[14])     # Fifteenth column: Patient's name
                self.DOB.set(row[15])             # Sixteenth column: Date of birth
                self.Address.set(row[16])         # Seventeenth column: Address
                self.StorageAdvice.set(row[17])   # Eighteenth column: Storage advice
            except IndexError:
                print("Error: Row data might be incomplete or not matching the table structure.")

    def update(self):
            if self.PatientID.get() == "":
                messagebox.showerror("Error", "Select a patient to update")
                return  # Ensure to exit if no PatientID is provided

            # Debugging output
            print("Updating record for Patient ID:", self.PatientID.get())
            print("New Values:",
                self.Nametable.get(), self.ref.get(), self.Dose.get(), self.nooftab.get(), 
                self.lot.get(), self.issuedate.get(), self.issuedate1.get(), self.DDose.get(), 
                self.SE.get(), self.info.get(), self.BP.get(), self.StorageAdvice.get(), 
                self.Medication.get(), self.NHS.get(), self.PatientName.get(), 
                self.DOB.get(), self.Address.get())

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",  # Corrected parameter name
                    password="", 
                    database="mydata"
                )
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "UPDATE hospital SET Nametable=%s, ref=%s, Dose=%s, nooftab=%s, lot=%s, issuedate=%s, "
                    "issuedate1=%s, DDose=%s, SE=%s, info=%s, BP=%s, StorageAdvice=%s, Medication=%s, NHS=%s, "
                    "PatientName=%s, DOB=%s, Address=%s WHERE PatientID=%s",
                    (
                        self.Nametable.get(), self.ref.get(), self.Dose.get(), self.nooftab.get(), 
                        self.lot.get(), self.issuedate.get(), self.issuedate1.get(), self.DDose.get(), 
                        self.SE.get(), self.info.get(), self.BP.get(), self.StorageAdvice.get(), 
                        self.Medication.get(), self.NHS.get(), self.PatientName.get(), 
                        self.DOB.get(), self.Address.get(), self.PatientID.get()
                    )
                )

                conn.commit()

                # Check if any rows were affected
                if my_cursor.rowcount > 0:
                    print(f"Rows affected: {my_cursor.rowcount}")
                    messagebox.showinfo("Success", "Data updated successfully")
                else:
                    print("No rows were updated.")
                    messagebox.showwarning("Warning", "No data was updated; please check your input.")

                conn.close()
                self.fetch_data()  # Refresh the data after update
                self.iclear()  # Clear the input fields
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error updating data: {err}")
            finally:
                if conn.is_connected():
                    conn.close()  # Ensure connection is closed in case of an error



    def iPrescription(self):
        # Clear previous data in the text widget
        
        
        # Insert prescription details into the text widget
        self.txtPrescription.insert(END, "Name of tablets:\t\t\t" + self.Nametable.get() + "\n")
        self.txtPrescription.insert(END, "Reference:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t" + self.nooftab.get() + "\n")
        self.txtPrescription.insert(END, "Lot Number:\t\t\t" + self.lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + self.issuedate1.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effects:\t\t\t" + self.SE.get() + "\n")
        self.txtPrescription.insert(END, "Additional Info:\t\t" + self.info.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BP.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Medication:\t\t\t" + self.Medication.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t\t" + self.NHS.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + self.DOB.get() + "\n")
        self.txtPrescription.insert(END, "Address:\t\t\t" + self.Address.get() + "\n")

    def idelete(self):
    # Clear all input fields
        self.Nametable.set("")
        self.ref.set("")
        self.Dose.set("")
        self.nooftab.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.issuedate1.set("")
        self.DDose.set("")
        self.SE.set("")
        self.info.set("")
        self.BP.set("")
        self.StorageAdvice.set("")
        self.Medication.set("")
        self.NHS.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")
        
        # Clear the prescription text area
        self.txtPrescription.delete(1.0, END)

        # Optionally, display a message to confirm deletion
        messagebox.showinfo("Deleted", "Prescription data has been deleted.")

    def iclear(self):
        # Clear specific input fields
        self.Nametable.set("")
        self.ref.set("")
        self.Dose.set("")
        self.nooftab.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.issuedate1.set("")
        self.DDose.set("")
        self.SE.set("")
        self.info.set("")
        self.BP.set("")
        self.StorageAdvice.set("")
        self.Medication.set("")
        self.NHS.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")
        
        # Optionally, you can also clear the prescription text area
        self.txtPrescription.delete(1.0, END)
        
        # Display a message to confirm clearing
        messagebox.showinfo("Cleared", "Prescription data has been cleared.")


if __name__ == "__main__":
    window = tk.Tk()
    app = LoginPage(window)
    window.mainloop()
