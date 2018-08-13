ㅇ Github
- Pull Request
- Fork
- Push
- Fetch
- Clone
- Commit

ㅇ Git 용어
- master : svn의 trunk에 해당(메인 브랜치)
- index (staging area) : 로컬저장소에 반영되기 전 단계
- snapshot : svn은 변경사항을 저장, git은 파일의 스냅샵을 저장
- HEAD

ㅇ github에 레파지토리 생성하기
- new repository 생성	
	echo "# alpa44_repo" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin https://github.com/alpa44/alpa44_repo.git
	git push -u origin master

- 이미 존재하는 레파지토리를 푸시하기
	git remote add origin https://github.com/alpa44/alpa44_repo.git
	git push -u origin master

ㅇ git 명령어
git clone <저장소경로> : 저장소 받아오기(최초)
git status : 작업 디렉토리 변경 사항 확인
git log

git init : 저장소생성
git add README.md : 인덱스(스테이지)에 파일 추가
git reset HEAD : 스테이지 추가된 내역 취소
git commit -m "first commit" : HEAD에 반영
git commit -a : 스테이지 추가와 커밋을 동시

git remote add origin https://github.com/alpa44/alap44_repo.git : 로컬저장소 -> 원격저장소로 연결
git push -u origin master : 원격저장소에 반영

git pull : 원격저장소 -> 로컬저장소 내려받고 작업디렉토리에 병합 git fetch + git merge
git fetch : 원격저장소 -> 로컬저장소 내려받기
git merge feature_x : 브랜지 병합

git branch : 브랜치 조회
git branch --no-merged 
git branch --merged
git branch -d feature_x : 브랜치 삭제
git checkout -b feature_x : 브랜치 생성
git checkout master : 브랜치 변경
git checkout -- : 수정했지만 아직 스테이지에 추가하지 않은 파일을 되돌릴 때
git checkout -- <파일이름> : 로컬 변경 내용 되돌리기
git merge <브랜치>
git rebase <브랜치> : merge와 병합은 동일하지만 병합 히스토리를 정리함

git config --global core.editor /usr/bin/vim : editor 지정

git diff <원래branch> <비고대상branch> 
git tag : 태그 목록 조회
git tag <name> : 꼬리표 달기
git tag -a <name> : 작업자, 설명등을 추가로 저장
git tag -d <name> : 태그 지우기

- 로컬저장소에 commit한 파일 되돌리기
	git fetch origin
	git reset --hard origin/master

ㅇ remote branch clone하기
- git clone -b <branch> <remote_repo> <dir>
- e.g> git clone -b develop https://alpa44@bitbucket.org/alpa44/astock.git astock-dev