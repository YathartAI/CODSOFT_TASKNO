print("=" * 50)
print("🤖 Welcome to AI Chatbot!")
print("=" * 50)

name = input("What is your name? ")
print(f"\nHello, {name}! 😊")
print("Type 'bye' anytime to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I assist you today?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking. ❤️")

    elif user_input == "what is your name":
        print("Bot: I am an AI Chatbot created using Python.")

    elif user_input == "what can you do":
        print("Bot: I can chat with you and answer simple questions.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.") 