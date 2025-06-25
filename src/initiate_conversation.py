from constants.bots import bot_1

def initiate_conversation():
    initial_input = "Hi, how are you?"
    answer = bot_1.ask(initial_input)
    return answer