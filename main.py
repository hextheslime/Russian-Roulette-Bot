import discord
import discord.utils
import random
import time
from datetime import timedelta, datetime, timezone

BOTTOKEN = "" # Put your bot token here.

class Client(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    async def on_message(self, message):
        if message.content == "russianroulette start": # Command to begin a round of russian roulette.
                if runninggame == False:
                    cc = random.randint(1, 6)
                    chamber = 0
                    runninggame = True
                    await message.channel.send(f"**{message.author.display_name}** started a new game of russian roulette! type `russianroulette` to participate!")
                else:
                    await message.channel.send(f"A game is already running! Use 'russianroulette' to participate!")
        if message.content == "russianroulette": # Command to play during a round of russian roulette.
                if runninggame == True:
                    chamber += 1
                    if chamber == cc:
                        runninggame = False
                        await message.channel.send(f"the gun fired! **{message.author.display_name}** has been *taken care of*!\n-# type `russianroulette start` to start a new round!")
                        try: 
                            if isinstance(message.author, discord.Member):
                                until = datetime.now(timezone.utc) + timedelta(seconds=60) # Timeout duration in seconds.
                            await message.author.edit(timed_out_until=until)
                        except(Exception):
                             await message.channel.send(f"Exception occured: `{Exception}`") # The most common exception is caused by the bot trying to time out an administrator.
                    else:
                        await message.channel.send(f'Phew, this chamber was empty! **{message.author.display_name}** gets to live another day!')
                        if chamber == 5:
                            runninggame = False
                            await message.channel.send(f'Looks like the bullet was in the last chamber. Since nobody is dumb enough to get themselves willingly shot, start a new game with `russianroulette start`!')
                else: await message.channel.send(f"There's no game ongoing! Start a new one with `russianroulette start`!")

intents = discord.Intents.default()
intents.message_content = True
 
client = Client(intents=intents)
client.run(BOTTOKEN)