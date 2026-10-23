import tkinter as tk
import tkinter as ttk

def show_message():
    result_label.config(text ="You clicked")
    
def reset_message():
    result_label.config(text ="waiting...")

window = tk.Tk()
window.title("Buttons")

button = tk.Button(window, text="Click Me", command=show_message)
button.pack(padx=20, pady=20)

reset_button = tk.Button(window, text="Reset", command=reset_message)
reset_button.pack(padx=20, pady=20)

result_label = ttk.Label(window, text="waiting...")
result_label.pack(padx=20, pady=20)


window.geometry("800x600")
window.mainloop()