# About nodejs

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine

## Versions of node
- Current : 10.8.0
- LTS : 8.11.3

## npm
```
npm list --global
```

### Installing Packages in Local Mode
```
npm init
npm install # install packages in package.json
npm install <package>
npm install <package> --save-dev
npm install jshint --save-dev
```

### use as a build tool
```
npm run  # show script list
npm run <property>  # run a specific property
npm run <property> -s   # only ouput
```

## nvm
Node version manager

### Installation
- on MacOS

```shell
brew install nvm
 
mkdir ~/.nvm

add the following to ~/.bash_profile
> export NVM_DIR=$HOME/.nvm
> . /usr/local/opt/nvm/nvm.sh
```

### Usage
- To download, compile, and install the latest release of node
```
nvm install node // the latest release of node
nvm install v10.2.1 // the version 10.2.1 of node
```

- To use the installed version
```
nvm use node
```

- Run
```
nvm run node --version
```

- Run any arbitrary command in a subshell with the desired version of node
```
nvm exec 4.2 node --version
```

- Get the path to the executable to where it was installed
```
nvm which 5.0
```

- set default alias
```
nvm alias default v10.2.1
```

### aliases
- `node` : installs the latest version of node
- `iojs` : installs the latest version of io.js


## nodemon
A utility that will monitor for any changes in your source and automatically restart your server.

### installation
```
npm install -g nodemon
```

### Features
- Automatic restarting of application.
- Detects default file extension to monitor.
- Default support for node & coffeescript, but easy to run any executable (such as python, make, etc).
- Ignoring specific files or directories.
- Watch specific directories.
- Works with server applications or one time run utilities and REPLs.
- Requirable in node apps.
- Open source and available on github.

## pm2
Advanced, production process manager for Node.js

### installation
```
npm install pm2 -g
```

### CheatSheet
```
# Fork mode
pm2 start app.js --name my-api # Name process

# Cluster mode
pm2 start app.js -i 0        # Will start maximum processes with LB depending on available CPUs
pm2 start app.js -i max      # Same as above, but deprecated.
pm2 scale app +3             # Scales `app` up by 3 workers
pm2 scale app 2              # Scales `app` up or down to 2 workers total

# Listing

pm2 list               # Display all processes status
pm2 jlist              # Print process list in raw JSON
pm2 prettylist         # Print process list in beautified JSON

pm2 describe 0         # Display all informations about a specific process

pm2 monit              # Monitor all processes

# Logs

pm2 logs [--raw]       # Display all processes logs in streaming
pm2 flush              # Empty all log files
pm2 reloadLogs         # Reload all logs

# Actions

pm2 stop all           # Stop all processes
pm2 restart all        # Restart all processes

pm2 reload all         # Will 0s downtime reload (for NETWORKED apps)

pm2 stop 0             # Stop specific process id
pm2 restart 0          # Restart specific process id

pm2 delete 0           # Will remove process from pm2 list
pm2 delete all         # Will remove all processes from pm2 list

# Misc

pm2 reset <process>    # Reset meta data (restarted time...)
pm2 updatePM2          # Update in memory pm2
pm2 ping               # Ensure pm2 daemon has been launched
pm2 sendSignal SIGUSR2 my-app # Send system signal to script
pm2 start app.js --no-daemon
pm2 start app.js --no-vizion
pm2 start app.js --no-autorestart
```

### Folder structure
```
$HOME/.pm2 will contain all PM2 related files
$HOME/.pm2/logs will contain all applications logs
$HOME/.pm2/pids will contain all applications pids
$HOME/.pm2/pm2.log PM2 logs
$HOME/.pm2/pm2.pid PM2 pid
$HOME/.pm2/rpc.sock Socket file for remote commands
$HOME/.pm2/pub.sock Socket file for publishable events
$HOME/.pm2/conf.js PM2 Configuration
```

### Features
- Behavior configuration
- Source map support
- Container Integration
- Watch & Reload
- Log management
- Monitoring
- Module System
- Max memory reload
- Cluster Mode
- Hot reload
- Development workflow
- Startup Scripts
- Deployment workflow
- PaaS Compatible
- Keymetrics monitoring
- API

## Books
- Node.js 교과서 o
- 웹 서비스를 만들며 배우는 node.js 프로그래밍
- Do it! Node.js 프로그래밍 o
- Node.js로 봇 만들기 o
- 초보자를 위한 Node.js 200제 o
- 자바스크립트로 서버와 클라이언트 구축하기
- 모던 자바스크립트 입문
- Node.js 마이크로서비스 코딩 공작소
