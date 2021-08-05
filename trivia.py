import random

from questions import questions

trivia_map = {
    'trivia': questions
}


def generate_question(subcommand):
    question = random.choice(trivia_map[subcommand])
    return random.choice(trivia_map[subcommand])


class Trivia():
    def __init__(self):
        pass
