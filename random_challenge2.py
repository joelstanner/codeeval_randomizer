"""some code by user aperezalbela"""

import ast
from lxml import html
from requests import Session

s = Session()

# response = s.get("https://codeeval.com/open_challenges/", cookies={'sessionid':'PASTE_YOUR_SESSION_ID_HERE'})

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
                'easy_challanges =')[1].split(';')[0].strip()
            to_extract[challenge] = ast.literal_eval(temp_data.strip())

#print to_extract['easy_challanges']
#print to_extract['moderate_challanges']
#print to_extract['hard_challanges']
