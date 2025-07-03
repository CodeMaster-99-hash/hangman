import tkinter as tk
from tkinter import scrolledtext

# Only show this once when the app starts
WELCOME_MESSAGE = "HELLO! I am chatbot. How can I help you?"

# Function to generate response
def respond_to_input(user_input):
    user_input = user_input.lower()

    if user_input == "bye":
        return "Goodbye, have a nice day!"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! Is there anything you'd like to ask?"
    elif "help" in user_input:
        return "I'll help, tell me what you need."
    elif "how are you" in user_input:
        return "I'm fine, thank you. What about you?"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    else:
        return "I can't answer that. Please ask something else."

# Function triggered when Send button is clicked
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chatarea.config(state=tk.NORMAL)
    chatarea.insert(tk.END, "You: " + user_input + "\n")

    response = respond_to_input(user_input)
    chatarea.insert(tk.END, "Chatbot: " + response + "\n\n")

    chatarea.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Tkinter Window setup
window = tk.Tk()
window.title("Rule-Based Chatbot")
window.geometry("600x500")
window.config(bg="sky blue")

# Chat display area
chatarea = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED, font=("bold", 12))
chatarea.pack(padx=200,pady=200)
chatarea.place(x=50, y=20, width=500, height=300)
chatarea.config(state=tk.NORMAL)
chatarea.insert(tk.END, "Chatbot: " + WELCOME_MESSAGE + "\n\n")
title=tk.Label(window,text="ASK",font=("Times",16,"bold"))
title.place(x=10,y=340)


# Input field
entry = tk.Entry(window, font=("bold", 14))
entry.place(x=80, y=340, width=400)
entry.focus()

# Send button
send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 12))

send_button.place(x=500, y=335, width=80, height=35)



window.mainloop()
