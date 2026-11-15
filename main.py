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


def create_default_quizzes():
    """굿플레이스 속 철학 퀴즈 5개를 만들어 리스트로 돌려준다"""
    return [
        Quiz(
            "시즌2 5화, 마이클이 진짜 기차를 만들어 치디에게 "
            "'다섯 명을 살릴까, 한 명을 살릴까' 고르게 한 사고실험은?",
            ["필리파 풋 - 트롤리 딜레마", "플라톤 - 동굴의 비유",
             "임마누엘 칸트 - 정언명령", "제러미 벤담 - 공리주의"],
            1,
        ),
        Quiz(
            "시즌2 1화, 중간지대에 간 치디는 자신들이 이미 여러 번 이곳으로 도망치고 "
            "리부트됐다는 걸 깨닫는다. 같은 일이 끝없이 반복되는 이 상황과 닮은 이론은?",
            ["임마누엘 칸트 - 정언명령", "프리드리히 니체 - 허무주의",
             "프리드리히 니체 - 영원회귀", "T.M. 스캔런 - 계약주의"],
            3,
        ),
        Quiz(
            "시즌1 6화의 제목이자 치디가 엘리너에게 가르친 책 "
            "'What We Owe to Each Other'의 철학자와 이론은?",
            ["제러미 벤담 - 공리주의", "플라톤 - 동굴의 비유",
             "T.M. 스캔런 - 계약주의", "임마누엘 칸트 - 정언명령"],
            3,
        ),
        Quiz(
            "시즌3 8화, 마이클과 재닛이 찾아간 캐나다의 더그 포셋은 "
            "남들을 행복하게 하려고 자기 삶을 다 희생한다. 이 삶이 보여주는 이론은?",
            ["아리스토텔레스 - 덕 윤리", "T.M. 스캔런 - 계약주의",
             "프리드리히 니체 - 허무주의", "제러미 벤담 - 공리주의"],
            4,
        ),
        Quiz(
            "시즌3 4화, 사후세계의 진실을 알게 된 치디가 수업 시간에 "
            "'삶에는 아무 의미가 없다'고 말하며 빠져든 철학자와 이론은?",
            ["임마누엘 칸트 - 정언명령", "프리드리히 니체 - 허무주의",
             "제러미 벤담 - 공리주의", "필리파 풋 - 트롤리 딜레마"],
            2,
        ),
    ]


# ----- 테스트용 코드 (나중에 지울 거예요) -----
quizzes = create_default_quizzes()
print(f"기본 퀴즈 개수: {len(quizzes)}")
print()
for i, quiz in enumerate(quizzes, start=1):
    quiz.display(i)
    print()