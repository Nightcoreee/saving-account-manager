import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os 

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" or password == "123":
        messagebox.showinfo("Success", "Đăng nhập thành công!")
        print("Login successful!")
    else:
        messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin")

def register():
    os.system("python app/views/register.py")
    
root = tk.Tk()
root.title("Trang đăng nhập")
root.geometry("1000x500")
root.configure(bg="#ffffff")

# ========== Header ==========
header_frame = tk.Frame(root, bg="#cc9a35", height=70)
header_frame.pack(fill=tk.X)

# Icon login
icon_img = Image.open("img/enter.png")
icon = ImageTk.PhotoImage(icon_img)
icon_label = tk.Label(header_frame, image=icon, bg="#cc9a35")
icon_label.pack(side=tk.LEFT, padx=20)

# Tiêu đề
title_label = tk.Label(header_frame, text="Login", font=("Times New Roman", 28, "bold"),bg="#cc9a35", fg="#000")
title_label.pack(side=tk.LEFT)

# ========== Nội dung ==========
content_frame = tk.Frame(root, bg="white")
content_frame.pack(expand=True, fill=tk.BOTH, padx=40, pady=20)

# welcome text
welcome = tk.Label(content_frame, text="Welcome to the money savings book management", 
                   font=("Times New Roman", 18, "bold"), fg="#cc9a35", bg="white", justify="left")
welcome.grid(row=0, column=0, sticky="w", pady=20)

book_img = Image.open("img/manual.png")
book_img = book_img.resize((220, 220))
book_icon = ImageTk.PhotoImage(book_img)
book_label = tk.Label(content_frame, image=book_icon, bg="white")
book_label.grid(row=1, column=0, rowspan=3)

# ========== Bên phải ==========
form_frame = tk.Frame(content_frame, bg="white")
form_frame.grid(row=1, column=1, padx=50)

# Username
user_icon = ImageTk.PhotoImage(Image.open("img/user.png").resize((20, 20)))
tk.Label(form_frame, image=user_icon, bg="white").grid(row=0, column=0, padx=5)
tk.Label(form_frame, text="Username:", font=("Times New Roman", 14, "bold"), bg="white").grid(row=0, column=1, sticky="w")
username_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, bg="#d9d9d9")
username_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Password
pass_icon = ImageTk.PhotoImage(Image.open("img/reset-password.png").resize((20, 20)))
tk.Label(form_frame, image=pass_icon, bg="white").grid(row=2, column=0, padx=5)
tk.Label(form_frame, text="Password:", font=("Times New Roman", 14, "bold"),
         bg="white").grid(row=2, column=1, sticky="w")
password_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, bg="#d9d9d9", show="*")
password_entry.grid(row=3, column=0, columnspan=2, pady=5)

# Buttons
btn_frame = tk.Frame(form_frame, bg="white")
btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

login_btn = tk.Button(btn_frame, text="Login", font=("Times New Roman", 13), width=12,
                      relief="groove", bd=2, command=login)
login_btn.grid(row=0, column=0, padx=10)

register_btn = tk.Button(btn_frame, text="Register", font=("Times New Roman", 13), width=12,
                         relief="groove", bd=2, command=register)
register_btn.grid(row=0, column=1, padx=10)

# Chia tỷ lệ lưới cho content_frame
content_frame.columnconfigure(0, weight=1)
content_frame.columnconfigure(1, weight=1)

root.mainloop()
