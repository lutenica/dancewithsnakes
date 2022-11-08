#!/usr/bin/python3

class Question:
    """
        Class for a question object
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class QuizBrain:
    """
        Class for the main part of the quizz
    """
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    def next_question(self):
        """
            Generates question
        """
        q_l = self.question_list
        q_n = self.question_number
        q_u = q_l[q_n].question
        a = q_l[q_n].answer

        p_a = input(f"{q_n + 1}: {q_u}\n")
        self.check_answer(p_a, a)
        self.question_number += 1

    def still_has_questions(self):
        """
            Checks if there are remaining questions, returns bool
        """
        q_n = self.question_number
        q_l = self.question_list
        return len(q_l) > q_n

    def check_answer(self, player_answer, correct_answer):
        """
            Checks provided answer and adjusts score
        """
        if player_answer in ["t","T","true","True","TRUE"]:
            player_answer = "True"

        elif player_answer in ["f","F","false","False","FALSE"]:
            player_answer = "False"

        if player_answer == correct_answer:
            self.score += 1
            print(f"Correct! Your score is {self.score}")
        else:
            self.score += 0
            print(f"Incorrect! Your score is {self.score}")
