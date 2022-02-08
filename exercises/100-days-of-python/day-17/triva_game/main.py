from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

QUESTION_BANK = []

for questions in question_data:
    QUESTION_BANK.append(
        Question(questions["question"], questions["correct_answer"])
    )

quiz = QuizBrain(QUESTION_BANK)

while quiz.still_has_questions():
    quiz.next_question()
print(
    "You've completed the quiz. Your final score"
    f" was: {quiz.user_score}/{len(quiz.questions_list)}"
)
