import discord
import json

client = discord.Client()


def getTicket():
    """
    used to obtain the bot ticket from user
    :return: ticket
    """
    ticket = input("Please copy and paste your bot ticket here:")
    print("bot will now attempt to record")
    return ticket


def getLogText(message):
    """
    creates a dictionary of all the data relating to a text message.
    :return: textLog
    """
    textLog = {
        "username": str(message.author),
        "message": str(message.content),
        "timestamp": str(message.created_at),
        "channel": str(message.channel)
    }

    return textLog


@client.event
async def on_message(message):
    with open('log.json') as f:  # Imports the json file
        data = json.load(f)

    if message.content != "":  # If the message is a text (not image or video)
        data['messages'].append(getLogText(message))
        with open('log.json', 'w') as f:  # Appends and formats the new text into the json file
            json.dump(data, f, indent=2)
        print("message received at " + str(message.created_at))


client.run(getTicket())
