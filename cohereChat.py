import cohere

ch_api_key = 'fVHw36A8DdVfH3ubOgu6bjQotk37QinmZLz4X0sq'

# co = cohere.Client(ch_api_key)
#
# #input from user
# message = "why is the sky blue?"
#
# response = co.chat(
#     message,
#     model="command",
#     temperature=0.9#,
#     #chat_history=
# )
#
# answer = response.text
# print(answer)

coach_type = "Maria, a health and fitness coach"
chat_history = []
user_message = {"user_name": "User", "text": "You are " + coach_type}
max_turns = 10

co = cohere.Client(ch_api_key)

for _ in range(max_turns):
    # get user input
    message = input("Send the model a message: ")

    # generate a response with the current chat history
    response = co.chat(
        message,
        temperature=0.8,
        chat_history=chat_history
    )
    answer = response.text

    print(answer)

    # add message and answer to the chat history
    user_message = {"user_name": "User", "text": message}
    bot_message = {"user_name": "Chatbot", "text": answer}

    chat_history.append(user_message)
    chat_history.append(bot_message)