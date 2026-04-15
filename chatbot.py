import random
from datetime import datetime

# Responses with multiple options
responses = {
    "hello": ["Hi 😊", "Hello 👋", "Hey there!"],
    "hi": ["Hi!", "Hello 👋"],
    "name": ["I am a chatbot 🤖", "You can call me ChatBot!"],
    "course": ["We offer B.Tech, BCA, and MBA 🎓"],
    "fees": ["Fees vary by course 💰"],
    "location": ["We are in Karnataka 📍"],
    "contact": ["Call us at 9876543210 📞"]
}

print("🤖 Chatbot: Hello! Type 'help' for options or 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Exit
    if "bye" in user or "exit" in user:
        print("Bot: Goodbye! Have a nice day 🌟")
        break

    # Help menu
    elif "help" in user:
        print("""Bot:
You can ask me:
- hello / hi
- name
- course
- fees
- location
- contact
- time / date
- bye (to exit)
""")

    # Time
    elif "time" in user:
        now = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", now)

    # Date
    elif "date" in user:
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    else:
        found = False

        for key in responses:
            if key in user:
                print("Bot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Bot: Sorry, I didn't understand that 😅")