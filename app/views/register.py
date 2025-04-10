import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def register():
    user = username_entry.get()
    pw = password_entry.get()
    confirm = confirm_entry.get()

    if not user or not pw or not confirm:
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if pw != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # TODO: Save user data to DB
    messagebox.showinfo("Success", "Registered successfully!")

def go_back():
    root.destroy()
    # TODO: Open login screen again

root = tk.Tk()
root.title("Trang đăng ký")
root.geometry("1000x500")
root.configure(bg="white")

# Header
header_frame = tk.Frame(root, bg="#cc9a35", height=60)
header_frame.pack(fill=tk.X)

# Icon & Title
icon_img = Image.open("img/register.png")  # Đổi đường dẫn nếu cần
icon = ImageTk.PhotoImage(icon_img)
icon_label = tk.Label(header_frame, image=icon, bg="#cc9a35")
icon_label.pack(side=tk.LEFT, padx=20)

title_label = tk.Label(header_frame, text="Register", font=("Times New Roman", 28, "bold"), bg="#cc9a35", fg="#000")
title_label.pack(side=tk.LEFT)

# Content Frame
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)

# Welcome Text
welcome_label = tk.Label(content_frame, text="Welcome to the money savings book management",
                         font=("Times New Roman", 18, "bold"), fg="#cc9a35", bg="white", justify="left")
welcome_label.grid(row=0, column=0, sticky="w", pady=20)

# # Illustration
illustration_img = Image.open("img/manual.png")  # Đổi đường dẫn ảnh
illustration_img = illustration_img.resize((220, 220))
illustration = ImageTk.PhotoImage(illustration_img)
illustration_label = tk.Label(content_frame, image=illustration, bg="white")
illustration_label.grid(row=1, column=0, rowspan=3)

# Form Labels and Entries
form_frame = tk.Frame(content_frame, bg="white")
form_frame.grid(row=1, column=1, padx=50)

# Username
user_icon = ImageTk.PhotoImage(Image.open("img/user.png").resize((20, 20)))  # icon người dùng
tk.Label(form_frame, image=user_icon, bg="white").grid(row=0, column=0, padx=5)
tk.Label(form_frame, text="Username:", font=("Times New Roman", 14, "bold"), bg="white").grid(row=0, column=1, sticky="w")
username_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, bg="#d9d9d9")
username_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Password
pass_icon = ImageTk.PhotoImage(Image.open("img/reset-password.png").resize((20, 20)))  # icon ổ khóa
tk.Label(form_frame, image=pass_icon, bg="white").grid(row=2, column=0, padx=5)
tk.Label(form_frame, text="Password:", font=("Times New Roman", 14, "bold"), bg="white").grid(row=2, column=1, sticky="w")
password_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, bg="#d9d9d9", show="*")
password_entry.grid(row=3, column=0, columnspan=2, pady=5)

# Confirm Password
tk.Label(form_frame, image=pass_icon, bg="white").grid(row=4, column=0, padx=5)
tk.Label(form_frame, text="Confirm Password:", font=("Times New Roman", 14, "bold"), bg="white").grid(row=4, column=1, sticky="w")
confirm_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, bg="#d9d9d9", show="*")
confirm_entry.grid(row=5, column=0, columnspan=2, pady=5)

# Buttons
btn_frame = tk.Frame(form_frame, bg="white")
btn_frame.grid(row=6, column=0, columnspan=2, pady=20)

tk.Button(btn_frame, text="Register", font=("Times New Roman", 13), width=10, command=register).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Back", font=("Times New Roman", 13), width=10, command=go_back).grid(row=0, column=1, padx=10)

root.mainloop()
