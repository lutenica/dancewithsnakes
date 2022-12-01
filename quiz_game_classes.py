#!/usr/bin/python3
from random import shuffle
import html

class Question:
    """
        Class for a question object
    """
    def __init__(self, question, answer, incorrect_answers):
        self.question = question
        self.answer = answer
        self.incorrect_answers = incorrect_answers

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
        question = html.unescape(self.question_list[self.question_number].question)
        answer = self.question_list[self.question_number].answer
        incorrect_answers = self.question_list[self.question_number].incorrect_answers
        incorrect_answers.append(answer)
        shuffle(incorrect_answers)
        possibilities = ', '.join(incorrect_answers)
        player_answer = input(f"{self.question_number + 1}: {question}"
                              f" ({possibilities})\n")
        self.check_answer(player_answer, answer)
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
