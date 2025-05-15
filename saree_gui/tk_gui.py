'''import tkinter as tk
from query import answer_query

def get_answer():
    question = entry.get()
    answer = answer_query(question)
    result_label.config(text=answer)

# Create GUI window
root = tk.Tk()
root.title("Saree Query Assistant")

# Input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Submit button
button = tk.Button(root, text="Ask", command=get_answer)
button.pack()

# Result label
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

root.mainloop()'''
############################################
'''import tkinter as tk
from tkinter import CENTER
from PIL import Image, ImageTk
from query import answer_query
from tkinter import messagebox

# Theme Colors
BG_COLOR = "#f9f9f9"       # Light grayish white
PRIMARY_COLOR = "#4CAF50"  # Green for primary elements
ACCENT_COLOR = "#66BB6A"   # Lighter green for hover effects
TEXT_COLOR = "#333333"     # Dark gray for text
BUTTON_TEXT_COLOR = "#FFFFFF"  # White for button text
INPUT_BG_COLOR = "#FFFFFF"  # White for input field background
INPUT_BORDER_COLOR = "#DDDDDD"  # Light gray for input field border

# Main Window Setup
root = tk.Tk()
root.title("Saree Assistant")
root.geometry("900x600")
root.configure(bg=BG_COLOR)

# ---------------- CENTER: Main Content ---------------- #

center_frame = tk.Frame(root, bg=BG_COLOR)
center_frame.pack(expand=True, fill="both")

# Decorative Image (Central Orb or Logo)
try:
    orb_image = Image.open("orb.png")  # Replace with your decorative image
    orb_image = orb_image.resize((150, 150), Image.ANTIALIAS)
    orb_photo = ImageTk.PhotoImage(orb_image)
    orb_label = tk.Label(center_frame, image=orb_photo, bg=BG_COLOR)
    orb_label.image = orb_photo  # Keep reference to avoid garbage collection
    orb_label.pack(pady=(50, 20))
except Exception as e:
    orb_label = tk.Label(center_frame, text="🌟", font=("Helvetica", 50), bg=BG_COLOR, fg=PRIMARY_COLOR)
    orb_label.pack(pady=(50, 20))

# Heading Text
heading = tk.Label(center_frame, text="What do you want to know about Sarees?", font=("Helvetica", 18, "bold"),
                   bg=BG_COLOR, fg=TEXT_COLOR)
heading.pack(pady=(10, 30))

# Buttons for Options
def on_button_hover(e):
    e.widget.config(bg=ACCENT_COLOR)

def on_button_leave(e):
    e.widget.config(bg=PRIMARY_COLOR)

def button_action(option):
    print(f"Selected Option: {option}")  # Replace with actual functionality

button_texts = ["Generate Summary", "Find the Best Match", "Learn About Styles"]
for text in button_texts:
    button = tk.Button(center_frame, text=text, font=("Helvetica", 14), bg=PRIMARY_COLOR, fg=BUTTON_TEXT_COLOR,
                       relief="flat", padx=20, pady=10, cursor="hand2", bd=0)
    button.pack(pady=10)
    button.bind("<Enter>", on_button_hover)
    button.bind("<Leave>", on_button_leave)
    button.config(command=lambda t=text: button_action(t))

# ---------------- BOTTOM: Input Field ---------------- #

bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(side="bottom", fill="x", pady=20)

# Input Field
entry = tk.Entry(bottom_frame, font=("Helvetica", 14), bg=INPUT_BG_COLOR, fg=TEXT_COLOR,
                 relief="solid", highlightthickness=1, highlightbackground=INPUT_BORDER_COLOR,
                 highlightcolor=PRIMARY_COLOR, bd=0)
entry.pack(side="left", padx=20, pady=10, ipady=8, expand=True, fill="x")

# Send Button
def on_send():
    user_query = entry.get()
    if not user_query.strip():
        messagebox.showwarning("Empty Input", "Please enter a question.")
        return
    try:
        response = answer_query(user_query)
        messagebox.showinfo("Answer", response)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

send_button = tk.Button(bottom_frame, text="Send", font=("Helvetica", 13, "bold"), bg=PRIMARY_COLOR,
                        fg=BUTTON_TEXT_COLOR, relief="flat", padx=15, pady=7, cursor="hand2", bd=0,
                        command=on_send)
send_button.pack(side="right", padx=20)
send_button.bind("<Enter>", on_button_hover)
send_button.bind("<Leave>", on_button_leave)


root.mainloop()'''
#############333333333333######################################################33
import tkinter as tk
from tkinter import CENTER
from PIL import Image, ImageTk
from query import answer_query  # Import the function to handle queries

# Theme Colors
BG_COLOR = "#f9f9f9"
PRIMARY_COLOR = "#4CAF50"
ACCENT_COLOR = "#66BB6A"
TEXT_COLOR = "#333333"
BUTTON_TEXT_COLOR = "#FFFFFF"
INPUT_BG_COLOR = "#FFFFFF"
INPUT_BORDER_COLOR = "#DDDDDD"

# Main Window Setup
root = tk.Tk()
root.title("Saree Assistant")
root.geometry("900x600")
root.configure(bg=BG_COLOR)

# ---------------- CENTER: Main Content ---------------- #
center_frame = tk.Frame(root, bg=BG_COLOR)
center_frame.pack(expand=True, fill="both")

# Decorative Image
try:
    orb_image = Image.open("orb.png")
    orb_image = orb_image.resize((150, 150), Image.ANTIALIAS)
    orb_photo = ImageTk.PhotoImage(orb_image)
    orb_label = tk.Label(center_frame, image=orb_photo, bg=BG_COLOR)
    orb_label.image = orb_photo
    orb_label.pack(pady=(50, 20))
except Exception:
    orb_label = tk.Label(center_frame, text="🌟", font=("Helvetica", 50), bg=BG_COLOR, fg=PRIMARY_COLOR)
    orb_label.pack(pady=(50, 20))

# Heading Text
heading = tk.Label(center_frame, text="What do you want to know about Sarees?", font=("Helvetica", 18, "bold"),
                   bg=BG_COLOR, fg=TEXT_COLOR)
heading.pack(pady=(10, 30))

# Answer Display Label
result_label = tk.Label(center_frame, text="", font=("Helvetica", 13), bg=BG_COLOR,
                        fg=TEXT_COLOR, wraplength=700, justify="center")
result_label.pack(pady=10)

# Button Hover Effects
def on_button_hover(e):
    e.widget.config(bg=ACCENT_COLOR)

def on_button_leave(e):
    e.widget.config(bg=PRIMARY_COLOR)

# Button Click Placeholder
def button_action(option):
    entry.delete(0, tk.END)
    entry.insert(0, f"Tell me about {option} sarees")

# Buttons
button_texts = ["Banarasi", "Kanjeevaram", "Bandhani"]
for text in button_texts:
    button = tk.Button(center_frame, text=text, font=("Helvetica", 14), bg=PRIMARY_COLOR, fg=BUTTON_TEXT_COLOR,
                       relief="flat", padx=20, pady=10, cursor="hand2", bd=0)
    button.pack(pady=10)
    button.bind("<Enter>", on_button_hover)
    button.bind("<Leave>", on_button_leave)
    button.config(command=lambda t=text: button_action(t))

# ---------------- BOTTOM: Input Field ---------------- #
bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(side="bottom", fill="x", pady=20)

# Input Entry
entry = tk.Entry(bottom_frame, font=("Helvetica", 14), bg=INPUT_BG_COLOR, fg=TEXT_COLOR,
                 relief="solid", highlightthickness=1, highlightbackground=INPUT_BORDER_COLOR,
                 highlightcolor=PRIMARY_COLOR, bd=0)
entry.pack(side="left", padx=20, pady=10, ipady=8, expand=True, fill="x")

# Send Button Action
def handle_send():
    question = entry.get()
    if question.strip():
        answer = answer_query(question)
        result_label.config(text=answer)
        entry.delete(0, tk.END)
    else:
        result_label.config(text="Please enter a question about sarees.")

# Send Button
send_button = tk.Button(bottom_frame, text="Send", font=("Helvetica", 13, "bold"), bg=PRIMARY_COLOR,
                        fg=BUTTON_TEXT_COLOR, relief="flat", padx=15, pady=7, cursor="hand2", bd=0,
                        command=handle_send)
send_button.pack(side="right", padx=20)
send_button.bind("<Enter>", on_button_hover)
send_button.bind("<Leave>", on_button_leave)

# Run the application
root.mainloop()
