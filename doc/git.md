# About Git

## Setting git configuration

### git config
- /etc/gitconfig : git config --system
- ~/.gitconfig : git config --global
- .git/config

```
# set config on ~/.gitconfig
git config --global user.name "Steve Cho"
git config --global user.email steve@stayge.io
git config --global merge.tool vimdiff  # apply diff tool

# set config on .git/config
git config --global user.name "Steve Cho"

# set config on /etc/gitconfig
git config --system user.name "Steve Cho"

# show configuration
git config --list
```

## help
```
git help <verb>
git <verb> --help
man git-<verb>
```

## Basic Commands
```
# create empty git repository
git init
git add *.c
git add README
git commit -m 'initial project version'

# clone existing git repository
git clone git://github.com/schacon/grit.git
git clone git://github.com/schacon/grit.git mygrit

# Check the status of files
git status

# put files to stage area
git add <file>

# diff
git diff  # compare working directory with staging area
git diff --cached # compare staging area with repository
git diff --staged # same above

# commit
git commit
git commit -m "blah blah"  # commit with message
git commit -a  # skip stagin area

# edit commit
git commit -m 'initial commit'
git add forgotten_file
git commit --ament

# remove file
git rm <file>
git rm log/\*.log
git rm \*~
git rm --cached readme.txt  # remove from staging area

# rename file
git mv README.txt README

# commit history
git log
git log --abbrev-commit
git log -p -2   # -p show diff result, -2 show last 2 commit
git log --stat 
git log --pretty=oneline
git log --pretty=format:"%h - %an, %ar : %s"
git log --pretty=format:"%h %s" --graph
git log --pretty="%h - %s" --author=ryancho --since="2018-01-01" --before="2018-08-01"
git log origin/master..HEAD
git log origin/dev-steve..HEAD

# change to unstaged
git add test.txt
git reset HEAD test.txt

# restore modified files
git checkout -- benchmarks.rb

# check remote repository
git remote
git remote -v
git remote add pb git://github.com/paulboone/ticgit.git # add remote repository
git remote rename pb paul
git remote rm paul
git remote show [remote-name]

# sync remote to local repository
git fetch [remote-name]

# push to remote repository
git push origin master

# tag
git tag
git tag -l 'v1.4.2.*'
git tag -a v1.4 -m 'my version 1.4' # annotated tag
git show v1.4
git tag v1.4-lw  # lightweight tag
git tag -a v.12 -m 'version 1.2' [commit checksum]
git push origin [tag name]  # push tags to remote repository
git push origin --tags # push all tags to remote repository

# branch
git branch  # show branch list
git branch -v
git branch --no-merged
git branch --merged
git branch [name]  # create new branch
git checkout [branch name]  # switch to the branch (change HEAD pointer)
git checkout -b [branch name] # create a new branch and switch to the branch
git merge [branch name] # merge
git branch -d [branch name] # remove branch
git push [remote] [branch | local branch:remote branch]  # push local branch to remote branch
git push origin serverfix
git push origin serverfix:serverfix
git push origin serverfix:awesomebranch
git checkout -b sf origin/serverfix
git checkout --track origin/dev-steve # create tracking branch
git branch --set-upstream-to=origin/[branch] # track remote branch
git push origin :serverfix  # remove remote branch

# show
git show [commit hash|branch|tag]
git rev-parse [branch|tag]
git reflog
git show HEAD@{n}
git show HEAD@{2}
git show master@{yesterday}
git show HEAD^ # show the previous commit, ^ means parent
git show HEAD~

# stash
git stash
git stash list
git stash apply [stash name]
git stash apply [stash name] --index  # restore with staging area
git stash drop

# blame
git blame -L 12,22 simplegit.rb
```




## .gitignore file
```
# is comments

# ignore files with .a extension
*.a

# even though above line ignore files with .a extension, lib.a is not ignored
!lib.a

# ignore TYODO file in root directory, but don't ignore TODO file in subdirection like /subdir/TODO
/TODO

# ignore all files in build/ directory
build/

doc/*.txt

# ignore all .txt files in doc directory
doc/**/*.txt
```

## Git 용어
- master : svn의 trunk에 해당(메인 브랜치)
- index (staging area) : 로컬저장소에 반영되기 전 단계
- snapshot : svn은 변경사항을 저장, git은 파일의 스냅샵을 저장
- HEAD : pointer of working branch

## github에 레파지토리 생성하기
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

## git 명령어
- git clone <저장소경로> : 저장소 받아오기(최초)
- git status : 작업 디렉토리 변경 사항 확인
- git log

- git init : 저장소생성
- git add README.md : 인덱스(스테이지)에 파일 추가
- git reset HEAD : 스테이지 추가된 내역 취소
- git commit -m "first commit" : HEAD에 반영
- git commit -a : 스테이지 추가와 커밋을 동시

- git remote add origin https://github.com/alpa44/alap44_repo.git : 로컬저장소 -> 원격저장소로 연결
- git push -u origin master : 원격저장소에 반영

- git pull : 원격저장소 -> 로컬저장소 내려받고 작업디렉토리에 병합 git fetch + git merge
- git fetch : 원격저장소 -> 로컬저장소 내려받기
- git merge feature_x : 브랜지 병합

- git branch : 브랜치 조회
- git branch --no-merged 
- git branch --merged
- git branch -d feature_x : 브랜치 삭제
- git checkout -b feature_x : 브랜치 생성
- git checkout master : 브랜치 변경
- git checkout -- : 수정했지만 아직 스테이지에 추가하지 않은 파일을 되돌릴 때
- git checkout -- <파일이름> : 로컬 변경 내용 되돌리기
- git merge <브랜치>
- git rebase <브랜치> : merge와 병합은 동일하지만 병합 히스토리를 정리함

- git config --global core.editor /usr/bin/vim : editor 지정

- git diff <원래branch> <비고대상branch> 
- git tag : 태그 목록 조회
- git tag <name> : 꼬리표 달기
- git tag -a <name> : 작업자, 설명등을 추가로 저장
- git tag -d <name> : 태그 지우기

- 로컬저장소에 commit한 파일 되돌리기
	git fetch origin
	git reset --hard origin/master

## remote branch clone하기
- git clone -b <branch> <remote_repo> <dir>
- e.g> git clone -b develop https://alpa44@bitbucket.org/alpa44/astock.git astock-dev
