About Mac
========

Keyboard shortcuts
--------
* spotlight : ctrl + space
* screen capture
** whole screen : command + shift + 3
** part of screen : command + shift + 4
** window : command + shift + 4, then space
** clipboard : command + shift + ctrl + (3 or 4), then space
* mission control : F3 or 세손가락 위로 밀기


Terminal app color theme
--------
* solarized
* peppermint

Homebrew
--------
* 맥용 패키지 관리자
* 설치 : /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
* 전용 디렉토리에 패키지 설치하고 /usr/local에 심볼릭 링크
* formula : 패키지
* brew
* brew -v : 버전 확인
* brew install <패키지명> : 패키지 설치
* brew search <패키지명> : 패키지 검색
* brew info <패키지명> : 패키지정보
* brew upgrade <패키지명> : 패키지 업그레이드
* brew ls : 설치한 패키지(formula)목록
* brew update : Homebrew 업데이트
* brew doctor : 시스템에 문제가 있는지 호가인
* brew outdated : 설치한 패키지 이후 버전이 나왔는지 확인
* brew cleanup : 패키지의 모든 과거버전을 제거함
* brew switch <패키지명> <버전> : 해당버전으로 변경(설치한 패키지가 여러 버전이 있을때)

Open Finder app in terminal
--------
* open current directory :  `open .`
* open Library directory : `open /Library`
* open file with linked default app : `open mac.md`

Change the default app for a file type
--------
1. find a file in Finder
2. right click on you file
3. select Get Info
4. you can find out how to change the default app
