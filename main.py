class Quiz:
    """퀴즈 한 문제를 나타내는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number):
        """문제와 선택지를 화면에 보여준다"""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False"""
        return user_answer == self.answer


# ----- 테스트용 코드 (나중에 바꿀 거예요) -----
test_quiz = Quiz("1 + 1은?", ["1", "2", "3", "4"], 2)
test_quiz.display(1)
print(test_quiz.is_correct(2))
print(test_quiz.is_correct(3))