import discord
import os
import re

client = discord.Client()

#this can be more clever
def is_chatthew_request(message):
    request = None
    for r in ['chatthew,','Chatthew,','chatthew!', 'Chatthew!']:
        if message.content.startswith(r):
            request = message.content.strip(r).strip()
    return request

def process_request(message, request):
    await message.channel.send(f"request: {request}")
    

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
        process_request(message, request)
 
client.run(os.getenv('TOKEN'))
