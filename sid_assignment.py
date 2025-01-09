import tkinter as tk
from tkinter import filedialog, messagebox

def create_file():
    # Prompt the user to specify a new file name
    file_path = filedialog.asksaveasfilename(
        title="Create a new file",
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if not file_path:
        return

    try:
        # Create the file (overwriting if it already exists)
        with open(file_path, "w") as file:
            file.write("")  # Create an empty file
        messagebox.showinfo("Success", f"File '{file_path}' created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def append_to_file():
    # Get the input text
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "No text to append!")
        return

    # Get the file path
    file_path = filedialog.askopenfilename(
        title="Select a file to append to",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if not file_path:
        return

    try:
        # Append text to the file
        with open(file_path, "a") as file:
            file.write(text + "\n")
        messagebox.showinfo("Success", f"Text appended to file '{file_path}' successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_file_content():
    # Get the file path
    file_path = filedialog.askopenfilename(
        title="Select a file to display",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if not file_path:
        return

    try:
        # Read and display the file content
        with open(file_path, "r") as file:
            content = file.read()
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("File Operations: Create, Append, Display")

# Create and place a button for creating a new file
create_button = tk.Button(root, text="Create New File", command=create_file)
create_button.pack(pady=5)

# Create and place a label for input
instruction_label = tk.Label(root, text="Enter text to append:")
instruction_label.pack(pady=5)

# Create and place a Text widget for input
text_input = tk.Text(root, width=50, height=5)
text_input.pack(pady=5)

# Create and place buttons for appending and displaying
append_button = tk.Button(root, text="Append to File", command=append_to_file)
append_button.pack(pady=5)

display_button = tk.Button(root, text="Display File Content", command=display_file_content)
display_button.pack(pady=5)

# Create and place a Text widget to display file content
text_display = tk.Text(root, width=50, height=10, state=tk.NORMAL)
text_display.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()