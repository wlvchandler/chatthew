import discord
import os
import re

client = discord.Client()

#this can be more clever
def is_chatthew_request(message):
    request = None
    for r in ['chatthew,','Chatthew,','chatthew!', 'Chatthew!']:
        if message.content.startswith(r):
            request = ' '.join(message.content.split()[1:])
    return request

def process_request(request):
    response = None

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print('Alright alright alright... Chatthew in the house')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    request = is_chatthew_request(message)
    if request:
        await message.channel.send(process_request(request))


client.run(os.getenv('TOKEN'))
