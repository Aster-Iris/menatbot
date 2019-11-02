import discord
import os

# todo set up logging

# Obtaining the discord key from the deployment machine
client_token = os.environ['MENAT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    """
    Ensure we can connect succesfuly, print which servers we're connected to
    """
    print(f'{client.user} has connected to discord')
    for guild in client.guilds:
        print(f'menat is connected to {guild}')

@client.event
async def on_message(message):
    """
    Function that runs every time a new message is sent, basically the heart of the bot
    :param message: The message object, see https://discordpy.readthedocs.io/en/latest/api.html#message
    """
    print(f'{message.guild}|{message.channel}|{message.author}: {message.content}')

if __name__ =="__main__":
    client.run(client_token)