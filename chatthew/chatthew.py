import discord
import os, sys
import re
import random
from .fact import generate_fact
from .trivia import generate_question, check_answer

# stores info if someone is in the middle of something
user_map = {}

class Chatthew(discord.Client):
    def __init__(self):
        try:
            super().__init__()
            sys.stdout.write("Alright alright alright... Chatthew in the house\n")
        except:
            pass
    
    # this can be more clever
    def is_chatthew_request(self, message):
        request = None
        for r in ['chatthew,', 'chatthew!']:
            if message.content.lower().startswith(r):
                request = ' '.join(message.content.split()[1:])
        return request

    def process_request(self, request, id):
        # TODO: make this a map?
        response = ''  # can't return None
        subcommand = request.lower()
        if subcommand == 'trivia':
            response, question_id = generate_question(subcommand)
            user_map[id] = {
                'question_id': question_id
            }
        elif subcommand in ['pun', 'ant-fact', 'lacroix']:
            response = generate_fact(subcommand)
        elif subcommand == 'simp':
            response = ':pleading_face: :point_right: :point_left: is there anything my Queen needs'
        return response

    
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))
        print('Alright alright alright... Chatthew in the house')

        
    async def on_message(self, message):
        if message.author == self.user:
            return
        request = self.is_chatthew_request(message)
        if request:
            req = request.split()
            if message.author.id in user_map:
                answer = check_answer(req[0], user_map[message.author.id]['question_id'])
                user_map.pop(message.author.id)
                await message.channel.send(answer)
            elif req[0].lower() == 'simp':
                await message.channel.send( ':pleading_face: :point_right: :point_left: is there anything my Queen needs')
            elif req[0].lower() == 'meme':
                meme = random.choice(os.listdir("img/memes"))
                await message.channel.send(file=discord.File(open(f'img/memes/{meme}','rb')))
            elif req[0].lower() == 'poll':
                channel = ' '.join(req[1:])
                await message.channel.send(f'[NOT FUNCTIONAL] Type your poll question for {channel}')
                # TODO: get user response
                # await message.channel.send('set poll options') # todo: separate by \n, autoassign emojis, custom emoji choice
                # for e in ['👍', '👎']:
                #     await poll.add_reaction(e)
        else:
            await message.channel.send(self.process_request(request, message.author.id))


def main():
    try:
        c = Chatthew()
        c.run(os.getenv('TOKEN'))
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    main()
