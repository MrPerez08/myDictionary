import tkinter as tk 

root = tk.Tk()
root.title("myDictionary")
root.geometry("1366x768")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


frame = tk.Frame(root, width=root.winfo_screenwidth(),height=root.winfo_screenheight(),borderwidth=2,relief="sunken")
frame.pack_propagate(False)
frame.pack(anchor="nw",padx=10, pady=10)


label = tk.Label(frame, text="This is inside the frame")
label.pack()



def createVocab():
    print("Button clicked!")

button = tk.Button(frame, text=" + ", command=createVocab)
button.pack()




def addDefinition():
    print("Button clicked!")

button = tk.Button(frame, text=" + ", command=addDefinition)
button.pack()




root.mainloop()

