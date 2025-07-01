from question_model import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []
for qn in question_data:
    question_text = qn["text"]
    question_ans = qn["answer"]
    new_qn = Question(text=question_text,ans=question_ans)
    question_bank.append(new_qn)

quiz = quiz_brain(question_bank)
while quiz.still_have_qn():
    quiz.next_qn()
print("-----------------------------------------")
print("your quiz has been completed!!!")
print(f"your final score is : {quiz.score}/{len(question_bank)}")



