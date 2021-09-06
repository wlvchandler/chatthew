import random
import string

from .questions import questions

trivia_map = {
    'trivia': questions
}


def get_question(question_dict):
    return question_dict['Q']


def get_options(question_dict):
    return ''.join(['{}. {}\n'.format(option, answer)
                    for (option, answer) in zip(string.ascii_lowercase, question_dict['O'])])


def get_answer(question_dict):
    return '{}'.format(question_dict['O'][question_dict['A']])


def generate_question(subcommand):
    index = random.choice(range(len(trivia_map[subcommand])))
    question = trivia_map[subcommand][index]
    return get_question(question) + '\n' + str(get_options(question)) + '\n', index


def check_answer(answer, question):
    return 'Correct Answer: {}'.format(get_answer(questions[question]))


class Trivia():
    def __init__(self):
        pass
