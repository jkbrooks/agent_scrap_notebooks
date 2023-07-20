import chainlit as cl

@cl.on_chat_start
def main():
    res = cl.AskUserMessage(content="What is your name?", timeout=10).send()
    if res:
        cl.Message(
            content=f"Your name is: {res['content']}",
        ).send()


@cl.on_message
def main(message: str):
    # Your custom logic goes here...

    # Send a response back to the user
    cl.Message(
        content=f"Received: {message}",
    ).send()


