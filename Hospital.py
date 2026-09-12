import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

USERNAME = "admin"
PASSWORD = "password123"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mydata"
}


# ============================================================
# COLORS
# ============================================================

BG = "#F4F7FB"
CARD = "#FFFFFF"
NAVY = "#102A43"
NAVY_2 = "#173F5F"
TEAL = "#16B8A6"
TEAL_DARK = "#0E9183"
TEXT = "#243B53"
MUTED = "#7B8794"
BORDER = "#D9E2EC"
WHITE = "#FFFFFF"
RED = "#E55353"
GREEN = "#20A464"
ORANGE = "#F59E0B"
LIGHT_TEAL = "#E8F8F5"
LIGHT_BLUE = "#EAF2F8"


# ============================================================
# DATABASE HELPER
# ============================================================

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


# ============================================================
# LOGIN PAGE
# ============================================================

class LoginPage:

    def __init__(self, window):

        self.window = window

        self.window.title("MediCare | Secure Login")
        self.window.geometry("1200x720")
        self.window.minsize(1000, 650)
        self.window.configure(bg=BG)

        self.setup_styles()
        self.build_login()

    # --------------------------------------------------------
    # STYLES
    # --------------------------------------------------------

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Login.TEntry",
            fieldbackground=WHITE,
            background=WHITE,
            foreground=TEXT,
            borderwidth=0,
            padding=12,
            font=("Segoe UI", 12)
        )

        style.configure(
            "Login.TButton",
            background=TEAL,
            foreground=WHITE,
            font=("Segoe UI Semibold", 12),
            borderwidth=0,
            padding=12
        )

        style.map(
            "Login.TButton",
            background=[
                ("active", TEAL_DARK),
                ("pressed", TEAL_DARK)
            ]
        )

    # --------------------------------------------------------
    # LOGIN UI
    # --------------------------------------------------------

    def build_login(self):

        main = tk.Frame(
            self.window,
            bg=BG
        )
        main.pack(fill="both", expand=True)

        # Left branding section
        left = tk.Frame(
            main,
            bg=NAVY,
            width=500
        )
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        # Decorative circle
        circle = tk.Canvas(
            left,
            bg=NAVY,
            highlightthickness=0
        )
        circle.pack(fill="both", expand=True)

        circle.create_oval(
            -100, -100, 330, 330,
            fill=NAVY_2,
            outline=""
        )

        circle.create_oval(
            300, 500, 700, 900,
            fill=TEAL_DARK,
            outline=""
        )

        circle.create_text(
            55,
            185,
            anchor="w",
            text="✚",
            fill=TEAL,
            font=("Segoe UI", 54, "bold")
        )

        circle.create_text(
            55,
            270,
            anchor="w",
            text="MediCare",
            fill=WHITE,
            font=("Segoe UI", 34, "bold")
        )

        circle.create_text(
            58,
            325,
            anchor="w",
            text="Hospital Management",
            fill="#B8C7D9",
            font=("Segoe UI", 15)
        )

        circle.create_text(
            58,
            370,
            anchor="w",
            text="Smart • Simple • Secure",
            fill=TEAL,
            font=("Segoe UI Semibold", 13)
        )

        # Right login area
        right = tk.Frame(
            main,
            bg=BG
        )
        right.pack(
            side="right",
            fill="both",
            expand=True
        )

        card = tk.Frame(
            right,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=430,
            height=470
        )

        tk.Label(
            card,
            text="Welcome back",
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI", 27, "bold")
        ).pack(
            pady=(50, 5)
        )

        tk.Label(
            card,
            text="Sign in to access your hospital dashboard",
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            pady=(0, 35)
        )

        # Username
        tk.Label(
            card,
            text="USERNAME",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 9)
        ).pack(
            anchor="w",
            padx=45
        )

        self.usernameEntry = ttk.Entry(
            card,
            style="Login.TEntry"
        )
        self.usernameEntry.pack(
            fill="x",
            padx=45,
            pady=(7, 20)
        )

        # Password
        tk.Label(
            card,
            text="PASSWORD",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 9)
        ).pack(
            anchor="w",
            padx=45
        )

        self.passwordEntry = ttk.Entry(
            card,
            style="Login.TEntry",
            show="●"
        )
        self.passwordEntry.pack(
            fill="x",
            padx=45,
            pady=(7, 25)
        )

        self.loginButton = ttk.Button(
            card,
            text="SIGN IN  →",
            style="Login.TButton",
            command=self.login
        )
        self.loginButton.pack(
            fill="x",
            padx=45,
            pady=5
        )

        tk.Label(
            card,
            text="Demo access: admin / password123",
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 9)
        ).pack(
            pady=(20, 0)
        )

        self.usernameEntry.focus()

        self.window.bind(
            "<Return>",
            lambda event: self.login()
        )

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    def login(self):

        username = self.usernameEntry.get().strip()
        password = self.passwordEntry.get()

        if username == USERNAME and password == PASSWORD:

            messagebox.showinfo(
                "Login Successful",
                "Welcome to the MediCare Hospital Dashboard."
            )

            self.window.destroy()

            new_root = tk.Tk()
            HospitalManagement(new_root)
            new_root.mainloop()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            self.passwordEntry.delete(0, tk.END)
            self.passwordEntry.focus()


# ============================================================
# HOSPITAL MANAGEMENT
# ============================================================

class HospitalManagement:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "MediCare | Hospital Management Dashboard"
        )

        self.root.geometry("1500x850")
        self.root.minsize(1150, 700)

        self.root.configure(bg=BG)

        self.create_variables()
        self.setup_styles()
        self.build_interface()

        self.fetch_data()

    # --------------------------------------------------------
    # VARIABLES
    # --------------------------------------------------------

    def create_variables(self):

        self.Nametable = tk.StringVar()
        self.ref = tk.StringVar()
        self.Dose = tk.StringVar()
        self.nooftab = tk.StringVar()
        self.lot = tk.StringVar()
        self.issuedate = tk.StringVar()
        self.issuedate1 = tk.StringVar()
        self.DDose = tk.StringVar()
        self.SE = tk.StringVar()
        self.info = tk.StringVar()
        self.BP = tk.StringVar()
        self.StorageAdvice = tk.StringVar()
        self.Medication = tk.StringVar()
        self.PatientID = tk.StringVar()
        self.NHS = tk.StringVar()
        self.PatientName = tk.StringVar()
        self.DOB = tk.StringVar()
        self.Address = tk.StringVar()

        self.status_text = tk.StringVar(
            value="Ready"
        )

    # --------------------------------------------------------
    # STYLES
    # --------------------------------------------------------

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Modern.TEntry",
            fieldbackground=WHITE,
            background=WHITE,
            foreground=TEXT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            padding=8,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Modern.TCombobox",
            fieldbackground=WHITE,
            background=WHITE,
            foreground=TEXT,
            bordercolor=BORDER,
            padding=7,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Modern.Treeview",
            background=WHITE,
            fieldbackground=WHITE,
            foreground=TEXT,
            rowheight=34,
            borderwidth=0,
            font=("Segoe UI", 9)
        )

        style.configure(
            "Modern.Treeview.Heading",
            background=NAVY,
            foreground=WHITE,
            font=("Segoe UI Semibold", 9),
            padding=10
        )

        style.map(
            "Modern.Treeview",
            background=[
                ("selected", TEAL)
            ],
            foreground=[
                ("selected", WHITE)
            ]
        )

    # --------------------------------------------------------
    # MAIN INTERFACE
    # --------------------------------------------------------

    def build_interface(self):

        self.build_topbar()

        self.build_sidebar()

        self.build_content()

        self.build_statusbar()

    # --------------------------------------------------------
    # TOP BAR
    # --------------------------------------------------------

    def build_topbar(self):

        top = tk.Frame(
            self.root,
            bg=WHITE,
            height=75
        )
        top.pack(
            side="top",
            fill="x"
        )
        top.pack_propagate(False)

        tk.Label(
            top,
            text="MediCare",
            bg=WHITE,
            fg=NAVY,
            font=("Segoe UI", 21, "bold")
        ).pack(
            side="left",
            padx=(30, 5)
        )

        tk.Label(
            top,
            text="Hospital Management",
            bg=WHITE,
            fg=TEAL,
            font=("Segoe UI Semibold", 10)
        ).pack(
            side="left",
            pady=(10, 0)
        )

        # Right side
        profile = tk.Frame(
            top,
            bg=WHITE
        )
        profile.pack(
            side="right",
            padx=30
        )

        tk.Label(
            profile,
            text="●",
            bg=WHITE,
            fg=GREEN,
            font=("Segoe UI", 15)
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            profile,
            text="Administrator",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI Semibold", 10)
        ).pack(
            side="left"
        )

    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    def build_sidebar(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=NAVY,
            width=220
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="WORKSPACE",
            bg=NAVY,
            fg="#829AB1",
            font=("Segoe UI Semibold", 8)
        ).pack(
            anchor="w",
            padx=25,
            pady=(35, 15)
        )

        self.sidebar_button(
            "▣   Dashboard",
            self.show_dashboard,
            active=True
        )

        self.sidebar_button(
            "♙   Patient Records",
            self.show_records
        )

        self.sidebar_button(
            "▤   Prescription",
            self.show_prescription
        )

        self.sidebar_button(
            "⚙   System",
            self.show_system
        )

        # Bottom information
        bottom = tk.Frame(
            self.sidebar,
            bg=NAVY
        )
        bottom.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=25
        )

        tk.Label(
            bottom,
            text="DATABASE",
            bg=NAVY,
            fg="#829AB1",
            font=("Segoe UI Semibold", 8)
        ).pack(
            anchor="w"
        )

        tk.Label(
            bottom,
            text="●  MySQL Connected",
            bg=NAVY,
            fg="#6EE7B7",
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

    def sidebar_button(
        self,
        text,
        command,
        active=False
    ):

        bg = TEAL if active else NAVY

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            bg=bg,
            fg=WHITE,
            activebackground=TEAL_DARK,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            font=("Segoe UI Semibold", 10),
            cursor="hand2"
        )

        button.pack(
            fill="x",
            ipady=12,
            pady=2
        )

    # --------------------------------------------------------
    # CONTENT
    # --------------------------------------------------------

    def build_content(self):

        self.content = tk.Frame(
            self.root,
            bg=BG
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.build_dashboard()

    # --------------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------------

    def build_dashboard(self):

        self.clear_content()

        # Header
        header = tk.Frame(
            self.content,
            bg=BG
        )
        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        tk.Label(
            header,
            text="Patient Management",
            bg=BG,
            fg=NAVY,
            font=("Segoe UI", 25, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="Manage patient prescriptions and medical records",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        # Main form card
        card = tk.Frame(
            self.content,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

        # Notebook
        notebook = ttk.Notebook(card)
        notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        patient_tab = tk.Frame(
            notebook,
            bg=CARD
        )

        prescription_tab = tk.Frame(
            notebook,
            bg=CARD
        )

        notebook.add(
            patient_tab,
            text="  Patient & Medicine  "
        )

        notebook.add(
            prescription_tab,
            text="  Prescription Preview  "
        )

        self.build_patient_form(patient_tab)
        self.build_prescription_tab(prescription_tab)

        # Buttons
        self.build_action_buttons(card)

    # --------------------------------------------------------
    # PATIENT FORM
    # --------------------------------------------------------

    def build_patient_form(self, parent):

        # Scrollable canvas
        canvas = tk.Canvas(
            parent,
            bg=CARD,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            parent,
            orient="vertical",
            command=canvas.yview
        )

        form = tk.Frame(
            canvas,
            bg=CARD
        )

        form.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=form,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Make columns stretch
        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        # Section
        self.section_title(
            form,
            "PATIENT DETAILS",
            0
        )

        self.add_field(
            form,
            "Patient ID",
            self.PatientID,
            1,
            0,
            required=True
        )

        self.add_field(
            form,
            "Patient Name",
            self.PatientName,
            1,
            2
        )

        self.add_field(
            form,
            "NHS Number",
            self.NHS,
            2,
            0
        )

        self.add_field(
            form,
            "Date of Birth",
            self.DOB,
            2,
            2,
            placeholder="DD-MM-YYYY"
        )

        self.add_field(
            form,
            "Blood Pressure",
            self.BP,
            3,
            0,
            placeholder="120/80"
        )

        self.add_field(
            form,
            "Address",
            self.Address,
            3,
            2
        )

        # Medicine
        self.section_title(
            form,
            "MEDICATION DETAILS",
            4
        )

        self.add_combobox(
            form,
            "Name of Tablets",
            self.Nametable,
            5,
            0
        )

        self.add_field(
            form,
            "Reference No.",
            self.ref,
            5,
            2
        )

        self.add_field(
            form,
            "Dose",
            self.Dose,
            6,
            0,
            placeholder="e.g. 500 mg"
        )

        self.add_field(
            form,
            "No. of Tablets",
            self.nooftab,
            6,
            2
        )

        self.add_field(
            form,
            "Lot Number",
            self.lot,
            7,
            0
        )

        self.add_field(
            form,
            "Daily Dose",
            self.DDose,
            7,
            2
        )

        # Dates
        self.add_field(
            form,
            "Issue Date",
            self.issuedate,
            8,
            0,
            placeholder="DD-MM-YYYY"
        )

        self.add_field(
            form,
            "Expiry Date",
            self.issuedate1,
            8,
            2,
            placeholder="DD-MM-YYYY"
        )

        # Additional
        self.section_title(
            form,
            "MEDICAL INFORMATION",
            9
        )

        self.add_field(
            form,
            "Medication Info",
            self.Medication,
            10,
            0
        )

        self.add_field(
            form,
            "Side Effects",
            self.SE,
            10,
            2
        )

        self.add_field(
            form,
            "Storage Advice",
            self.StorageAdvice,
            11,
            0
        )

        self.add_field(
            form,
            "Further Information",
            self.info,
            11,
            2
        )

    # --------------------------------------------------------
    # SECTION TITLE
    # --------------------------------------------------------

    def section_title(
        self,
        parent,
        text,
        row
    ):

        frame = tk.Frame(
            parent,
            bg=CARD
        )

        frame.grid(
            row=row,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=20,
            pady=(18, 10)
        )

        tk.Frame(
            frame,
            bg=TEAL,
            width=4,
            height=24
        ).pack(
            side="left",
            padx=(0, 10)
        )

        tk.Label(
            frame,
            text=text,
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI Semibold", 10)
        ).pack(
            side="left"
        )

    # --------------------------------------------------------
    # FIELD
    # --------------------------------------------------------

    def add_field(
        self,
        parent,
        label,
        variable,
        row,
        column,
        placeholder=""
    ):

        container = tk.Frame(
            parent,
            bg=CARD
        )

        container.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=20,
            pady=7
        )

        tk.Label(
            container,
            text=label,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 9)
        ).pack(
            anchor="w"
        )

        entry = ttk.Entry(
            container,
            textvariable=variable,
            style="Modern.TEntry"
        )

        entry.pack(
            fill="x",
            pady=(5, 0)
        )

        if placeholder:

            # Small helper text
            tk.Label(
                container,
                text=placeholder,
                bg=CARD,
                fg=MUTED,
                font=("Segoe UI", 7)
            ).pack(
                anchor="w"
            )

    # --------------------------------------------------------
    # COMBOBOX
    # --------------------------------------------------------

    def add_combobox(
        self,
        parent,
        label,
        variable,
        row,
        column
    ):

        container = tk.Frame(
            parent,
            bg=CARD
        )

        container.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=20,
            pady=7
        )

        tk.Label(
            container,
            text=label,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 9)
        ).pack(
            anchor="w"
        )

        combo = ttk.Combobox(
            container,
            textvariable=variable,
            state="normal",
            style="Modern.TCombobox",
            values=(
                "Paracetamol",
                "Amoxicillin",
                "Azithromycin",
                "Ibuprofen",
                "Cetirizine",
                "Omeprazole",
                "Metformin",
                "Aspirin"
            )
        )

        combo.pack(
            fill="x",
            pady=(5, 0)
        )

    # --------------------------------------------------------
    # PRESCRIPTION TAB
    # --------------------------------------------------------

    def build_prescription_tab(self, parent):

        parent.grid_rowconfigure(
            0,
            weight=1
        )

        parent.grid_columnconfigure(
            0,
            weight=1
        )

        wrapper = tk.Frame(
            parent,
            bg=LIGHT_TEAL
        )

        wrapper.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=30
        )

        tk.Label(
            wrapper,
            text="PRESCRIPTION",
            bg=LIGHT_TEAL,
            fg=TEAL_DARK,
            font=("Segoe UI Semibold", 11)
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        tk.Label(
            wrapper,
            text="Digital Medical Prescription",
            bg=LIGHT_TEAL,
            fg=NAVY,
            font=("Segoe UI", 20, "bold")
        ).pack(
            anchor="w",
            padx=25
        )

        tk.Frame(
            wrapper,
            bg=TEAL,
            height=2
        ).pack(
            fill="x",
            padx=25,
            pady=15
        )

        self.txtPrescription = tk.Text(
            wrapper,
            bg=WHITE,
            fg=TEXT,
            font=("Consolas", 10),
            relief="flat",
            bd=0,
            padx=20,
            pady=20,
            wrap="word"
        )

        self.txtPrescription.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 25)
        )

        self.txtPrescription.insert(
            "1.0",
            "Select patient information and click\n"
            "\"Generate Prescription\" to preview it here."
        )

        self.txtPrescription.config(
            state="disabled"
        )

    # --------------------------------------------------------
    # ACTION BUTTONS
    # --------------------------------------------------------

    def build_action_buttons(self, parent):

        button_frame = tk.Frame(
            parent,
            bg=CARD
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.modern_button(
            button_frame,
            "Generate Prescription",
            self.iPrescription,
            TEAL
        ).pack(
            side="left",
            padx=5
        )

        self.modern_button(
            button_frame,
            "Save Record",
            self.iPrescriptionData,
            NAVY
        ).pack(
            side="left",
            padx=5
        )

        self.modern_button(
            button_frame,
            "Update",
            self.update,
            ORANGE
        ).pack(
            side="left",
            padx=5
        )

        self.modern_button(
            button_frame,
            "Clear",
            self.iclear,
            "#64748B"
        ).pack(
            side="left",
            padx=5
        )

        self.modern_button(
            button_frame,
            "Delete / Clear",
            self.idelete,
            RED
        ).pack(
            side="left",
            padx=5
        )

        self.modern_button(
            button_frame,
            "Exit",
            self.root.quit,
            "#334E68"
        ).pack(
            side="right",
            padx=5
        )

    def modern_button(
        self,
        parent,
        text,
        command,
        color
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=WHITE,
            activebackground=color,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            padx=18,
            pady=9,
            cursor="hand2",
            font=("Segoe UI Semibold", 9)
        )

    # --------------------------------------------------------
    # RECORDS PAGE
    # --------------------------------------------------------

    def show_records(self):

        self.clear_content()

        header = tk.Frame(
            self.content,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Label(
            header,
            text="Patient Records",
            bg=BG,
            fg=NAVY,
            font=("Segoe UI", 25, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="View all saved medical records from MySQL",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            pady=3
        )

        card = tk.Frame(
            self.content,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30)
        )

        # Search area
        search = tk.Frame(
            card,
            bg=CARD
        )

        search.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            search,
            text="Records",
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI Semibold", 12)
        ).pack(
            side="left"
        )

        tk.Button(
            search,
            text="↻ Refresh",
            command=self.fetch_data,
            bg=TEAL,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=15,
            pady=7,
            cursor="hand2",
            font=("Segoe UI Semibold", 9)
        ).pack(
            side="right"
        )

        self.create_table(card)

        self.fetch_data()

    # --------------------------------------------------------
    # CREATE TABLE
    # --------------------------------------------------------

    def create_table(self, parent):

        table_frame = tk.Frame(
            parent,
            bg=CARD
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "Nametable",
            "ref",
            "Dose",
            "nooftab",
            "lot",
            "issuedate",
            "issuedate1",
            "DDose",
            "SE",
            "info",
            "BP",
            "Medication",
            "PatientID",
            "NHS",
            "PatientName",
            "DOB",
            "Address",
            "StorageAdvice"
        )

        x_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal"
        )

        y_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical"
        )

        self.hospital_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Modern.Treeview",
            xscrollcommand=x_scroll.set,
            yscrollcommand=y_scroll.set
        )

        x_scroll.config(
            command=self.hospital_table.xview
        )

        y_scroll.config(
            command=self.hospital_table.yview
        )

        x_scroll.pack(
            side="bottom",
            fill="x"
        )

        y_scroll.pack(
            side="right",
            fill="y"
        )

        self.hospital_table.pack(
            fill="both",
            expand=True
        )

        headings = {
            "Nametable": "Tablet",
            "ref": "Reference",
            "Dose": "Dose",
            "nooftab": "Tablets",
            "lot": "Lot",
            "issuedate": "Issue Date",
            "issuedate1": "Expiry",
            "DDose": "Daily Dose",
            "SE": "Side Effects",
            "info": "Information",
            "BP": "Blood Pressure",
            "Medication": "Medication",
            "PatientID": "Patient ID",
            "NHS": "NHS No.",
            "PatientName": "Patient Name",
            "DOB": "DOB",
            "Address": "Address",
            "StorageAdvice": "Storage"
        }

        for column in columns:

            self.hospital_table.heading(
                column,
                text=headings[column]
            )

            self.hospital_table.column(
                column,
                width=120,
                minwidth=90
            )

        self.hospital_table.column(
            "PatientName",
            width=160
        )

        self.hospital_table.column(
            "Address",
            width=220
        )

        self.hospital_table.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

    # --------------------------------------------------------
    # PRESCRIPTION PAGE
    # --------------------------------------------------------

    def show_prescription(self):

        self.clear_content()

        header = tk.Frame(
            self.content,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Label(
            header,
            text="Prescription Center",
            bg=BG,
            fg=NAVY,
            font=("Segoe UI", 25, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="Generate and review digital prescriptions",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w"
        )

        card = tk.Frame(
            self.content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30)
        )

        self.txtPrescriptionPage = tk.Text(
            card,
            bg="#FBFEFD",
            fg=TEXT,
            font=("Consolas", 11),
            relief="flat",
            padx=30,
            pady=30
        )

        self.txtPrescriptionPage.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        self.txtPrescriptionPage.insert(
            "1.0",
            self.generate_prescription_text()
        )

        self.txtPrescriptionPage.config(
            state="disabled"
        )

        tk.Button(
            card,
            text="Generate Again",
            command=self.iPrescription,
            bg=TEAL,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=20,
            pady=9,
            cursor="hand2",
            font=("Segoe UI Semibold", 9)
        ).pack(
            pady=(0, 20)
        )

    # --------------------------------------------------------
    # SYSTEM PAGE
    # --------------------------------------------------------

    def show_system(self):

        self.clear_content()

        header = tk.Frame(
            self.content,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Label(
            header,
            text="System Information",
            bg=BG,
            fg=NAVY,
            font=("Segoe UI", 25, "bold")
        ).pack(
            anchor="w"
        )

        card = tk.Frame(
            self.content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 30)
        )

        information = [
            ("Application", "MediCare Hospital Management"),
            ("Database", "MySQL"),
            ("Database Name", "mydata"),
            ("Table", "hospital"),
            ("Authentication", "Local administrator login"),
            ("Status", "Operational")
        ]

        for i, (key, value) in enumerate(information):

            row = tk.Frame(
                card,
                bg=WHITE
            )

            row.pack(
                fill="x",
                padx=35,
                pady=10
            )

            tk.Label(
                row,
                text=key,
                bg=WHITE,
                fg=MUTED,
                width=20,
                anchor="w",
                font=("Segoe UI Semibold", 10)
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=value,
                bg=WHITE,
                fg=TEXT,
                anchor="w",
                font=("Segoe UI", 10)
            ).pack(
                side="left"
            )

    # --------------------------------------------------------
    # DASHBOARD REBUILD
    # --------------------------------------------------------

    def show_dashboard(self):

        self.build_dashboard()

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # --------------------------------------------------------
    # STATUS BAR
    # --------------------------------------------------------

    def build_statusbar(self):

        status = tk.Frame(
            self.root,
            bg=NAVY,
            height=28
        )

        status.pack(
            side="bottom",
            fill="x"
        )

        status.pack_propagate(False)

        tk.Label(
            status,
            textvariable=self.status_text,
            bg=NAVY,
            fg="#BCCCDC",
            font=("Segoe UI", 8)
        ).pack(
            side="left",
            padx=15
        )

        tk.Label(
            status,
            text="MediCare HMS  •  MySQL",
            bg=NAVY,
            fg="#829AB1",
            font=("Segoe UI", 8)
        ).pack(
            side="right",
            padx=15
        )

    # ========================================================
    # MYSQL FUNCTIONS
    # ========================================================

    def iPrescriptionData(self):

        if (
            self.Nametable.get().strip() == ""
            or self.ref.get().strip() == ""
        ):

            messagebox.showerror(
                "Missing Information",
                "Tablet name and Reference Number are required."
            )

            return

        conn = None

        try:

            conn = get_connection()

            cursor = conn.cursor()

            # IMPORTANT:
            # This order matches the existing 18-column database
            # structure used by the original application.

            query = """
                INSERT INTO hospital VALUES
                (
                    %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s
                )
            """

            values = (
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
            )

            cursor.execute(
                query,
                values
            )

            conn.commit()

            self.status_text.set(
                "Record saved successfully"
            )

            messagebox.showinfo(
                "Success",
                "Patient prescription saved successfully."
            )

            self.fetch_data()

        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Unable to save record:\n\n{err}"
            )

        finally:

            if conn and conn.is_connected():
                conn.close()

    # --------------------------------------------------------
    # FETCH DATA
    # --------------------------------------------------------

    def fetch_data(self):

        if not hasattr(
            self,
            "hospital_table"
        ):
            return

        conn = None

        try:

            conn = get_connection()

            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM hospital"
            )

            rows = cursor.fetchall()

            self.hospital_table.delete(
                *self.hospital_table.get_children()
            )

            for row in rows:

                self.hospital_table.insert(
                    "",
                    tk.END,
                    values=row
                )

            self.status_text.set(
                f"{len(rows)} record(s) loaded"
            )

        except mysql.connector.Error as err:

            self.status_text.set(
                "Database connection error"
            )

            messagebox.showerror(
                "Database Error",
                f"Unable to load records:\n\n{err}"
            )

        finally:

            if conn and conn.is_connected():
                conn.close()

    # --------------------------------------------------------
    # GET SELECTED ROW
    # --------------------------------------------------------

    def get_cursor(self, event=None):

        selected = self.hospital_table.focus()

        if not selected:
            return

        contents = self.hospital_table.item(
            selected
        )

        row = contents.get(
            "values",
            []
        )

        if len(row) < 18:
            return

        try:

            self.Nametable.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.nooftab.set(row[3])
            self.lot.set(row[4])
            self.issuedate.set(row[5])
            self.issuedate1.set(row[6])
            self.DDose.set(row[7])
            self.SE.set(row[8])
            self.info.set(row[9])
            self.BP.set(row[10])
            self.Medication.set(row[11])
            self.PatientID.set(row[12])
            self.NHS.set(row[13])
            self.PatientName.set(row[14])
            self.DOB.set(row[15])
            self.Address.set(row[16])
            self.StorageAdvice.set(row[17])

            self.status_text.set(
                f"Selected patient: {self.PatientName.get()}"
            )

        except Exception as err:

            messagebox.showerror(
                "Selection Error",
                str(err)
            )

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    def update(self):

        if self.PatientID.get().strip() == "":

            messagebox.showerror(
                "Update Error",
                "Select a patient record first."
            )

            return

        conn = None

        try:

            conn = get_connection()

            cursor = conn.cursor()

            query = """
                UPDATE hospital
                SET
                    Nametable=%s,
                    ref=%s,
                    Dose=%s,
                    nooftab=%s,
                    lot=%s,
                    issuedate=%s,
                    issuedate1=%s,
                    DDose=%s,
                    SE=%s,
                    info=%s,
                    BP=%s,
                    StorageAdvice=%s,
                    Medication=%s,
                    NHS=%s,
                    PatientName=%s,
                    DOB=%s,
                    Address=%s
                WHERE PatientID=%s
            """

            values = (
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
                self.StorageAdvice.get(),
                self.Medication.get(),
                self.NHS.get(),
                self.PatientName.get(),
                self.DOB.get(),
                self.Address.get(),
                self.PatientID.get()
            )

            cursor.execute(
                query,
                values
            )

            conn.commit()

            if cursor.rowcount > 0:

                messagebox.showinfo(
                    "Update Successful",
                    "Patient record updated successfully."
                )

                self.status_text.set(
                    "Patient record updated"
                )

                self.fetch_data()

            else:

                messagebox.showwarning(
                    "No Changes",
                    "No matching Patient ID was found."
                )

        except mysql.connector.Error as err:

            messagebox.showerror(
                "Database Error",
                f"Unable to update record:\n\n{err}"
            )

        finally:

            if conn and conn.is_connected():
                conn.close()

    # --------------------------------------------------------
    # PRESCRIPTION TEXT
    # --------------------------------------------------------

    def generate_prescription_text(self):

        now = datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )

        return (
            "\n"
            "                    MEDICARE HOSPITAL\n"
            "                 DIGITAL PRESCRIPTION\n"
            "\n"
            "============================================================\n"
            f"Generated: {now}\n"
            "============================================================\n\n"
            f"Patient ID       : {self.PatientID.get()}\n"
            f"Patient Name     : {self.PatientName.get()}\n"
            f"NHS Number       : {self.NHS.get()}\n"
            f"Date of Birth    : {self.DOB.get()}\n"
            f"Blood Pressure   : {self.BP.get()}\n"
            f"Address          : {self.Address.get()}\n\n"
            "------------------------------------------------------------\n"
            "MEDICATION\n"
            "------------------------------------------------------------\n"
            f"Tablet           : {self.Nametable.get()}\n"
            f"Reference        : {self.ref.get()}\n"
            f"Dose             : {self.Dose.get()}\n"
            f"No. of Tablets   : {self.nooftab.get()}\n"
            f"Lot Number       : {self.lot.get()}\n"
            f"Issue Date       : {self.issuedate.get()}\n"
            f"Expiry Date      : {self.issuedate1.get()}\n"
            f"Daily Dose       : {self.DDose.get()}\n"
            f"Medication Info  : {self.Medication.get()}\n\n"
            "------------------------------------------------------------\n"
            "ADDITIONAL INFORMATION\n"
            "------------------------------------------------------------\n"
            f"Side Effects     : {self.SE.get()}\n"
            f"Storage Advice   : {self.StorageAdvice.get()}\n"
            f"Information      : {self.info.get()}\n\n"
            "============================================================\n"
            "              Authorized Hospital Record\n"
            "============================================================\n"
        )

    # --------------------------------------------------------
    # GENERATE PRESCRIPTION
    # --------------------------------------------------------

    def iPrescription(self):

        prescription = self.generate_prescription_text()

        if hasattr(
            self,
            "txtPrescription"
        ):

            self.txtPrescription.config(
                state="normal"
            )

            self.txtPrescription.delete(
                "1.0",
                tk.END
            )

            self.txtPrescription.insert(
                "1.0",
                prescription
            )

            self.txtPrescription.config(
                state="disabled"
            )

        self.status_text.set(
            "Prescription generated"
        )

        messagebox.showinfo(
            "Prescription Ready",
            "Prescription generated successfully."
        )

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------

    def iclear(self):

        variables = [
            self.Nametable,
            self.ref,
            self.Dose,
            self.nooftab,
            self.lot,
            self.issuedate,
            self.issuedate1,
            self.DDose,
            self.SE,
            self.info,
            self.BP,
            self.StorageAdvice,
            self.Medication,
            self.PatientID,
            self.NHS,
            self.PatientName,
            self.DOB,
            self.Address
        ]

        for variable in variables:
            variable.set("")

        if hasattr(
            self,
            "txtPrescription"
        ):

            self.txtPrescription.config(
                state="normal"
            )

            self.txtPrescription.delete(
                "1.0",
                tk.END
            )

            self.txtPrescription.insert(
                "1.0",
                "Select patient information and click\n"
                "\"Generate Prescription\" to preview it here."
            )

            self.txtPrescription.config(
                state="disabled"
            )

        self.status_text.set(
            "Form cleared"
        )

    # --------------------------------------------------------
    # DELETE / CLEAR
    # --------------------------------------------------------

    def idelete(self):

        result = messagebox.askyesno(
            "Clear Prescription",
            "Clear all currently entered prescription information?"
        )

        if result:

            self.iclear()

            self.status_text.set(
                "Prescription data cleared"
            )


# ============================================================
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    window = tk.Tk()

    LoginPage(window)

    window.mainloop()
