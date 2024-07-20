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

class Testing:

    def test_show_messages()
        