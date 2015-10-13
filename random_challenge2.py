"""some code by user aperezalbela http://dpaste.com/0957WEF

To use this script, go to https://www.codeeval.com/open_challenges/ and save
the html file there to 'codeeval_open_challenges.html' (you must be logged in).
Now, in the same directory that you saved that HTML file, run this script with
a number corresponding to which level of eval you are looking to attempt. For
example 'python random_challenge2.py 1'. This will return a random challenge
from the "easy" category. The valid choices are as follows:

1 - easy
2 - moderate
3 - hard
4 - any

"""

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


def solved_challenge(challenge_level, unsolved_list):
    for item in (challenge_level):
        if item[6] != 'Solved':
            unsolved_list.append(item)


def randomize(random_lvl):
    """Pick a random challenge from a list of challenges and return it.

    args:
        random_lvl: which level of difficulty the user wants to select from
            1 - easy
            2 - moderate
            3 - hard
            4 - any

    returns:
        a challenge
    """
    if random_lvl == '1':
        return random.choice(UNSOLVED_EASY)
    elif random_lvl == '2':
        return random.choice(UNSOLVED_MOD)
    elif random_lvl == '3':
        return random.choice(UNSOLVED_HARD)
    elif random_lvl == '4':
        # make one giant list of everything
        UNSOLVED_ALL.extend(UNSOLVED_EASY)
        UNSOLVED_ALL.extend(UNSOLVED_MOD)
        UNSOLVED_ALL.extend(UNSOLVED_HARD)

        return random.choice(UNSOLVED_ALL)


if __name__ == '__main__':
    solved_challenge(to_extract['easy_challanges'], UNSOLVED_EASY)
    solved_challenge(to_extract['moderate_challanges'], UNSOLVED_MOD)
    solved_challenge(to_extract['hard_challanges'], UNSOLVED_HARD)

    print(randomize(argv[1]))

#print to_extract['easy_challanges']
#print to_extract['moderate_challanges']
#print to_extract['hard_challanges']
