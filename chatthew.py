import discord
import os

#from datetime import datetime
#from threading import Timer

client = discord.Client()

def set_reminder(content):
    time = ''
    if content[0] == 'daily':
        time = content[1:]
    return f'Setting reminder at {time}'


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # if message.content.startswith('bb remind'):
    #     await message.channel.send(set_reminder(message.content.split()[2:]))

client.run('TODO_TOKEN_HERE')
