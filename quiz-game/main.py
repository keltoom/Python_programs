from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you've completed the game!")
print(f"you're final score is {quiz.score}/{len(question_bank)}")
