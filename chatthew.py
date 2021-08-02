import discord
import os
import re

#from datetime import datetime
#from threading import Timer

client = discord.Client()

# def set_reminder(content):
#     time = ''
#     if content[0] == 'daily':
#         time = content[1:]
#     return f'Setting reminder at {time}'

class ChatthewResponse():
    def __init__(self):
        pass

def parse_request(message):
    pass

def is_chattew_request(message):
    # '(optional)greeting' chatthew (request)
    chatthew_rgx = '^(.*)*(chatthew)(.*)$' #todo: something more clever without going into NLP
    if re.match('', message.content, re.IGNORECASE):
        return True
    return False

def process_request(message):
    response = ChatthewResponse()
    request = parse_message(message)
    
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print('Alright alright alright... Chatthew in the house')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if is_chatthew_request(message):
        process_request(message)
 
client.run('TODO_TOKEN_HERE')
