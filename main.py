import tkinter as tk
from tkinter import messagebox

def print_health_info():
    health_card_no = entry.get()

    # Create a new window for displaying health information
    info_window = tk.Toplevel(root)
    info_window.title("Health Information")

    # Display health information in the new window with a larger font
    info_label = tk.Label(info_window, text=f"Health Card Number: 10001\n"
                                            f"Patient Name: Jacob K George\n"
                                            f"Date of Birth: April 27, 2006\n"
                                            f"Blood Type: O+\n"
                                            f"Allergies: None"
                                            f"Medications (if any): None",
                                            font=("Arial", 16))  # Adjust font size as needed
    info_label.pack(padx=20, pady=10)

# Create the main application window
root = tk.Tk()
root.title("Health Card Info")
root.geometry("700x700")

# Create a label and entry for the health card number with increased font size
label = tk.Label(root, text="Enter the health card no.", font=("Arial", 14))
label.pack(pady=5)
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=5)

# Create a button to trigger the print statements with increased font size
button = tk.Button(root, text="Print Info", command=print_health_info, font=("Arial", 14))
button.pack(pady=10)

# Run the main event loop
root.mainloop()
