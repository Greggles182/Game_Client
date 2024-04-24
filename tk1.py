import tkinter as tk



def TKinput(texts):
    root = tk.Tk()
    root.title("CLI App")

    command_var = tk.StringVar()  # Create a StringVar to store the command

    def submit_command():
        command_var.set(entry.get())  # Set the value of command_var
        root.destroy()  # Close the window after getting the command
    
    instruction_label = tk.Label(root, text=texts)
    instruction_label.pack()

    entry = tk.Entry(root)
    entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_command)
    submit_button.pack()

    root.mainloop()

    return command_var.get()  # Return the value of command_var

def main():
    command = TKinput("Enter Command")
    print("Command entered:", command)

if __name__ == "__main__":
    main()
