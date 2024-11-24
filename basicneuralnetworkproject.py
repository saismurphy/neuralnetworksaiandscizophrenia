import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from tkinter import ttk

# initialize weights and bias globally
weightone = random.random()
weighttwo = random.random()
bias = random.random()
learning_thinking = 0.1  # Learning rate

# global variable for the network's name
network_name = ""

# function to welcome the user and confirm the network name
def welcome_message():
    global network_name
    network_name = name_entry.get()
    if network_name:
        messagebox.showinfo("Hello", f"Hello, I am {network_name}, your simple, yet personal neural network!")
    else:
        messagebox.showinfo("Hello", "Hello, I am your simple, yet personal neural network!")

# confirm name function
def confirm_name():
    global network_name
    network_name = name_entry.get()
    if network_name:
        confirmation_of_name = messagebox.askyesno("Confirm Name", f"Do you want to call me {network_name}?")
        if confirmation_of_name:
            messagebox.showinfo("Name Confirmation", f"I love it! {network_name} sounds beautiful!")
            welcome_message()  # Show the welcome message with the confirmed name
        else:
            name_entry.delete(0, tk.END)  # Clear the entry to let the user try again
            messagebox.showinfo("Change Name", "Okay, let's try another name!")
    else:
        messagebox.showwarning("No Name", "Please give me a name.")

# training function with loading screen
def training_loop():
    show_loading_screen("Thinking....")
    
    global weightone, weighttwo, bias
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    targets = [0, 1, 1, 0]

    for epoch in range(100):
        total_error = 0
        for i, (input1, input2) in enumerate(inputs):
            output = (input1 * weightone) + (input2 * weighttwo) + bias
            error = targets[i] - output
            total_error += error ** 2

            # Update weights and bias
            weightone += learning_thinking * error * input1
            weighttwo += learning_thinking * error * input2
            bias += learning_thinking * error

    hide_loading_screen()  # Hide the loading screen once training is complete
    messagebox.showinfo("Training Complete", "Training is complete!\nWeights and bias have been updated.")

# Input processing function with loading screen
def process_input1():
    show_loading_screen("Thinking... Processing your input.")
    
    try:
        input1 = simpledialog.askinteger("Input 1", "Please input the first value (0 or 1):", parent=root)
        if input1 is None:
            hide_loading_screen()  # Hide loading if user cancels input
            return  # User cancelled the input
        
        if input1 not in [0, 1]:
            messagebox.showerror("Invalid Input", "I only know 0s and 1s!")
            hide_loading_screen()  # Hide loading before returning
            return
        
        process_input2(input1)  # Now prompt for the second input after the first is valid
    except ValueError:
        messagebox.showerror("Invalid Input", "I only eat 0s and 1s!")
        hide_loading_screen()  # hide loading before returning

def process_input2(input1):
    try:
        input2 = simpledialog.askinteger("Input 2", "Please input the second value (0 or 1):", parent=root)
        if input2 is None:
            hide_loading_screen()  # Hide loading if user cancels input
            return  # User cancelled the input
        
        if input2 not in [0, 1]:
            messagebox.showerror("Invalid Input", "I only read 0s and 1s!")
            hide_loading_screen()  # Hide loading before returning
            return
        
        # Perform the calculation with the current weights
        output = (input1 * weightone) + (input2 * weighttwo) + bias
        hide_loading_screen()  # Hide the thinking screen before showing the result
        messagebox.showinfo("Number Guess", f"So, I am guessing the number: {output:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Hey! I only know 0s and 1s!")
        hide_loading_screen()  # Hide loading before returning

# exiting confirmation
def confirm_exit():
    if messagebox.askyesno("Exit", f"Are you sure you want to exit, {network_name}? I'll miss you... :("):
        root.destroy()

# round button functioning
def create_button(text, command, bg_color, fg_color):
    button = tk.Button(main_frame, text=text, command=command, font=("Helvetica", 14, "bold"), bg=bg_color, fg=fg_color, relief="flat", bd=5, padx=30, pady=15)
    button.config(highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=2, activebackground="#F6A4D1", activeforeground="black")
    return button

# main window function for loading screen
def show_loading_screen(message):
    global loading_label, loading_indicator
    # Show the loading text and progress bar in the same window
    loading_label = tk.Label(main_frame, text=message, font=("Helvetica", 16, "bold"), fg="pink", bg="black")
    loading_label.grid(row=6, column=0, columnspan=2, pady=30)
    
    loading_indicator = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="indeterminate")
    loading_indicator.grid(row=7, column=0, columnspan=2, pady=10)
    loading_indicator.start()

# function to hide the loading screen
def hide_loading_screen():
    if loading_label:
        loading_label.grid_forget()  # Remove the loading text
    if loading_indicator:
        loading_indicator.grid_forget()  # Remove the progress bar

# initialize the main window
root = tk.Tk()
root.title("Simple Neural Network")

# set the background to black (Apple default dark mode)
root.configure(bg="black")

# frame for main content with dark color scheme
main_frame = tk.Frame(root, bg="black")
main_frame.pack(padx=20, pady=20)

# add a logo or welcome message at the top with white text
welcome_label = tk.Label(main_frame, text="Welcome to Your Personal Neural Network", font=("Helvetica", 16, "bold"), bg="black", fg="white")
welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

# input fields for naming the network
tk.Label(main_frame, text="Give me a name for the network:", bg="black", font=("Arial", 12), fg="white").grid(row=1, column=0, sticky="w", padx=5)
name_entry = tk.Entry(main_frame, font=("Arial", 12), bd=2, relief="solid", width=20)
name_entry.grid(row=1, column=1, padx=5, pady=5)

# button to confirm name
name_button = create_button("Confirm Name", confirm_name, "#F6A4D1", "black")
name_button.grid(row=2, column=0, columnspan=2, pady=10)

# button to start training
train_button = create_button("Start Training", training_loop, "#F6A4D1", "black")
train_button.grid(row=3, column=0, columnspan=2, pady=10)

# button to initiate thinking (input process)
think_button = create_button("Think", process_input1, "#F6A4D1", "black")
think_button.grid(row=4, column=0, columnspan=2, pady=10)

# exit button
exit_button = create_button("Exit Program", confirm_exit, "#F6A4D1", "black")
exit_button.grid(row=5, column=0, columnspan=2, pady=20)


root.mainloop()
