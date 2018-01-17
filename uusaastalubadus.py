import tkinter as tk
    

def write_slogan():
    print("Saan geo perioodihinde positiivse.")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button()
slogan = tk.Button(frame,
                   text="Vajuta minu peale!",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()