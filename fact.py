import random

from puns import puns
from ant_facts import ant_facts

fact_map = {
    'pun': puns,
    'ant-fact': ant_facts
}


# get a random fact
# we can house any one-shot questions here
def generate_fact(type):
    return random.choice(fact_map[type])


class Fact():
    def __init__(self):
        pass
