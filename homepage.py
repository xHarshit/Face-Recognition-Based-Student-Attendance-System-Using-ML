from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

root=Tk()
root.geometry("1366x768+0+0")
root.title("Face_Recognition_System")

# This part is image labels setting start
# first header image
img = Image.open(r"Images_GUI\banner.jpg")
img = img.resize((1366, 130), Image.LANCZOS)  # Use Image.LANCZOS for resizing

photoimg = ImageTk.PhotoImage(img)

# set image as label
f_lb1 = Label(root, image=photoimg)
f_lb1.place(x=0, y=0, width=1366, height=130)

# background image
bg1 = Image.open(r"Images_GUI\bg3.jpg")
bg1 = bg1.resize((1366, 768), Image.LANCZOS)  # Use Image.LANCZOS for resizing
photobg1 = ImageTk.PhotoImage(bg1)

# set image as label
bg_img = Label(root, image=photobg1)
bg_img.place(x=0, y=130, width=1366, height=768)

# title section
title_lb1 = Label(bg_img, text="Attendance Management System Using Facial Recognition", font=("verdana", 30, "bold"),bg="white", fg="navyblue")
title_lb1.place(x=0, y=0, width=1366, height=45)

# ==================Function for Open Images Folder==================
def open_img():
    os.startfile("dataset")

# ==================Functions Buttons=====================
def student_pannels():
    import student

def train_pannels():
    import train_v2

def face_rec():
    import recognizer

def attendance_pannel():
    import attendance

def developr():
    import developer

def helpSupport():
    import helpsupport

def Close():
    root.destroy()


# Create buttons below the section
# -------------------------------------------------------------------------------------------------------------------
# student button 1
std_img_btn = Image.open(r"Images_GUI\std1.jpg")
std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
std_img1 = ImageTk.PhotoImage(std_img_btn)

std_b1 = Button(bg_img, command=student_pannels, image=std_img1, cursor="hand2")
std_b1.place(x=250, y=100, width=180, height=180)

std_b1_1 = Button(bg_img, command=student_pannels, text="Student Panel", cursor="hand2",
                  font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
std_b1_1.place(x=250, y=280, width=180, height=45)

# Detect Face button 2
det_img_btn = Image.open(r"Images_GUI\det1.jpg")
det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
det_img1 = ImageTk.PhotoImage(det_img_btn)

det_b1 = Button(bg_img, command=face_rec, image=det_img1, cursor="hand2")
det_b1.place(x=480, y=100, width=180, height=180)

det_b1_1 = Button(bg_img, command=face_rec, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"),
                  bg="white", fg="navyblue")
det_b1_1.place(x=480, y=280, width=180, height=45)

# Attendance System button 3
att_img_btn = Image.open(r"Images_GUI\att.jpg")
att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
att_img1 = ImageTk.PhotoImage(att_img_btn)

att_b1 = Button(bg_img, command=attendance_pannel, image=att_img1, cursor="hand2")
att_b1.place(x=710, y=100, width=180, height=180)

att_b1_1 = Button(bg_img, command=attendance_pannel, text="Attendance", cursor="hand2",
                  font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
att_b1_1.place(x=710, y=280, width=180, height=45)

# Help Support button 4
hlp_img_btn = Image.open(r"Images_GUI\hlp.jpg")
hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

hlp_b1 = Button(bg_img, command=helpSupport, image=hlp_img1, cursor="hand2")
hlp_b1.place(x=940, y=100, width=180, height=180)

hlp_b1_1 = Button(bg_img, command=helpSupport, text="Help Support", cursor="hand2", font=("tahoma", 15, "bold"),
                  bg="white", fg="navyblue")
hlp_b1_1.place(x=940, y=280, width=180, height=45)

# Top 4 buttons end.......
# ---------------------------------------------------------------------------------------------------------------------------
# Start below buttons.........
# Train button 5
tra_img_btn = Image.open(r"Images_GUI\tra1.jpg")
tra_img_btn = tra_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
tra_img1 = ImageTk.PhotoImage(tra_img_btn)

tra_b1 = Button(bg_img, command=train_pannels, image=tra_img1, cursor="hand2")
tra_b1.place(x=250, y=330, width=180, height=180)

tra_b1_1 = Button(bg_img, command=train_pannels, text="Data Train", cursor="hand2", font=("tahoma", 15, "bold"),bg="white", fg="navyblue")
tra_b1_1.place(x=250, y=510, width=180, height=45)

# Photo button 6
pho_img_btn = Image.open(r"Images_GUI\qr1.png")
pho_img_btn = pho_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
pho_img1 = ImageTk.PhotoImage(pho_img_btn)

pho_b1 = Button(bg_img, command=open_img, image=pho_img1, cursor="hand2")
pho_b1.place(x=480, y=330, width=180, height=180)

pho_b1_1 = Button(bg_img, command=open_img, text="QR-Codes", cursor="hand2", font=("tahoma", 15, "bold"),
                  bg="white", fg="navyblue")
pho_b1_1.place(x=480, y=510, width=180, height=45)

# Developers button 7
dev_img_btn = Image.open(r"Images_GUI\dev.jpg")
dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
dev_img1 = ImageTk.PhotoImage(dev_img_btn)

dev_b1 = Button(bg_img, command=developr, image=dev_img1, cursor="hand2")
dev_b1.place(x=710, y=330, width=180, height=180)

dev_b1_1 = Button(bg_img, command=developr, text="Developers", cursor="hand2", font=("tahoma", 15, "bold"),
                  bg="white", fg="navyblue")
dev_b1_1.place(x=710, y=510, width=180, height=45)

# exit button 8
exi_img_btn = Image.open(r"Images_GUI\exi.jpg")
exi_img_btn = exi_img_btn.resize((180, 180), Image.LANCZOS)  # Use Image.LANCZOS for resizing
exi_img1 = ImageTk.PhotoImage(exi_img_btn)

exi_b1 = Button(bg_img, command=Close, image=exi_img1, cursor="hand2")
exi_b1.place(x=940, y=330, width=180, height=180)

exi_b1_1 = Button(bg_img, command=Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"), bg="white",
                  fg="navyblue")
exi_b1_1.place(x=940, y=510, width=180, height=45)


root.mainloop()
