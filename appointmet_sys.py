from logging import root
from tkinter import *
from tkinter import messagebox, StringVar, Frame
from tkinter import ttk

'''
# import pymysql
            def clear(self):
                txt_username.delete(0, END)
                txt_password.delete(0, END)

             def login1():
            if txt_username.get() == "" or txt_password.get() == "":
                messagebox.showwarning("warning", "Fill all fields", parent=self.root)
            else:
                messagebox.showwarning("successfull")

'''


def main():
    root = Tk()
    app = login_window(root)


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("appointment system")
        self.root.geometry("400x400+0+0")
        self.root.resizable(False, False)
        user = StringVar
        passw = StringVar

        def login():
            frame = Frame(self.root, bg="#FFFFFF")
            frame.place(x=0, y=0, width=400, height=400)

            login_frame = Frame(self.root, bg="#FF9900")
            login_frame.place(x=0, y=0, width=400, height=50)

            # Frame 2
            log_frame = Frame(self.root, bg="#22313F")
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

            btn_clear = Button(log_frame, text="Clear", font=("Tahoma", 14, "bold"), fg="white", bg="Green", bd=7)
            btn_clear.place(x=100, y=220)
            btn_login = Button(log_frame, text="Login", font=("Tahoma", 14, "bold"), fg="white", bg="maroon", bd=7)
            btn_login.place(x=200, y=220)
            btn_register = Button(log_frame, text="Not Registered? Register", font=("Tahoma", 10, "bold"), bg="#22313F",
                                  fg="white", bd=0, command=Registration_Window)
            btn_register.place(x=100, y=290)

        # ----------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------


class Registration_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("appointment system")
        self.root.geometry("500x700+0+0")
        self.root.resizable(False, False)

        # Registration  form
        def register(self):
            # Frame 1
            frame_register = Frame(self.root, bg="#FF9900")
            frame_register.place(x=0, y=0, width=500, height=50)

            # frame 2
            frame_reg = Frame(self.root, bg="#22313F")
            frame_reg.place(x=0, y=50, width=500, height=650)

            # GUI
            reg_heading = Label(frame_register, text="Registration Form", font=("Tahoma", 14, "bold"), fg="white",
                                bg="#FF9900")
            reg_heading.place(x=100, y=10)

            lbl_fname = Label(frame_reg, text="First name:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_fname.place(x=10, y=30)
            txt_fname = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_fname.place(x=10, y=60, width=200, height=30)

            lbl_lname = Label(frame_reg, text="Last Name:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_lname.place(x=280, y=30)
            txt_lname = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_lname.place(x=280, y=60, width=200, height=30)

            lbl_age = Label(frame_reg, text="Age:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_age.place(x=10, y=100)
            txt_age = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_age.place(x=10, y=130, width=200, height=30)

            lbl_gender = Label(frame_reg, text="Gender:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_gender.place(x=280, y=100)
            radiobtn_male = ttk.Radiobutton(frame_reg, text="Male", value="Male").place(x=280, y=130)
            radiobtn_female = ttk.Radiobutton(frame_reg, text="Female", value="Female").place(x=380, y=130)

            lbl_city = Label(frame_reg, text="City:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_city.place(x=10, y=170)
            lbl_city = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            lbl_city.place(x=10, y=200, width=200, height=30)

            lbl_username = Label(frame_reg, text="Username:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_username.place(x=280, y=170)
            txt_username = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_username.place(x=280, y=200, width=200, height=30)

            lbl_pass = Label(frame_reg, text="Password:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_pass.place(x=10, y=240)
            txt_pass = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_pass.place(x=10, y=270, width=200, height=30)

            lbl_cpass = Label(frame_reg, text="Confirm Password:", font=("Tahoma", 12, "bold"), bg="#22313F",
                              fg="white")
            lbl_cpass.place(x=280, y=240)
            txt_cpass = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_cpass.place(x=280, y=270, width=200, height=30)

            lbl_address = Label(frame_reg, text="Address:", font=("Tahoma", 12, "bold"), bg="#22313F", fg="white")
            lbl_address.place(x=10, y=310)
            txt_address = Entry(frame_reg, font=("Tahoma", 10, "bold"), fg="black", bg="#CCCCCC")
            txt_address.place(x=10, y=340, width=200, height=30)

            btn_clr = Button(frame_reg, text="Clear", font=("Tahoma", 14, "bold"), bg="green", fg="white", bd=7)
            btn_clr.place(x=100, y=390, width=120)
            btn_reg = Button(frame_reg, text="Register", font=("Tahoma", 14, "bold"), bg="maroon", fg="white", bd=7)
            btn_reg.place(x=260, y=390, width=120)
            btn_log = Button(frame_reg, text="Registered? Login", font=("Tahoma", 11, "bold"), bg="#22313F", fg="white",
                             bd=0, command=login_window)
            btn_log.place(x=150, y=450)


root.mainloop()
