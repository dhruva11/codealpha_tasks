import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

# ----------- BOT LOGIC -------------
class ChatBot:
    def __init__(self):
        self.state = None
        self.current_question = None
        self.memory = {}  # store user answers
        self.asked_questions = set()  # track asked questions

        # --- 25 Questions with pos/neg answers ---
        self.questions = [
            {"id": "fav_lang", "q": "Do you like Python programming?",
             "pos": "Great! Python is my favorite too. 🐍",
             "neg": "Oh, that’s surprising. I find Python very versatile 🐍"},
            {"id": "like_ai", "q": "Do you like AI and chatbots?",
             "pos": "Awesome! I love AI as well 🤖",
             "neg": "That’s okay, not everyone has to like AI. I still enjoy it 🤖"},
            {"id": "enjoy_coding", "q": "Do you enjoy coding projects?",
             "pos": "Nice! Building things with code is exciting 🚀",
             "neg": "I see, coding isn’t for everyone — but it can be rewarding 💡"},
            {"id": "like_gaming", "q": "Do you enjoy playing video games?",
             "pos": "Cool! Games are a great way to relax 🎮",
             "neg": "Fair enough, games aren’t for everyone 🙂"},
            {"id": "like_music", "q": "Do you like listening to music?",
             "pos": "Great! Music makes everything better 🎶",
             "neg": "That’s fine, silence can be peaceful too 🌿"},
            {"id": "outdoors", "q": "Do you enjoy spending time outdoors?",
             "pos": "Nice! Fresh air and nature are wonderful 🌳",
             "neg": "That’s okay, being indoors can be cozy 🏠"},
            {"id": "like_movies", "q": "Do you enjoy watching movies?",
             "pos": "Cool! Movies are a fun escape 🎬",
             "neg": "That’s fine, not everyone enjoys movies 🍿"},
            {"id": "like_sports", "q": "Do you like sports?",
             "pos": "Awesome! Sports are great for health and fun ⚽",
             "neg": "No worries, sports aren’t for everyone 🏆"},
            {"id": "like_reading", "q": "Do you like reading books?",
             "pos": "That's great! Reading expands knowledge 📚",
             "neg": "That’s fine, there are many other ways to learn 📱"},
            {"id": "like_coffee", "q": "Do you like drinking coffee?",
             "pos": "Me too! Coffee keeps us energized ☕",
             "neg": "That’s okay, tea works just as well 🍵"},
            {"id": "like_travel", "q": "Do you like traveling?",
             "pos": "That’s awesome! Traveling opens new perspectives ✈️",
             "neg": "That’s okay, home can be the best place 🏡"},
            {"id": "like_art", "q": "Do you like art?",
             "pos": "Art is inspiring and creative 🎨",
             "neg": "That’s fine, not everyone is into art 🖼️"},
            {"id": "like_pets", "q": "Do you like having pets?",
             "pos": "Pets are amazing companions 🐶🐱",
             "neg": "That’s fine, pets are not for everyone 🐾"},
            {"id": "like_food", "q": "Do you enjoy trying new foods?",
             "pos": "Yum! Exploring food is fun 🍜",
             "neg": "That’s fine, sticking to favorites works too 🍽️"},
            {"id": "like_dance", "q": "Do you like dancing?",
             "pos": "That’s awesome! Dancing is fun 💃🕺",
             "neg": "No worries, not everyone likes to dance 🙂"},
            {"id": "like_singing", "q": "Do you like singing?",
             "pos": "Cool! Singing is joyful 🎤",
             "neg": "That’s fine, not everyone likes singing 🎶"},
            {"id": "like_space", "q": "Do you like space and astronomy?",
             "pos": "The universe is fascinating 🌌",
             "neg": "That’s okay, it’s not everyone’s interest 🌍"},
            {"id": "like_history", "q": "Do you like history?",
             "pos": "Great! History teaches us so much 📖",
             "neg": "That’s fine, not everyone enjoys history 🏛️"},
            {"id": "like_science", "q": "Do you like science?",
             "pos": "Science is amazing 🔬",
             "neg": "That’s okay, not everyone is into science ⚗️"},
            {"id": "like_math", "q": "Do you like mathematics?",
             "pos": "Awesome! Math is the language of the universe ➕➗",
             "neg": "That’s fine, math can be tricky for many people ➖✖️"},
            {"id": "like_tech", "q": "Do you like technology?",
             "pos": "Tech makes life exciting 💻",
             "neg": "That’s okay, sometimes simple is better 📻"},
            {"id": "like_cooking", "q": "Do you enjoy cooking?",
             "pos": "Nice! Cooking is both fun and tasty 👩‍🍳",
             "neg": "That’s fine, ordering food works too 🍔"},
            {"id": "like_philosophy", "q": "Do you like philosophy?",
             "pos": "That’s deep! Philosophy makes us think 🧠",
             "neg": "That’s fine, not everyone likes abstract ideas 💭"},
            {"id": "like_learning", "q": "Do you enjoy learning new things?",
             "pos": "Awesome! Learning keeps us growing 📘",
             "neg": "That’s fine, routines can be comfortable too 🔄"},
            {"id": "like_comedy", "q": "Do you like comedy shows?",
             "pos": "Laughter is the best medicine 😂",
             "neg": "That’s fine, humor is subjective 🙂"},
        ]

    def classify_sentiment(self, text):
        text = text.lower()
        positive_words = ["yes", "yeah", "yep", "sure", "of course", "love", "like", "absolutely"]
        negative_words = ["no", "nope", "nah", "never", "not really", "don't"]

        if any(word in text for word in positive_words):
            return "positive"
        elif any(word in text for word in negative_words):
            return "negative"
        return "neutral"

    def get_greeting(self):
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning! 🌅 I'm ChatBot."
        elif 12 <= hour < 18:
            return "Good afternoon! ☀️ I'm ChatBot."
        else:
            return "Good evening! 🌙 I'm ChatBot."

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()

        if self.state == "awaiting_answer" and self.current_question:
            q = self.current_question
            qid = q["id"]

            sentiment = self.classify_sentiment(user_input)
            if sentiment == "positive":
                reply = q["pos"]
                self.memory[qid] = "yes"
            elif sentiment == "negative":
                reply = q["neg"]
                self.memory[qid] = "no"
            else:
                reply = f"Got it! You said: {user_input}"
                self.memory[qid] = user_input

            self.asked_questions.add(qid)

            unanswered = [ques for ques in self.questions if ques["id"] not in self.asked_questions]
            if unanswered:
                self.current_question = random.choice(unanswered)
                follow_up = f"\n\nHere's another one: {self.current_question['q']}"
                self.state = "awaiting_answer"
                return reply + follow_up
            else:
                self.state = None
                self.current_question = None
                return reply + "\n\nYou've answered all my questions! 🎉"

        if "bye" in user_input:
            return "Goodbye! 👋 Have a great day!"
        elif "help" in user_input:
            return "You can chat with me or type 'bye' to exit."
        else:
            return "I didn't understand that. Type 'help' to see what I can do."

    def start_question(self):
        unanswered = [ques for ques in self.questions if ques["id"] not in self.asked_questions]
        if unanswered:
            self.current_question = random.choice(unanswered)
            self.state = "awaiting_answer"
            return f"{self.current_question['q']}"
        else:
            return "You've already answered all my questions! 🎉"


# ----------- GUI FUNCTIONS -------------
def send_message(event=None):
    user_msg = user_input.get().strip()
    if not user_msg:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n", "user")
    chat_area.insert(tk.END, "Bot is typing...\n", "bot")
    chat_area.update()

    bot_reply = bot.get_response(user_msg)

    chat_area.delete("end-2l", "end-1l")
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    user_input.delete(0, tk.END)

    if "bye" in user_msg.lower():
        root.after(5000, root.destroy)


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)


def exit_app():
    root.destroy()


# ----------- GUI SETUP -------------
root = tk.Tk()
root.title("🤖 Smart ChatBot")
root.geometry("600x550")
root.configure(bg="#f9f9f9")

bot = ChatBot()

chat_area = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD,
                                      font=("Arial", 12), bg="white")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, f"🤖 Bot: {bot.get_greeting()}\nType 'help' for commands.\n\n", "bot")
chat_area.insert(tk.END, "🤖 Bot: " + bot.start_question() + "\n\n", "bot")
chat_area.config(state=tk.DISABLED)

frame = tk.Frame(root, bg="#f9f9f9")
frame.pack(fill=tk.X, padx=10, pady=10)

user_input = tk.Entry(frame, font=("Arial", 12))
user_input.insert(0, "Type your message here...")
user_input.bind("<FocusIn>", lambda e: user_input.delete(0, tk.END))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
user_input.bind("<Return>", send_message)

send_button = tk.Button(frame, text="Send", command=send_message,
                        font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(side=tk.RIGHT)

btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(fill=tk.X, pady=5)

clear_button = tk.Button(btn_frame, text="Clear Chat", command=clear_chat,
                         font=("Arial", 11), bg="#f44336", fg="white")
clear_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(btn_frame, text="Exit", command=exit_app,
                        font=("Arial", 11), bg="#555", fg="white")
exit_button.pack(side=tk.RIGHT, padx=5)

user_input.focus()

# ----------- RUN APP -------------
root.mainloop()