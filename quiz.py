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
import requests
import quiz_game_classes

# Get some constants
question_bank = []
URL = "https://opentdb.com/api.php?"
# Category handiling
C_URL = "https://opentdb.com/api_category.php"
c_r = requests.get(C_URL, timeout=10)
c_r_j = c_r.json()
cat_list = c_r_j["trivia_categories"]
# Category name list
cat_n_l = ["Any"]

for category in cat_list:
    new_cat = category["name"]
    cat_n_l.append(new_cat)

# Gather user input
n_questions = input("How many questions would you like?\n")
cat = input(f"Choose from the following categories:\n{cat_n_l}\n")
diff = input("Select difficulty, easy/medium/hard\n")
a_type = input("Answer type (boolean or multiple)?\n")
c_id = ''

for category in cat_list:
    if cat == category["name"]:
        c_id = category["id"]

if not c_id:
    u = f"{URL}amount={n_questions}&difficulty={diff}&type={a_type}"
else:
    u = f"{URL}amount={n_questions}&category={c_id}&difficulty={diff}&type={a_type}"
print(u)
r = requests.get(u, timeout=10)
r_j = r.json()
print(r_j)
question_data = r_j['results']

for i in question_data:
    q = quiz_game_classes.Question(i['question'], i['correct_answer'])
    question_bank.append(q)

quiz = quiz_game_classes.QuizBrain(question_bank)

while quiz.still_has_questions():

    if a_type == "boolean":
        print("True or false:")

    quiz.next_question()
