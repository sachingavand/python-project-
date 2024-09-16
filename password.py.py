
import tkinter as tk
import random
import string
from tkinter import messagebox


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0") 

        
        self.initial_label = tk.Label(root, text="Welcome to the Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.initial_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Password Generation", command=self.show_options, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
        self.start_button.pack(pady=20)

        
        self.options_frame = tk.Frame(root, bg="#f0f0f0")

        self.length_label = tk.Label(self.options_frame, text="Password Length:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.options_frame, font=("Arial", 12), width=10, bg="#ffffff", borderwidth=2, relief="solid")
        self.length_entry.pack(pady=5)

        self.special_char_var = tk.IntVar(value=1)  
        self.special_char_check = tk.Checkbutton(self.options_frame, text="Include Special Characters", variable=self.special_char_var, font=("Arial", 12), bg="#f0f0f0")
        self.special_char_check.pack(pady=10)

        self.label_label = tk.Label(self.options_frame, text="Label/Description:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.label_label.pack(pady=10)

        self.label_entry = tk.Entry(self.options_frame, font=("Arial", 12), width=20, bg="#ffffff", borderwidth=2, relief="solid")
        self.label_entry.pack(pady=5)

        self.generate_button = tk.Button(self.options_frame, text="Generate Password", command=self.confirm_and_generate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(self.options_frame, text="", font=("Arial", 12), fg="green", bg="#f0f0f0")
        self.password_label.pack(pady=10)

        self.copy_button = tk.Button(self.options_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", relief="raised")
        self.copy_button.pack(pady=5)

        self.save_button = tk.Button(self.options_frame, text="Save Password", command=self.save_password, font=("Arial", 12, "bold"), bg="#FF5722", fg="white", relief="raised")
        self.save_button.pack(pady=10)

        self.strength_label = tk.Label(self.options_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.strength_label.pack(pady=10)

       
        self.options_frame.pack_forget()

    def show_options(self):
       
        if messagebox.askyesno("Confirm", "Do you want to generate a password?"):
            self.initial_label.pack_forget()
            self.start_button.pack_forget()
            self.options_frame.pack(pady=20)

    def confirm_and_generate_password(self):
       
        self.generate_password()

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            self.password_label.config(text="Please enter a valid length.")
            return

        length = int(length)
        if length < 8:
            self.password_label.config(text="Password length should be at least 8 characters.")
            return

        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        if self.special_char_var.get() == 1:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password: {password}")
        self.evaluate_password_strength(password)

    def evaluate_password_strength(self, password):
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        strength = "Weak"
        if length >= 8 and has_upper and has_lower and has_digit and has_special:
            strength = "Strong"
        elif length >= 8 and (has_upper or has_lower) and has_digit:
            strength = "Moderate"

        self.strength_label.config(text=f"Password Strength: {strength}")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Error", "No password to copy.")

    def save_password(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        label = self.label_entry.get()

        if not password:
            messagebox.showwarning("Error", "No password to save.")
            return

        if not label:
            messagebox.showwarning("Error", "Please provide a label or description for the password.")
            return

        with open("E:\\New folder\\Python Project\\password.txt", "a") as file:
            file.write(f"{label}: {password}\n")
        
        messagebox.showinfo("Saved", "Password saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
