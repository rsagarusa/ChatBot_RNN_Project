import tkinter as tk
from tkinter import *

responses = {
    "hi": "Hello User!",
    "hello": "Hi There!",
    "how are you": "I am Fine",
    "what is python": "Python is a Programming Language",
    "bye": "Goodbye!"
}

# ===========================
# Send Message
# ===========================

def send():

    user_message = entry_box.get()

    chat_box.insert(END, "You : " + user_message + "\\n")

    message = user_message.lower()

    bot_response = responses.get(
        message,
        "Sorry I don't understand"
    )

    chat_box.insert(END, "Bot : " + bot_response + "\\n\\n")

    entry_box.delete(0, END)

# ===========================
# GUI Window
# ===========================

window = tk.Tk()

window.title("Python ChatBot")

window.geometry("500x600")

chat_box = Text(window, font=("Arial", 12))
chat_box.pack(pady=20)

entry_box = Entry(window, width=40, font=("Arial", 14))
entry_box.pack(pady=10)

send_button = Button(
    window,
    text="Send",
    command=send,
    font=("Arial", 12)
)

send_button.pack()

window.mainloop()
