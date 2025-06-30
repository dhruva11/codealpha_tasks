import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

# ----------- BOT LOGIC -------------
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 😊"
    elif "how are you" in user_input:
        return "I'm great! Thanks for asking. How about you?"
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a great day!"
    elif "your name" in user_input:
        return "I'm ChatBot, your virtual assistant!"
    elif "help" in user_input:
        return (
            "Here are some things you can ask me:\n"
            "- hello / hi\n"
            "- how are you\n"
            "- what's your name\n"
            "- tell me a joke\n"
            "- date\n"
            "- time\n"
            "- help\n"
            "- bye"
        )
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to therapy? It had too many bytes.",
            "Why don’t programmers like nature? It has too many bugs.",
            "What did the spider do on the computer? Made a website!"
        ]
        return random.choice(jokes)
    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}."
    else:
        return "I didn't understand that. Can you please rephrase? If you need help, type 'help'."

# ----------- SEND MESSAGE FUNCTION -------------
def send_message(event=None):
    user_msg = user_input.get().strip()
    if not user_msg:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n", "user")

    bot_reply = get_bot_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    user_input.delete(0, tk.END)

    # Close app after 5 seconds if user says "bye"
    if "bye" in user_msg.lower():
        root.after(5000, root.destroy)

# ----------- GUI SETUP -------------
root = tk.Tk()
root.title("🤖 Smart ChatBot")
root.geometry("500x500")
root.configure(bg="#f2f2f2")

chat_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12), bg="white")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

# 👉 Welcome message on start
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "🤖 Bot: Hello! I'm ChatBot.\nType 'help' to see what I can do.\n\n", "bot")
chat_area.config(state=tk.DISABLED)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(fill=tk.X, padx=10, pady=10)

user_input = tk.Entry(frame, font=("Arial", 12))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
user_input.bind("<Return>", send_message)

send_button = tk.Button(frame, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(side=tk.RIGHT)

user_input.focus()

# ----------- RUN APP -------------
root.mainloop()
