import json
from pathlib import Path

# 데이터 파일 위치: main.py와 같은 폴더(프로젝트 루트)의 state.json
STATE_FILE = Path(__file__).parent / "state.json"


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

    def to_dict(self):
        """JSON으로 저장할 수 있게 딕셔너리로 바꿔 준다"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


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


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []        # 퀴즈 목록 (list)
        self.best_score = None   # 최고 점수 (아직 안 풀었으면 None)
        self.load_data()         # 시작할 때 state.json에서 불러오기

    def load_data(self):
        """state.json에서 퀴즈 목록과 최고 점수를 불러온다"""
        if not STATE_FILE.exists():
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.reset_to_default()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = []
            for item in data["quizzes"]:
                quiz = Quiz(item["question"], item["choices"], item["answer"])
                quizzes.append(quiz)

            self.quizzes = quizzes
            self.best_score = data.get("best_score")
            print(f"📂 저장된 데이터를 불러왔습니다. "
                  f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score_text()})")
        except (json.JSONDecodeError, KeyError, TypeError, OSError):
            print("⚠️ state.json 파일이 손상되어 기본 퀴즈 데이터로 복구합니다.")
            self.reset_to_default()

    def reset_to_default(self):
        """기본 퀴즈로 되돌리고 바로 저장한다"""
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.save_data()

    def save_data(self):
        """퀴즈 목록과 최고 점수를 state.json에 저장한다"""
        quiz_list = []
        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("⚠️ 데이터를 저장하지 못했습니다.")

    def best_score_text(self):
        """최고 점수를 화면에 보여줄 글자로 바꿔 준다"""
        if self.best_score is None:
            return "아직 없음"
        return f"{self.best_score}점"

    def get_number(self, prompt, min_value, max_value):
        """min_value~max_value 사이의 숫자를 받을 때까지 계속 묻는다"""
        while True:
            text = input(prompt).strip()

            if text == "":
                print(f"⚠️ 입력이 비어 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            try:
                number = int(text)
            except ValueError:
                print(f"⚠️ 숫자가 아닙니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            if number < min_value or number > max_value:
                print(f"⚠️ 범위를 벗어났습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            return number

    def play_quiz(self):
        """저장된 퀴즈를 차례로 출제하고 결과를 보여준다"""
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print()
        print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")

        for i, quiz in enumerate(self.quizzes, start=1):
            print()
            print("-" * 40)
            quiz.display(i)
            print()
            user_answer = self.get_number("정답 입력: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                right_choice = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 '{right_choice}'입니다.")

        score = round(correct_count / total * 100)
        print()
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_data()
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")
        print("=" * 40)
    def get_text(self, prompt):
        """빈칸이 아닌 글자를 받을 때까지 계속 묻는다"""
        while True:
            text = input(prompt).strip()

            if text == "":
                print("⚠️ 내용이 비어 있습니다. 다시 입력하세요.")
                continue

            return text

    def add_quiz(self):
        """새 퀴즈를 입력받아 목록에 추가하고 저장한다"""
        print()
        print("📌 새로운 퀴즈를 추가합니다.")
        print()

        question = self.get_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = self.get_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = self.get_number("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_data()

        print()
        print(f"✅ 퀴즈가 추가되었습니다! (현재 퀴즈 {len(self.quizzes)}개)")

    def show_list(self):
        """저장된 퀴즈의 문제 목록을 보여준다"""
        if len(self.quizzes) == 0:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print()
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print()
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)
    def show_score(self):
        """최고 점수를 보여준다"""
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어 보세요!")
            return

        print()
        print(f"🏆 최고 점수: {self.best_score}점")
    def show_menu(self):
        """메인 메뉴를 화면에 보여준다"""
        print()
        print("=" * 40)
        print("       🍦 굿플레이스 철학 퀴즈 🍦")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self):
        """메뉴를 보여주고, 종료를 고를 때까지 반복한다"""
        while True:
            self.show_menu()
            choice = self.get_number("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save_data()
                print("💾 저장 완료! 👋 게임을 종료합니다. 다음에 또 만나요!")
                break


def main():
    """프로그램 시작점"""
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print()
        game.save_data()
        print("⚠️ 입력이 중단되어 저장 후 프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    main()