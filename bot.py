import discord
import responses
import key
import time
# 534723950656
# 2733747207233


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
        # implement method that waits for response consisting of a time in minutes from user if message is "set customs time"
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = key.key
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] != '?':
            return
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)

    client.run(TOKEN)
