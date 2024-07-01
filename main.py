import random, string
import customtkinter
import tkinter
import pyperclip
from zxcvbn import zxcvbn

numberArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowerLettersArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLettersArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolArray = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '!'] 

class NoCheckBoxSelectedError(Exception):
    """Raised when no checkboxes for character types are selected."""
    pass

def passGen():
	try:
		characters = []

		if numVar.get() == "on":
			characters += numberArray

		if lowVar.get() == "on":
			characters += lowerLettersArray

		if uppVar.get() == "on":
			characters += upperLettersArray

		if symVar.get() == "on":
			characters += symbolArray

		if (numVar.get() == "off") and (lowVar.get() == "off") and (uppVar.get() == "off") and (symVar.get() == "off"):
			raise NoCheckBoxSelectedError("Please Select at least one character type.")

		passlength = int(passlen.get())
		
		password = ''.join(random.choice(characters) for _ in range(passlength))
		
		if showVar.get() == "on":
			passLabel.configure(text=f"Password: {password}")

		if copyVar.get() == "on":
			pyperclip.copy(password)

		results = zxcvbn(password)
		score = int(results['score'])
		strengthScore = score * 0.25
		strengthbar.set(strengthScore)

		if score == 0:
			strengthLabel.configure(text="Strength: Terrible")
		elif score == 1:
			strengthLabel.configure(text="Strength: Poor")
		elif score == 2:
			strengthLabel.configure(text="Strength: Okay")
		elif score == 3:
			strengthLabel.configure(text="Strength: Good")
		elif score == 4:
			strengthLabel.configure(text="Strength: Great")
	
	except ValueError:
		passLabel.configure(text="Error: Invalid input. Please enter a number for password length.")
	except Exception as e:
		passLabel.configure(text=f"Error: {e}")

# GUI setup
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  
app.geometry("720x600")
app.title("ProProgrammer's Password Generator")  # My touch!

# Configure Grid Weights (for responsiveness)
app.grid_columnconfigure((0, 1), weight=1)  # Columns 0 and 1 expand equally
app.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)  # All rows expand equally

# --- Title ---
title = customtkinter.CTkLabel(app, text="Configure Password", font=("Helvetica", 24, "bold"))
title.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

# --- Password Length Section ---
passlength_label = customtkinter.CTkLabel(app, text="Password Length:")
passlength_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Align left (west)

passlengthVar = tkinter.StringVar()
passlen = customtkinter.CTkEntry(app, width=500, height=20, textvariable=passlengthVar)
passlen.grid(row=1, column=1, padx=10, pady=10)

# --- Checkbox Options ---
numVar = customtkinter.StringVar(value="off")
numCheckbox = customtkinter.CTkCheckBox(app, text="Numbers", variable=numVar, onvalue="on", offvalue="off")
numCheckbox.grid(row=2, column=0, sticky="w", padx=20)  # Align left

lowVar = customtkinter.StringVar(value="off")
lowCheckbox = customtkinter.CTkCheckBox(app, text="Lower Case Letters", variable=lowVar, onvalue="on", offvalue="off")
lowCheckbox.grid(row=2, column=1, sticky="w", padx=180)  # Align left, same row

uppVar = customtkinter.StringVar(value="off")
uppCheckbox = customtkinter.CTkCheckBox(app, text="Upper Case Letters", variable=uppVar, onvalue="on", offvalue="off")
uppCheckbox.grid(row=3, column=0, sticky="w", padx=20)  # Align left

symVar = customtkinter.StringVar(value="off")
symCheckbox = customtkinter.CTkCheckBox(app, text="Symbols", variable=symVar, onvalue="on", offvalue="off")
symCheckbox.grid(row=3, column=1, sticky="w", padx=180)  # Align left, same row

# --- Show Password Checkbox ---
showVar = customtkinter.StringVar(value="on")
showCheckbox = customtkinter.CTkCheckBox(app, text="Show Password", variable=showVar, onvalue="on", offvalue="off")
showCheckbox.grid(row=4, column=0, sticky="w", padx=20) 

# --- Copy Password Checkbox ---
copyVar = customtkinter.StringVar(value="off")
copyCheckbox = customtkinter.CTkCheckBox(app, text="Copy Password", variable=copyVar, onvalue="on", offvalue="off")
copyCheckbox.grid(row=4, column=1, sticky="w", padx=180)

# --- Strength Label and Progress Bar --- 
strengthLabel = customtkinter.CTkLabel(app, text="Generate a password to get the strength")
strengthLabel.grid(row=6, column=0, columnspan=2, pady=10)

strengthbar = customtkinter.CTkProgressBar(app, width=400, orientation="horizontal")
strengthbar.set(0)
strengthbar.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# --- Generate Button ---
genButton = customtkinter.CTkButton(app, width=150, height=30, text="Generate Password", command=passGen)
genButton.grid(row=9, column=0, columnspan=2, pady=10)

# --- Password Label ---
passLabel = customtkinter.CTkLabel(app, text="")
passLabel.grid(row=11, column=0, columnspan=2, pady=10) 

app.mainloop()