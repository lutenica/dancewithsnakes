#!/usr/bin/python3
"""
    A simple game for Open Trivia Database questions.
    You will be asked the number of questions you want (Max is 50)
    Then you will be asked which category, you need to select one from
    the printed options.
    You need to seelct a difficulty from easy medium and hard.
    The boolean type of answer means true or false. This is case insensitive
    and t/f T/F also work.
    Multiple means anything can be an answer but is case sensitive. Note that
    this relies on opentdb.
"""
import sys
import requests
import quiz_game_classes

# Get some constants
question_bank = []
URL = "https://opentdb.com/api.php"
# Category handiling
CAT_URL = "https://opentdb.com/api_category.php"
cat_resp = requests.get(CAT_URL, timeout=10)
cat_resp.raise_for_status()
cat_dict = cat_resp.json()
cat_list = cat_dict["trivia_categories"]
cat_n_l = [ category["name"] for category in cat_list ]
cat_n_l = ",\n".join(cat_n_l)
cat_n_l += ",\nAny"

# Gather user input
n_questions = input("How many questions would you like?\n")
cat = input(f"Choose from the following categories:\n{cat_n_l}\n")
diff = input("Select difficulty: easy/medium/hard\n")
a_type = input("Answer type: boolean(true or false) or multiple)?\n")
c_id = None

# Get category id
for category in cat_list:

    if cat == category["name"]:
        c_id = category["id"]

params = {
    "amount": n_questions,
    "difficulty": diff,
    "type": a_type,
}

if c_id:
    params["category"] = c_id

r = requests.get(url=URL, params=params, timeout=10)
r.raise_for_status()
r_j = r.json()

if r_j["response_code"] == 1:
    sys.exit("There are not enough questions of the requested type available.")

question_data = r_j['results']

question_bank = [
    quiz_game_classes.Question(
        i['question'],
        i['correct_answer'],
        i['incorrect_answers']
    )
    for i in question_data
]

quiz = quiz_game_classes.QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()
