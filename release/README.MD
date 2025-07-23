## 실행 환경
- Windows
- Python3.13

## 패키지 설치
- pip install opencv-python==4.12.0.88 pymodbus==2.5.3

## 실행 방법
- start.bat(foreground) 또는 start-background.vbs(background) 파일로 실행할 수 있습니다.
  - TIME_ : 동영상 길이(초)
  - MOD_IP: 모드버스 서버 IP
  - MOD_PORT: 모드버스 서버 포트
  - MOD_WORD: 모드버스 트리거 받을 word
  - PATH_: 모듈 디렉터리의 절대 경로 (bat/vbs 파일 모듈 루트 디렉토리에서 실행 시 PATH_ 설정 생략 가능)
- 실행 후 트리거가 들어오면 최대 TIME_초의 웹캠 영상이 recordings 디렉토리에 "날짜_시간.mp4"로 저장됩니다.
- stop_all_python_process.bat로 Python 프로세스를 종료할 수 있습니다.(모든 파이썬 프로세스 종료)
- 트리거 테스트: ./test/trigger.bat 파일로 트리거를 발생시킬 수 있습니다.