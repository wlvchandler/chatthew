import discord
import os
import re
import random
from fact import generate_fact

client = discord.Client()

#this can be more clever
def is_chatthew_request(message):
    request = None
    for r in ['chatthew,','chatthew!']:
        if message.content.lower().startswith(r):
            request = ' '.join(message.content.split()[1:])
    return request

def process_request(request):
    # TODO: make this a map?
    response = '' # can't return None
    subcommand = request.lower()
    if subcommand == 'trivia':
        response = 'Hype likes:\na) ants\nb) feet\nc) filthy grandmother pornography\nd) a & b\ne) None of the above'
    elif subcommand in ['pun','ant-fact']:
        response = generate_fact(subcommand)
    elif subcommand == 'simp':
        response = ':pleading_face: :point_right: :point_left: is there anything my Queen needs'
    return response

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
        if request.lower() == 'meme':
            meme = random.choice(os.listdir("img/memes"))
            await message.channel.send(file=discord.File(open(f'img/memes/{meme}','rb')))
            await message.channel.send('Is this a le funnie maeme?')  # add voting reactions
        else:
            await message.channel.send(process_request(request))


client.run(os.getenv('TOKEN'))
