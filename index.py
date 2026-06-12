print("AI Chatbot Started")

while True:

    user = input("You: ").lower()

    if user == "hi":
        response = "Hello!"

    elif user == "hello":
        response = "Hi there!"

    elif user == "how are you":
        response = "I am fine."

    elif user == "what is your name":
        response = "My name is AI Chatbot."

    elif user == "how old are you":
        response = "I am ageless."

    elif user == "who created you":
        response = "I was created using Python."

    elif user == "thank you":
        response = "You are welcome."

    elif user == "help":
        response = "How can I help you?"

    elif user == "what is ai":
        response = "AI means Artificial Intelligence."

    elif user == "which course":
        response = "I know Python, AI and ML."

    elif user == "bye":
        response = "Goodbye!"

        print("Bot:", response)

        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"User: {user}\n")
            file.write(f"Bot: {response}\n\n")

        break

    else:
        response = "Sorry, I don't understand."

    print("Bot:", response)

    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot: {response}\n\n")