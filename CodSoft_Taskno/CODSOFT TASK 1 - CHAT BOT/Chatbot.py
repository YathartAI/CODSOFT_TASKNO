from datetime import datetime 
import random

quotes = [
    "Success is the sum of small efforts repeated every day. 💪",
    "Believe in yourself. You are capable of amazing things. 🌟",
    "The best way to predict the future is to create it. 🚀",
    "Dream big, work hard, stay focused. 🎯",
    "Every expert was once a beginner. Keep learning! 📚"
]

def show_welcome():
    print("=" * 60)
    print("🤖         AI CHATBOT - CODSOFT TASK 1         🤖")
    print("=" * 60)
    print("Hello! Welcome to the AI Chatbot.")
    print("I can answer simple questions based on predefined rules.")
    print("Type 'bye' anytime to end the conversation.")
    print("=" * 60)
    print()

show_welcome()



def show_help():
    print("\n📋 You can ask me:")
    print("• hi / hello")
    print("• how are you")
    print("• what is your name")
    print("• what can you do")
    print("• who created you")
    print("• time")
    print("• date")
    print("• joke")
    print("• motivate me")
    print("• thank you")
    print("• bye")
    print()

show_help()



while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello"]:
        print("Bot: Hello! How can I help you today?")
    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I'm just a program, but I'm doing great! 😊")
    elif user_input in ["what is your name", "what's your name"]:
        print("Bot: I am an AI Chatbot created for the CodSoft task.")
    elif user_input in ["what can you do", "what can you do?"]:
        print("Bot: I can answer simple questions based on predefined rules.")
    elif user_input in ["time", "current time", "what is the time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}. ⏰")
    elif user_input in ["date", "today", "today's date", "what is today's date"]:
        current_date = datetime.now().strftime("%d %B %Y")
        print(f"Bot: Today's date is {current_date}. 📅")
    elif user_input in ["motivate me", "motivation", "give me motivation"]:
        print("Bot: Keep going! Every small step brings you closer to your goal. 💪")
    elif user_input in ["thank you", "thanks", "thankyou"]:
        print("Bot: You're welcome! 😊 Happy to help.")
    elif user_input in ["good morning", "morning"]:
        print("Bot: Good morning! ☀️ Have a wonderful day!")
    elif user_input in ["good afternoon", "afternoon"]:
        print("Bot: Good afternoon! 🌤️ Hope you're having a great day!")
    elif user_input in ["good evening", "evening"]:
        print("Bot: Good evening! 🌙 Hope your day went well!")

    elif user_input in ["who created you", "who made you", "who is your creator"]:
        print("Bot: I was created by Yatharth using Python as part of the CodSoft AI Internship.")

    elif user_input in ["help", "menu", "commands"]:
        print("\n📋 You can ask me:")
        print("• hi / hello")
        print("• how are you")
        print("• what is your name")
        print("• what can you do")
        print("• who created you")
        print("• time")
        print("• date")
        print("• joke")
        print("• motivate me")
        print("• thank you")
        print("• bye")

    elif user_input in ["motivate me", "motivation", "quote", "inspire me"]:
        print("Bot:", random.choice(quotes))

    elif user_input in ["help", "menu", "commands"]:
        show_help()    

    elif user_input in ["joke", "tell me a joke", "make me laugh"]:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😂",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "Why did the bicycle fall over? Because it was two-tired! 🚲",
            "Why did the math book look sad? Because it had too many problems. 📚",
            "Why don't programmers like nature? It has too many bugs. 🐛"
        ]
        print("Bot:", random.choice(jokes))


    elif user_input in ["who created you", "who made you", "who is your creator"]:
        print("Bot: I was created by Yatharth using Python as part of the CodSoft AI Internship.")     

    elif user_input in ["help", "menu", "welcome"]:
        show_welcome() 

    elif user_input in ["bye", "exit", "quit"]:
        print("\nBot: Goodbye! Have a wonderful day. 👋")
        print("\n" + "=" * 60)
        print("        Thank you for using AI Chatbot 🤖")
        print("          Developed by Yatharth Singhal")
        print("=" * 60)
        break