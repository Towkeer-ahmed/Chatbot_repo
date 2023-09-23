def simple_bot():
    # Define a dictionary containing a list of responses for each input
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a program, but thanks for asking! How can I assist you?",
        "bye": "Goodbye! Have a great day!",
    }

    print("Simple Bot: Hi! Type 'bye' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ").lower().strip()
        
        # Check if the user wants to end the chat
        if user_input == 'bye':
            print("Simple Bot: Bye! Have a great day!")
            break
        
        # Get the response from the bot, if available, otherwise use a default response
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        print(f"Simple Bot: {response}")

if __name__ == "__main__":
    simple_bot()
