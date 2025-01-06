def show_messages(messages: list):
    for message in messages:
        print(message)

def copy_show_messages(messages: list): # For ex 8-10
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)

    print(f"Original messages: {messages}")
    
    print(f"Sent messages: {sent_messages}")

def archieved_messages(messages: list):   # For ex 8-11
    archieved_message = messages
    print(f"Original messages: {messages}")
    print(f"Archieved messages: {archieved_message}")
    print(f"Original messages: {messages}")


class Testing:

    def test_show_messages():
        messgaes = ["Hello", "How are you?", "Are you fine?"]
        show_messages(messgaes)

    def test_copy_show_messages():
        messgaes = ["Hello", "How are you?", "Are you fine?"]
        copy_show_messages(messgaes)

    def test_archieved_messages():
        messgaes = ["Hello", "How are you?", "Are you fine?"]
        archieved_messages(messgaes)