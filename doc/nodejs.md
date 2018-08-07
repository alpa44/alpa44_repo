#About nodejs


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
