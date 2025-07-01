class quiz_brain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list=q_list

    def still_have_qn(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            False

    def next_qn(self):
        current_qn = self.question_list[self.question_number]
        self.question_number+=1
        user_ans = input(f"{self.question_number} :{current_qn.text} (True/False)").lower()
        self.check_ans(user_ans,current_qn.ans)


    def check_ans(self,userin,correctans):
        if userin.lower() == correctans.lower():
            print("you got it!")
            self.score+=1
            print(f"current score = {self.score}/{self.question_number}")
            print("\n")
        else:
            print("sorry wrong ans!")
            print(f"the correct ans is: {correctans}")
            print("try again")
            print(f"current score = {self.score}/{self.question_number}")
            print("\n")



