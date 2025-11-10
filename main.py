import tkinter as tk
root = tk.Tk()
root.title("Task Tracker Login")

#Window sizing and positioning
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = (screen_width // 2) - (window_width // 2)
center_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.configure(bg="blue")

label = tk.Label(root, text = "Welcome, Al-Ayn Member!",
                 font=("Calibri", 20),
                 fg = "black",
                 justify="center",
                 bg = "yellow")
label.pack(padx=50, pady=50)

root.mainloop()