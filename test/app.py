import tkinter as tk 

root = tk.Tk()
root.title("myDictionary")
root.geometry("1366x768")

frame = tk.Frame(root, width=root.winfo_screenwidth(),height=root.winfo_screenheight(),borderwidth=2,relief="sunken")
frame.pack_propagate(False)
frame.pack(anchor="nw",padx=10, pady=10)

label = tk.Label(frame, text="This is inside the frame")
label.pack()






''' BUTTON UTILIZATION
def button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()
'''

root.mainloop()

