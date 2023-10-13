import discord
import responses
import datetime
import time
print(time.ctime)

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print (e)

def run_discord_bot():
    TOKEN = "MTE2MjQ4MDI1MDE1NzAxNTEzMQ.GrN4A9.o2GG6UXvGgqqo0dMPBNdPaUfsWQf3eKwaZl1_g"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, user_message, )
    client.run(TOKEN)