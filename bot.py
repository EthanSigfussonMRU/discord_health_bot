from discord.ext import tasks, commands
from decouple import config
import discord
import responses
import datetime as dt

start_time = dt.datetime.now() #to be used

bot_channel = 1162548640053723137
#token handeling
TOKEN = config("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise ValueError("where is bot token")


async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print (e)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    #hook onto a single user
    main_user = client.get_user(None)

    
    
    
    ## on start
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        try:
            await client.get_channel(bot_channel).send(responses.get_response("respond with \"I live\""))
        except Exception as e:
            print (e)
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #hook onto main user 
        if message.author != None:
            main_user = message.author
        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, user_message, )
    

    @tasks.loop(seconds=5)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(bot_channel)  # channel ID goes here
        self.counter += 1
        print("182192391283918239")

    client.run(TOKEN)