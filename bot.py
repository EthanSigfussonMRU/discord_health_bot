from discord.ext import tasks
from decouple import config
import discord
import responses
import datetime as dt
import datetime

start_time = dt.datetime.now()
counter = 0
bot_channel = 1162548640053723137
TOKEN = config("DISCORD_BOT_TOKEN")

utc = datetime.timezone.utc
times = [
    datetime.time(hour=8, tzinfo=utc),
    datetime.time(hour=4, minute=6, tzinfo=utc),
    datetime.time(hour=16, minute=40, second=30, tzinfo=utc)
]


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

    
    ##on certain amount of time passing
    @tasks.loop(time=times)
    async def prompt (self):
        print("My task is running!")
        await client.get_channel(bot_channel).send(responses.get_response("FFFsay \"I live\""))


    ## on start
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        try:
            await client.get_channel(bot_channel).send(responses.get_response("say \"I live\""))
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
    client.run(TOKEN)