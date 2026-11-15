# 🍦 굿플레이스 철학 퀴즈

Python으로 만든 콘솔 퀴즈 게임입니다.
미국 드라마 **굿플레이스(The Good Place)** 에 등장하는 윤리학·철학 이론을 장면과 함께 맞히는 퀴즈를 풀고, 직접 새 퀴즈를 추가할 수 있습니다.

## 1. 프로젝트 개요

- 터미널에서 메뉴 번호를 골라 **퀴즈 풀기 / 퀴즈 추가 / 퀴즈 목록 / 점수 확인 / 종료**를 할 수 있습니다.
- 퀴즈와 최고 점수는 `state.json` 파일에 저장되어, 프로그램을 껐다 켜도 그대로 유지됩니다.
- `Quiz`, `QuizGame` 두 개의 클래스로 역할을 나누어 만들었습니다.
- 외부 라이브러리 없이 Python 표준 기능만 사용했습니다.

## 2. 퀴즈 주제와 선정 이유

**주제: 굿플레이스 속 철학 이론**

굿플레이스는 제가 가장 좋아하는 드라마입니다. 마음이 답답할 때마다 다시 보며 20번 정도 시청했습니다.
이 드라마는 윤리학 교수 치디가 친구들에게 철학을 가르치는 이야기라서, 장면마다 실제 철학 이론이 등장합니다.
그래서 "이 장면에 나온 철학은 누구의 어떤 이론일까?"를 맞히는 퀴즈를 만들었습니다.

| 번호 | 장면 | 정답 |
|---|---|---|
| 1 | 시즌2 5화, 마이클이 만든 진짜 기차 | 필리파 풋 - 트롤리 딜레마 |
| 2 | 시즌2 1화, 중간지대에서 깨달은 반복되는 리부트 | 프리드리히 니체 - 영원회귀 |
| 3 | 시즌1 6화, 'What We Owe to Each Other' | T.M. 스캔런 - 계약주의 |
| 4 | 시즌3 8화, 더그 포셋의 삶 | 제러미 벤담 - 공리주의 |
| 5 | 시즌3 4화, 치디의 수업 | 프리드리히 니체 - 허무주의 |

## 3. 실행 방법

**필요 환경:** Python 3.10 이상 (외부 라이브러리 설치 필요 없음)

```bash
# 1. 저장소 복제
git clone https://github.com/yeoreumjoo/codyssey-python-quiz.git
cd codyssey-python-quiz

# 2. 실행 (Windows)
python main.py

# 2. 실행 (macOS / Linux)
python3 main.py
```

## 4. 기능 목록

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 퀴즈 풀기 | 저장된 퀴즈를 차례로 출제하고 정답/오답을 알려 줍니다. 다 풀면 점수(100점 만점)를 보여 주고, 최고 점수보다 높으면 갱신해 저장합니다. |
| 2 | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호를 입력해 새 퀴즈를 등록하고 바로 저장합니다. |
| 3 | 퀴즈 목록 | 등록된 퀴즈의 문제를 번호와 함께 보여 줍니다. |
| 4 | 점수 확인 | 최고 점수를 보여 줍니다. 아직 풀지 않았으면 안내 메시지를 보여 줍니다. |
| 5 | 종료 | 데이터를 저장하고 프로그램을 끝냅니다. |

**입력 / 예외 처리**
- 입력 앞뒤 공백은 지우고 처리합니다. (예: ` 1 ` → `1`)
- 숫자가 아닌 입력(`abc`), 범위 밖 숫자(메뉴 `9`, 정답 `0`), 빈 입력(그냥 Enter)은 안내 후 다시 입력받습니다.
- `Ctrl+C` 또는 입력이 끊겨도(EOF) 오류로 꺼지지 않고, 저장 후 안전하게 종료합니다.
- `state.json`이 없으면 기본 퀴즈로 시작하고, 파일이 손상되었으면 안내 후 기본 퀴즈로 복구합니다.

## 5. 파일 구조

```
codyssey-python-quiz/
├── main.py              # 프로그램 전체 코드 (Quiz, QuizGame 클래스)
├── state.json           # 퀴즈 목록과 최고 점수 저장 파일
├── README.md            # 프로젝트 설명서 (이 문서)
├── .gitignore           # Git에 올리지 않을 파일 목록 (Python 템플릿)
└── docs/
    └── screenshots/     # 실행 화면 캡처
```

**클래스 구조 (`main.py`)**

| 클래스 | 역할 | 주요 메서드 |
|---|---|---|
| `Quiz` | 퀴즈 한 문제 | `display()` 문제 출력, `is_correct()` 정답 확인, `to_dict()` 저장용 변환 |
| `QuizGame` | 게임 전체 관리 | `run()` 메뉴 반복, `play_quiz()`, `add_quiz()`, `show_list()`, `show_score()`, `load_data()`, `save_data()`, `get_number()` / `get_text()` 입력 검증 |

## 6. 데이터 파일 설명 (`state.json`)

- **경로:** 프로젝트 루트의 `state.json` (`main.py`와 같은 폴더)
- **역할:** 퀴즈 목록과 최고 점수를 저장해, 프로그램을 다시 실행해도 데이터가 유지되게 합니다.
- **인코딩:** UTF-8 (한글이 그대로 저장됩니다)
- **언제 저장되나요?** 퀴즈 추가, 최고 점수 갱신, 종료(메뉴 5 / Ctrl+C) 때

**스키마 (데이터 구조)**

```json
{
    "quizzes": [
        {
            "question": "문제 내용",
            "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
            "answer": 1
        }
    ],
    "best_score": 83
}
```

| 키 | 자료형 | 설명 |
|---|---|---|
| `quizzes` | list | 퀴즈 목록 |
| `quizzes[].question` | str | 문제 |
| `quizzes[].choices` | list (str 4개) | 선택지 4개 |
| `quizzes[].answer` | int (1~4) | 정답 번호 |
| `best_score` | int 또는 null | 최고 점수 (100점 만점). 아직 안 풀었으면 `null` |

## 7. 실행 화면

| 메뉴 | 퀴즈 풀기 |
|---|---|
| ![메뉴](docs/screenshots/10_menu.png) | ![퀴즈 풀기](docs/screenshots/04_play.png) |

| 퀴즈 추가 | 퀴즈 목록 |
|---|---|
| ![퀴즈 추가](docs/screenshots/06_add_quiz.png) | ![퀴즈 목록](docs/screenshots/07_list.png) |

| 점수 확인 | 재실행 후 데이터 유지 |
|---|---|
| ![점수 확인](docs/screenshots/08_score.png) | ![재실행](docs/screenshots/09_restart_load.png) |

| 잘못된 입력 처리 |
|---|
| ![잘못된 입력](docs/screenshots/11_input_error.png) |

## 8. 개발 환경

| Python 버전 | Git 설정 | VS Code |
|---|---|---|
| ![Python](docs/screenshots/01_env_python_version.png) | ![Git](docs/screenshots/02_env_git_config.png) | ![VS Code](docs/screenshots/03_env_vscode.png) |

## 9. Git 작업 기록

- 기능 단위로 커밋했습니다. (`Feat:` 기능, `Docs:` 문서)
- 퀴즈 풀기 기능은 `feature/quiz-play` 브랜치에서 개발한 뒤 `main`에 병합했습니다.
- 사용한 Git 명령어: `init`, `add`, `commit`, `push`, `pull`, `checkout`, `merge`, `clone`
- clone·pull 실습: 다른 폴더에 clone해서 수정·push한 뒤, 원래 폴더에서 pull로 받아왔습니다.

| Git 커밋 기록 (`git log --oneline --graph`) | clone·push·pull 실습 |
|---|---|
| ![Git 기록](docs/screenshots/12_git_log_graph.png) | ![clone pull](docs/screenshots/13_clone_pull.png) |