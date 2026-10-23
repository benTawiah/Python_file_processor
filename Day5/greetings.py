import tkinter as tk
import tkinter as ttk

def greet_user():
    name = name_entry.get().strip()
    
    if name == " ":
        result_label.config(text="Please enter your name.")
    else:
         result_label.config(text=f"Hello {name}!")

window = tk.Tk()
window.title("Greetings Application")

name_label = ttk.Label(window, text="Your Name : ")
name_label.pack(padx=20, pady=20)

name_entry= ttk.Entry(window, width=20 )
name_entry.pack(padx=20, pady=20)

button = tk.Button(window, text="Say Hello ", command=greet_user)
button.pack(padx=20, pady=20)

result_label = ttk.Label(window, text="...")
result_label.pack(padx=20, pady=20)










window.geometry("800x600")
window.mainloop()