from discord.ext import tasks
import discord
import responses
import datetime as dt

start_time = dt.datetime.now()
counter = 0
bot_channel = 1162548640053723137
##


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

    current_time = dt.datetime.now()

    @tasks.loop(seconds=10)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel(bot_channel)  # channel ID goes here
        self.counter += 1
        await channel.send(responses.get_response(f"add 1 to the following number and respond with only that result {self.counter}"))
    
    ##on certain amount of time passing
    if start_time - current_time > dt.timedelta(seconds=10):
        print("10 seconds have passed")

    if start_time - current_time > dt.timedelta(minutes=5):
        print("5 minutes has passed")
        try:
            bot_channel.send(responses.get_response("this prompt is supposed to be sent 5 minutes after this program first runs"))
        except Exception as e:
            print (e)


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

        print(f'{username} said: "{user_message}" ({channel})')

        await send_message(message, user_message, )
    client.run(TOKEN)