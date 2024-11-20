import random

chat={
    "hello": ["Hi there!🙏", "Hello!🙏", "Hey🙏! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!👍", "I'm here to assist you!👍", "I'm functioning well, thanks!👍"],
    "what is your name": ["I'm a chatbot created to help you.😍", "You can call me Chatbot!🤩",
                          "I'm your virtual assistant!🤩"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def chat_process(text):
    text=text.lower()
    for key in chat:
        if key in text:
            return random.choice(chat[key])
    return "I'm sorry, I don't understand. Can you please rephrase?"

print("Hello! I'm a chatbot. Type 'bye' to exit.")

while True:
    text1=input("You:")

    if text1.lower() == "bye":
        print("Chatbot: Goodbye! Take care!")
        break

    response = chat_process (text1)
    print("chatbot:",response)