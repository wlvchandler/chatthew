import random

from puns import puns
from ant_facts import ant_facts
from lacroix import lacroix

fact_map = {
    'pun': puns,
    'ant-fact': ant_facts,
    'lacroix': lacroix
}


# get a random fact
# we can house any one-shot questions here
def generate_fact(subcommand):
    return random.choice(fact_map[subcommand])


class Fact():
    def __init__(self):
        pass
