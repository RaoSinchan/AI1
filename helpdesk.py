# Define a dictionary of common problems and their solutions
problem_dict = {
    "Printer not working": "Check that it's turned on and connected to the network.",
    "Can't log in": "Make sure you're using the correct username and password.",
    "Software not installing": "Check that your computer meets the system requirements.",
    "Internet connection not working": "Restart your modem or router.",
    "Email not sending": "Check that you're using the correct email server settings."
}

# Define a function to handle user requests
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."

# Main loop to prompt user for input
while True:
    user_input = input("What's the problem? Type 'exit' to quit: ")
    response = handle_request(user_input)
    print(response)
    if user_input.lower() == "exit":
        break
