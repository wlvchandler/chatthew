import discord
import os
import re
from fact import generate_fact
from trivia import generate_question

client = discord.Client()


# this can be more clever
def is_chatthew_request(message):
    request = None
    for r in ['chatthew,', 'chatthew!']:
        if message.content.lower().startswith(r):
            request = ' '.join(message.content.split()[1:])
    return request


def process_request(request):
    # TODO: make this a map?
    response = ''  # can't return None
    subcommand = request.lower()
    if subcommand == 'trivia':
        response = generate_question(subcommand)
    elif subcommand == 'pun' or subcommand == 'ant-fact' or subcommand == 'lacroix':
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
        await message.channel.send(process_request(request))


#client.run(os.getenv('TOKEN'))
client.run('ODcwMTA3MDg2ODc5NjE3MDI0.YQH8Xw.0h5Ou2hwd8I8A9GzEcJTXRH6_FI')
