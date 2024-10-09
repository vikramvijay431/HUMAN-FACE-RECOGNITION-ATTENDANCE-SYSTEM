import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Tkinter App")
window.geometry("400x300")

# Create a label and add it to the window
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Start the Tkinter event loop
window.mainloop()
