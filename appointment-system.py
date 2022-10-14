from tkinter import *
from tkinter import messagebox, StringVar, Frame, Toplevel, Tk
from tkinter import ttk
import pymysql

'''
            def clear(self):
                txt_username.delete(0, END)
                txt_password.delete(0, END)

             def login1():
            if txt_username.get() == "" or txt_password.get() == "":
                messagebox.showwarning("warning", "Fill all fields", parent=self.root)
            else:
                messagebox.showwarning("successfull")

'''


class login_window:
    newWindow: Toplevel

    def Reg_window(self):
        newWindow = Toplevel(login_window)
        obj = Registration_Window(newWindow)

    def close(self):
        self.win1.destroy()

    def __init__(self, win1):
        self.win1 = win1
        self.win1.title("appointment system")
        self.win1.geometry("400x400+0+0")
        self.win1.resizable(False, False)
        user = StringVar()
        passw = StringVar()

        login_frame = Frame(self.win1, bg="#FF9900")
        login_frame.place(x=0, y=0, width=400, height=50)

        # Frame 2
        log_frame = Frame(self.win1, bg="#22313F")
        log_frame.place(x=0, y=40, width=400, height=350)

        #  login form
        heading = Label(login_frame, text="LOGIN FORM", font=("Tahoma", 16, "bold"), bg="#FF9900", fg="white")
        heading.place(x=100, y=10)

        lbl_username = Label(log_frame, text="Username:", font=("Tahoma", 14, "bold"), bg="#22313F", fg="white")
        lbl_username.place(x=100, y=40)
        self.txt_username = Entry(log_frame, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC",
                                  textvariable=user)
        self.txt_username.place(x=50, y=80, width=300, height=30)

        lbl_password = Label(log_frame, text="Password:", font=("Tahoma", 14, "bold"), bg="#22313F", fg="white")
        lbl_password.place(x=100, y=120)
        self.txt_password = Entry(log_frame, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC",
                                  textvariable=passw)
        self.txt_password.place(x=50, y=160, width=300, height=30)

        btn_clear = Button(log_frame, command=self.clear, text="Clear", font=("Tahoma", 14, "bold"), fg="white",
                           bg="Green", bd=7)
        btn_clear.place(x=100, y=220)
        btn_login = Button(log_frame, text="Login", command=self.appoint, font=("Tahoma", 14, "bold"), fg="white",
                           bg="maroon", bd=7)
        btn_login.place(x=200, y=220)
        btn_register = Button(log_frame, text="Not Registered? Register", font=("Tahoma", 10, "bold"), bg="#22313F",
                              fg="white", bd=0, command=self.Reg_window)
        btn_register.place(x=100, y=290)

    def Reg_window(self):
        self.newWindow = Toplevel(self.win1)
        Registration_Window(self.newWindow)

    def appoint(self):
        self.newWindow = Toplevel(self.win1)
        obj = appointment(self.newWindow)

    def clear(self):
        self.txt_username.delete(0, END)
        self.txt_password.delete(0, END)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


class Registration_Window:

    def switch(self):
        self.win1.destroy()

    def __init__(self, win1):
        self.win1 = win1
        self.win1.title("appointment system")
        self.win1.geometry("500x600+0+0")
        self.win1.resizable(False, False)

        fname = StringVar()
        lname = StringVar()
        age = StringVar()
        gender = IntVar()
        city = StringVar()
        username = StringVar()
        password = StringVar()
        cpassword = StringVar()
        address = StringVar()

        # Registration  form
        # Frame 1
        frame_register = Frame(self.win1, bg="#FF9900")
        frame_register.place(x=0, y=0, width=500, height=50)

        # frame 2
        frame_reg = Frame(self.win1, bg="#22313F")
        frame_reg.place(x=0, y=50, width=500, height=650)

        # GUI
        reg_heading = Label(frame_register, text="Registration Form", font=("Tahoma", 14, "bold"), fg="white",
                            bg="#FF9900")
        reg_heading.place(x=100, y=10)

        lbl_fname = Label(frame_reg, text="First name:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_fname.place(x=10, y=30)
        self.txt_fname = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=fname)
        self.txt_fname.place(x=10, y=60, width=200, height=30)

        lbl_lname = Label(frame_reg, text="Last Name:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_lname.place(x=280, y=30)
        self.txt_lname = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=lname)
        self.txt_lname.place(x=280, y=60, width=200, height=30)

        lbl_age = Label(frame_reg, text="Age:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_age.place(x=10, y=100)
        self.txt_age = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=age)
        self.txt_age.place(x=10, y=130, width=200, height=30)

        lbl_gender = Label(frame_reg, text="Gender:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_gender.place(x=280, y=100)
        self.radiobtn_male = ttk.Radiobutton(frame_reg, text="Male", value="Male").\
            place(x=280, y=130)
        self.radiobtn_female = ttk.Radiobutton(frame_reg, text="Female", value="Female").\
            place(x=380, y=130)

        lbl_city = Label(frame_reg, text="City:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_city.place(x=10, y=170)
        self.txt_city = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=city)
        self.txt_city.place(x=10, y=200, width=200, height=30)

        lbl_username = Label(frame_reg, text="Username:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_username.place(x=280, y=170)
        self.txt_username = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC",
                                  textvariable=username)
        self.txt_username.place(x=280, y=200, width=200, height=30)

        lbl_pass = Label(frame_reg, text="Password:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_pass.place(x=10, y=240)
        self.txt_pass = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=password)
        self.txt_pass.place(x=10, y=270, width=200, height=30)

        lbl_cpass = Label(frame_reg, text="Confirm Password:", font=("Tahoma", 12, "bold"), bg="#22313F",
                          fg="white")
        lbl_cpass.place(x=280, y=240)
        self.txt_cpass = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=cpassword)
        self.txt_cpass.place(x=280, y=270, width=200, height=30)

        lbl_address = Label(frame_reg, text="Address:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_address.place(x=10, y=310)
        self.txt_address = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC", textvariable=address)
        self.txt_address.place(x=10, y=340, width=200, height=30)

        self.btn_clr = Button(frame_reg, command=self.btn_clear, text="Clear", font=("Tahoma", 14, "bold"), bg="green", fg="white", bd=7)
        self.btn_clr.place(x=100, y=390, width=120)
        self.btn_reg = Button(frame_reg, text="Register", command=self.register, font=("Tahoma", 14, "bold"),
                              bg="maroon", fg="white", bd=7)
        self.btn_reg.place(x=260, y=390, width=120)
        self.btn_log = Button(frame_reg, text="Registered? Login", font=("Tahoma", 11, "bold"), bg="#22313F",
                              fg="white",
                              bd=0, command=self.switch)
        self.btn_log.place(x=150, y=450)

    def appoint(self):
        self.newWindow = Toplevel(self.win1)
        obj = appointment(self.newWindow)

    def btn_clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_age.delete(0, END)
        # self.radiobtn_male.set(0)
        # self.radiobtn_female.set(0)
        self.txt_city.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_cpass.delete(0, END)
        self.txt_address.delete(0, END)

    def register(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_age.get() == "" or self.radiobtn_female\
         .get() == "" or self.radiobtn_male.get() == "" or self.txt_city.get() == "" or\
         self.txt_username.get() == "" or self.txt_pass.get() == "" or self.txt_cpass.get() == "" or\
         self.txt_address.get() == "":

            messagebox.showerror("Error!!!", "all fields are required")

        elif self.txt_pass.get() != self.txt_pass.get():
            messagebox.showerror("Warning", "password and confirm password should be same")

        else:
            try:
                con = pymysql.connect(host="localhost",  username="", password="", database="")

class appointment:
    def __init__(self, win1):
        self.win1 = win1
        self.win1.title("appointment system")
        self.win1.geometry("400x600+0+0")
        self.win1.resizable(False, False)

        # Frame 1
        frame_register = Frame(self.win1, bg="#FF9900")
        frame_register.place(x=0, y=0, width=400, height=50)

        # frame 2
        frame_reg = Frame(self.win1, bg="#22313F")
        frame_reg.place(x=0, y=50, width=400, height=650)

        appointment_heading = Label(frame_register, text="Appointment Booking Form", font=("Tahoma", 14, "bold"),
                                    fg="white", bg="#FF9900")
        appointment_heading.place(x=50, y=10)

        lbl_username = Label(frame_reg, text="Username:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_username.place(x=20, y=20)
        self.txt_username = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
        self.txt_username.place(x=10, y=50, width=300, height=30)

        lbl_doctor = Label(frame_reg, text="Doctor's Name:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_doctor.place(x=20, y=90)
        self.cmb_doctor = ttk.Combobox(frame_reg, font=("Tahoma", 10, "bold"), state="readonly", justify=LEFT)
        self.cmb_doctor["values"] = (
        "Dr. Sharon Bungei", "Dr.Bornes Bett", "Dr.Bildad Koech", "Dr.Nimrod Tabu", "Dr.Anthony Toro")
        self.cmb_doctor.place(x=10, y=120, width=300, height=30)
        self.cmb_doctor.set("Select your doctor")

        lbl_date = Label(frame_reg, text="Appointment Date:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_date.place(x=20, y=160)
        self.txt_date = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
        self.txt_date.place(x=10, y=190, width=300, height=30)

        lbl_time = Label(frame_reg, text="Appointment Time:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_time.place(x=20, y=230)
        self.cmb_time = ttk.Combobox(frame_reg, font=("Tahoma", 10, "bold"), state="readonly", justify=LEFT)
        self.cmb_time["values"] = ("10.00am-10.30am", "10.30am-11.00am", "11.00am-11.30am", "11.30am-12.00pm")
        self.cmb_time.place(x=10, y=260, width=300, height=30)
        self.cmb_time.set("Select Appointment time")

        lbl_check = Label(frame_reg, text="Check Availability:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
        lbl_check.place(x=20, y=300)
        self.cmb_check = ttk.Combobox(frame_reg, font=("Tahoma", 10, "bold"), state="readonly", justify=LEFT)
        self.cmb_check["values"] = ("Available", "Not Available")
        self.cmb_check.place(x=10, y=330, width=300, height=30)
        self.cmb_check.set("Select availabiliy")

        lbl_confirm = Label(frame_reg, text="Confirm Availability:", font=("Tahoma", 12, "bold"), bg="#22313F",
                            fg="white")
        lbl_confirm.place(x=20, y=370)
        self.cmb_confirm = ttk.Combobox(frame_reg, font=("Tahoma", 10, "bold"), state="readonly", justify=LEFT)
        self.cmb_confirm["values"] = ("Available", "Not Available")
        self.cmb_confirm.place(x=10, y=410, width=300, height=30)
        self.cmb_confirm.set("Select availabiliy")

        self.btn_clr = Button(frame_reg, text="Clear", font=("Tahoma", 14, "bold"), bg="green", fg="white", bd=7)
        self.btn_clr.place(x=30, y=470, width=120)
        self.btn_submit = Button(frame_reg, text="Submit", font=("Tahoma", 14, "bold"), bg="maroon", fg="white", bd=7)
        self.btn_submit.place(x=200, y=470, width=120)


root = Tk()
obj = login_window(root)
root.mainloop()
