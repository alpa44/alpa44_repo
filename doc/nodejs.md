#About nodejs

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine

## Versions of node
- Current : 10.8.0
- LTS : 8.11.3

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
nvm install node
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

### Commands
- run
```
pm2 start app.js
```

- monitoring
```
pm2 monit
```

- list all processes
```
pm2 list
```

- etc
```
pm2 stop
pm2 restart
pm2 delete
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
