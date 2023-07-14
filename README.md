# autogpt
AutoGPT 조사

# 1. AutoGPT란?
AutoGPT란 GPT-4를 사용하는 python application으로, ChatGPT와 같이 사용자의 입력에 따른 대답을 생성한다. 이때, 자율적으로(Autonomous) 사용자의 임무에 대한 중간 보조 업무를 수행한다는 점에서 ChatGPT와 차이점을 가진다. 이러한 AutoGPT는 ChatGPT와 같은 언어모델 에이전트 여러 개로 구성되며, 각 에이전트들은 임무를 수행하기 위한 보조 업무를 생성하고 수행한다. 그 결과로, ChatGPT보다 훨씬 정확하고 많은 작업을 수행할 수 있다. 

# 2. AutoGPT 설치법
AutoGPT는 Git과 VSC를 이용하여 설치할 수 있으며, OpenAi 계정이 있다면 API 키를 생성하여 설치하면 된다.

1) Python과 Git 설치 (필수)
   - AutoGPT 버전에 따라 요구되는 버전이 달라질 수 있음. (현재는 python 3.8, 혹시 모르니 가장 최신버전을 다운로드 하자.)
     
2) git을 이용해 Autogpt 설치
   - git 설치 후 cmd 실행 > 원하는 경로로 이동 > git clone https://github.com/Significant-Gravitas/Auto-GPT.git 실행
   - cd Auto-GPT를 실행해 Auto-GPT를 설치한 디렉토리로 이동 > pip install -r requirements.txt 실행하여 필요한 파일 다운로드
   - 실행 후 cmd에 code 실행시 vsc가 자동으로 열림. vsc를 이용해 필요한 API 수정 등의 작업을 하는 것을 추천.
     
3) Visual Studio Code 설치 (필수는 아님, 강력추천.)
   - 추후에 제공된 코드를 사용자에 맞게 수정하는 데 필요, VSC를 제외한 다른 앱을 이용할 수도 있다. 
   - https://code.visualstudio.com/download 에서 설치 가능.
     
4) Open AI에서 API 생성(필수)
   - https://platform.openai.com/ 에 로그인 후 프로필 클릭 > view API Keys > create new secret key > 이름입력(선택) API 생성
   - 이때, 한번 생성된 API는 다시 볼 수 없으므로 저장해두어야 함.
   - API 생성을 위해 카드 정보를 등록해두어야 함.
     
5) pinecone에서 API KEY 생성 (필수는 아니나, AI가 장단기 기억을 오래 유지하기 위한 외부 프로그램)
   - https://www.pinecone.io/ 에 접속, 로그인 후 API KEY, environment 정보값 저장
     
6) Google Custom search API 생성 (역시 필수는 아니나, AI가 google 검색을 사용하기 위한 장치)
   - 구글 클라우드에 회원가입 후 로그인 > 새 프로젝트 만들기(이름자유)
   - 메뉴 > API 및 서비스 > 라이브러리 > Custom search API 선택 > 사용 클릭
   - 사용 인증 정보 > 사용인 정보 만들기 > API 키 복사
   - https://programmablesearchengine.google.com/controlpanel/all 들어가서 추가 > 이름자유, 전체 웹 검색 체크 > 만들기 > 맞춤 설정 > 검색엔진 ID 확인
     
7) API 입력
   - 다운로드 된 .env.template 파일에서 다음과 같이 실행 : 파일명을 .env 형태로 수정 > OPEN_API_KEY= 에 본인의 API Key 입력
   - 또한, 해당 .env 파일에서 다음을 수행 : GOOGLE_API_KEY= 와 CUSTOM_ENGINE_ID= 에 본인의 key와 id 입력
   - 또한, 해당 .env 파일에서 다음을 수행 : PINECONE_API_KEY= 와 PINECONE_ENV= 에 본인의 key와 env 값 입력
     
8) Auto-GPT 실행
   - cmd 실행 > AUTO-GPT 디렉토리에서 python -m autogpt 실행
   - 또는, Auto-GPT 폴더에서 run 배치파일 실행



**자주 발생하는 오류**
아래와 같이 ModuleNotFoundError가 계속해서 나타난다면, requirements.txt가 제대로 다운되었는지 확인한다.
1) ModuleNotFoundError: No module named 'dotenv'
해당 오류의 경우 크게 세 가지 방법으로 고칠 수 있다.
- 환경 변수에 존재하는 여러 개의 Python PATH 삭제
- DotEnv Module 다운로드
- Python 재설치
https://droidwin.com/autogpt-modulenotfounderror-no-module-named-dotenv-fix/#google_vignette 참고.
