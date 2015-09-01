"""some code by user aperezalbela http://dpaste.com/0957WEF"""

import ast
import random
from itertools import chain
from sys import argv
from lxml import html


UNSOLVED_EASY = []
UNSOLVED_MOD = []
UNSOLVED_HARD = []
UNSOLVED_ALL = []

with open('codeeval_open_challenges.html', 'r') as html_file:
    html_text = html_file.read()
    tree = html.fromstring(html_text)
    to_extract = {
        'easy_challanges': None,
        'moderate_challanges': None,
        'hard_challanges': None
    }

    for challenge, content in to_extract.items():
        xpath = "//script[contains(text(),\"{}\")]/text()".format(challenge)
        scripts = tree.xpath(xpath)

        for script in scripts:
            temp_data = script.split(
                challenge + ' =')[1].split(';')[0].strip()
            to_extract[challenge] = ast.literal_eval(temp_data.strip())

unsolved_easy = []
unsolved_mod = []
unsolved_hard = []


def solved_challenge(challenge_level, unsolved_list):
    for item in (challenge_level):
        if item[6] != 'Solved':
            unsolved_list.append(item)


#print to_extract['easy_challanges']
#print to_extract['moderate_challanges']
#print to_extract['hard_challanges']
