import json
import random

with open("intents.json", "r") as file:
    data = json.load(file)

print("Chatbot Started")
print("Type quit to exit")

while True:

    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Goodbye!")
        break

    found = False

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if user.lower() == pattern.lower():

                response = random.choice(intent["responses"])

                print("Bot:", response)

                with open("chat_history.txt", "a") as history:
                    history.write(f"User: {user}\n")
                    history.write(f"Bot: {response}\n\n")

                found = True
                break

        if found:
            break

    if not found:

        response = "I don't understand."

        print("Bot:", response)

        with open("chat_history.txt", "a") as history:
            history.write(f"User: {user}\n")
            history.write(f"Bot: {response}\n\n")