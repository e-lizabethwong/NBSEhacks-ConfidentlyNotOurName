def coherechat(coach_type, message):
    import cohere
    ch_api_key = 'fVHw36A8DdVfH3ubOgu6bjQotk37QinmZLz4X0sq'
    chat_history = []
    max_turns = 10
    chat_history = []
    co = cohere.Client(ch_api_key)
    user_message = {"user_name": "User", "text": "You are " + coach_type}
    for _ in range(max_turns):
        # get user input
        # generate a response with the current chat history
        response = co.chat(
            message,
            temperature=0.8,
            chat_history=chat_history,
            preamble_override="you give positive, polite, helpful, and inclusive advice based on facts",
            connectors=[{"id": "web-search"}]
        )
        answer = response.text

        # add message and answer to the chat history
        user_message = {"user_name": "User", "text": message}
        bot_message = {"user_name": "Chatbot", "text": answer}

        chat_history.append(user_message)
        chat_history.append(bot_message)