# Assignment 2 — 객체지향 프로그래밍 심화

## 📋 과제 개요

이 과제는 6개의 문제로 구성되어 있으며, 각 문제는 파이썬의 객체지향 프로그래밍 핵심 개념을 다룹니다.

### 문제 구성

- **Problem 1**: `Accumulator` — 상태를 가진 카운터 (Property 패턴)
- **Problem 2**: `textops` — 텍스트 전처리 패키지
- **Problem 3**: `tokenstats` — 토큰 통계 모듈
- **Problem 4**: `dsops` — 데이터셋 유틸리티
- **Problem 5**: `cachekit` — 메모리 캐시
- **Problem 6**: `지표 계산기` — 상속과 추상화

<<<<<<< HEAD
=======
**⚠️ 중요**: 문제 spec에서 명시가 된 경우를 제외하고, 라이브러리를 사용하지 말고 직접 구현해주세요.

>>>>>>> upstream/main
## 🚀 시작하기

### 1. 저장소 준비

#### 첫 번째 과제인 경우 (Fork)
```bash
# GitHub에서 organization 저장소를 본인 계정으로 fork
# 웹 브라우저에서 https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2 접속
# 우측 상단의 "Fork" 버튼 클릭

# fork한 저장소를 로컬로 클론
git clone https://github.com/YOUR_USERNAME/HUFS-LAI-OOP-2025-2.git
cd HUFS-LAI-OOP-2025-2
```

<<<<<<< HEAD
#### 이미 fork한 경우 (동기화)
=======
#### 이미 fork했고, 웹에서 sync를 하고 싶은 경우
- https://github.com/YOUR_USERNAME/HUFS-LAI-OOP-2025-2 에 접속해서 `Sync fork` 버튼 클릭 후 `Update branch` 선택.

#### 이미 fork했지만 터미널에서 작업하고 싶은 경우
>>>>>>> upstream/main
```bash
# 기존 로컬 저장소로 이동
cd HUFS-LAI-OOP-2025-2

# upstream 원격 저장소 설정 (최초 1회만)
git remote add upstream https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2.git

# 최신 변경사항 가져오기
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

<<<<<<< HEAD
### 2. 과제 파일 복사

```bash
=======
- 추가 설명 (2025-09-24 업데이트): 이 때 `upstream` 은 교수 repository (https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2) 이고, `origin` 은 여러분 학생 repository (https://github.com/YOUR_USERNAME/HUFS-LAI-OOP-2025-2) 입니다.

### 2. 과제 파일 복사

`assignments/` 디렉토리는 첫 화면에서 안내하듯이 과제 공지 및 템플릿 제공을 목적으로 하기 때문에, `assignments/` 에서는 코드를 수정하시면 안 됩니다.
이번 과제 제출을 위한 모든 파일 및 변경 사항은 `submissions/` 아래에서만 이루어져야 합니다.
아래는 명령어들은 터미널(cmd, git bash 등)을 통해 `submissions/` 아래에 `assignments/` 에서 제공하는 템플릿을 옮기는 방법입니다.
터미널이 익숙하지 않다면 직접 윈도우 폴더를 열어서 복사 후 작업해도 상관없습니다. 

```bash
# submissions 디렉토리 생성
mkdir submissions

# submissions 디렉토리 아래 본인 학번으로 디렉토리 생성
mkdir submissions/YOUR_STUDENT_ID

>>>>>>> upstream/main
# 현재 디렉토리에서 과제 파일들을 자신의 제출 디렉토리로 복사
cp -r assignments/assignment2 submissions/YOUR_STUDENT_ID/

# 예시: 학번이 202501234인 경우
cp -r assignments/assignment2 submissions/202501234/

# 복사가 제대로 되었는지 확인
ls submissions/YOUR_STUDENT_ID/assignment2
# 결과: problem1 problem2 problem3 problem4 problem5 problem6
```

### 3. 작업 디렉토리로 이동

```bash
cd submissions/YOUR_STUDENT_ID/assignment2
```

## 📁 제출 디렉토리 구조

제출할 때 다음과 같은 디렉토리 구조를 유지해야 합니다:

> **💡 팁**: `find submissions/YOUR_STUDENT_ID/assignment2 -type f | sort` 명령어로 실제 파일 구조를 확인할 수 있습니다.

```
submissions/YOUR_STUDENT_ID/assignment2/
├── problem1/
│   ├── README.md
│   └── main.py
├── problem2/
│   ├── README.md
│   └── textops/
│       ├── __init__.py
│       ├── main.py
│       ├── clean/
│       │   ├── __init__.py
│       │   └── filters.py
│       └── tokenize/
│           ├── __init__.py
│           └── word.py
├── problem3/
│   ├── README.md
│   └── main.py
├── problem4/
│   ├── README.md
│   └── dsops/
│       ├── __init__.py
│       ├── main.py
│       ├── split/
│       │   ├── __init__.py
│       │   └── train_test.py
│       └── stats/
│           ├── __init__.py
│           └── labels.py
├── problem5/
│   ├── README.md
│   └── cachekit/
│       ├── __init__.py
│       └── main.py
├── problem6/
│   ├── README.md
│   └── main.py
└── grader.py
```

## 🔧 개발 및 테스트

### 개별 문제 테스트

```bash
<<<<<<< HEAD
=======
# 현재 위치 확인 (xxx/HUFS-LAI-OOP-2025-2/submissions/YOUR_STUDENT_ID/assignment2 로 표시되어야 함.)
pwd

>>>>>>> upstream/main
# Problem 1 테스트
cd problem1 && python main.py

# Problem 2 테스트
<<<<<<< HEAD
cd problem2/textops && python main.py
=======
cd problem2 && python -m textops.main
>>>>>>> upstream/main

# Problem 3 테스트
cd problem3 && python main.py

# Problem 4 테스트
<<<<<<< HEAD
cd problem4/dsops && python main.py

# Problem 5 테스트
cd problem5/cachekit && python main.py
=======
cd problem4 && python -m dsops.main

# Problem 5 테스트
cd problem5 && python -m cachekit.main
>>>>>>> upstream/main

# Problem 6 테스트
cd problem6 && python main.py
```

## 📤 제출 방법

### 1. Git 상태 확인

```bash
# 현재 변경사항 확인
git status

# 변경된 파일들 확인
git diff --name-only
```

### 2. 파일 추가 및 커밋

```bash
# 새로 생성한 모든 파일 추가
git add submissions/YOUR_STUDENT_ID/

# 또는 개별 파일 추가
git add submissions/YOUR_STUDENT_ID/assignment2/problem1/main.py
git add submissions/YOUR_STUDENT_ID/assignment2/problem2/textops/

# 커밋
git commit -m "Add problem1/main.py"
```

## ✅ 체크리스트

제출 전에 다음 사항들을 확인하세요:

### 구현 사항

- [ ] Problem 1 구현 완료
- [ ] Problem 2 구현 완료 (패키지 구조 포함)
- [ ] Problem 3 구현 완료
- [ ] Problem 4 구현 완료 (dsops 패키지)
- [ ] Problem 5 구현 완료 (cachekit 패키지)
- [ ] Problem 6 구현 완료 (지표 계산기)
- [ ] 디렉토리 구조가 위 명세와 일치
- [ ] 모든 Python 파일에 문법 오류 없음

### PR 관련

- [ ] PR 제목이 `2nd Assignment by {학번} (이름)` 형식
- [ ] 모든 변경사항이 올바른 디렉토리에 위치
- [ ] 불필요한 파일들 (.pyc, __pycache__ 등) 제외

## 🆘 문제 해결

### 자주 발생하는 오류

1. **Import Error**: 패키지 구조가 올바른지 확인하고 `__init__.py` 파일 확인
2. **Git 충돌**: `git status`로 상태 확인 후 충돌 해결

### 도움말

- 각 문제별 상세 설명: 해당 문제 디렉토리의 `README.md` 참조
- 코딩 스타일: 기존 템플릿 코드의 패턴 따라하기
- 테스트 방법: 각 파일의 `if __name__ == "__main__"` 블록 활용

## 💡 유용한 Git 명령어

### 파일 상태 확인

```bash
# 현재 브랜치와 변경사항 확인
git status

# 현재 브랜치만 확인
git branch

# 마지막 커밋 이후 변경된 파일 목록
git diff --name-only HEAD

# 특정 파일의 변경사항만 보기
git diff submissions/YOUR_STUDENT_ID/assignment2/problem1/main.py

# 스테이징된 파일들 확인
git diff --cached --name-only
```

### 디렉토리 구조 확인

```bash
# 제출 디렉토리 구조 확인 (tree 명령어가 있는 경우)
tree submissions/YOUR_STUDENT_ID/assignment2

# tree가 없는 경우 find 사용
find submissions/YOUR_STUDENT_ID/assignment2 -type f | sort

# Python 파일들만 확인
find submissions/YOUR_STUDENT_ID/assignment2 -name "*.py" | sort

# 디렉토리 구조만 확인
find submissions/YOUR_STUDENT_ID/assignment2 -type d | sort
```

### 제출 준비

```bash
# 제출할 파일들만 선별적으로 추가
git add submissions/YOUR_STUDENT_ID/assignment2/

# 현재 추가된 파일들 확인
git diff --cached --name-only

# 커밋 전 최종 확인
git status

# 브랜치 생성과 동시에 체크아웃
git checkout -b assignment2-YOUR_STUDENT_ID

# 원격 저장소에 푸시 (본인의 fork로)
git push -u origin assignment2-YOUR_STUDENT_ID

# GitHub 웹에서 PR 생성
# 1. https://github.com/YOUR_USERNAME/HUFS-LAI-OOP-2025-2 접속
# 2. "Compare & pull request" 버튼 클릭
# 3. base repository를 HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2로, base를 main으로 설정
# 4. PR 제목: "2nd Assignment by YOUR_STUDENT_ID (Your Full Name)"
```

### 문제 해결

```bash
# 실수로 추가한 파일 제거 (아직 커밋 안한 경우)
git reset HEAD submissions/YOUR_STUDENT_ID/assignment2/unwanted_file.py

# 마지막 커밋 메시지 수정
git commit --amend -m "새로운 커밋 메시지"

# 원격 브랜치와 로컬 브랜치 상태 확인
git branch -va

# 최신 main 브랜치 내용 가져오기
git checkout main
git pull origin main
```

---

**주의사항**:
- 반드시 organization 저장소를 fork한 후 작업하세요
- 과제 시작 전 upstream과 동기화하여 최신 버전을 사용하세요
- 반드시 지정된 디렉토리 구조를 따라야 자동 검증이 통과됩니다
- PR은 본인의 fork에서 organization 저장소의 main 브랜치로 생성하세요
- PR 제목 형식을 정확히 지켜주세요: `2nd Assignment by {학번} (이름)`