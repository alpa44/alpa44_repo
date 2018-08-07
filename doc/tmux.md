# About tmux

**tmux** is a terminal multiplexer


## Installation
### Mac OS X
```
brew install tmux
```

## Components
- session : tmux execution unit, consists of windows
- window : can be used as a tab within a session
- pane : split screen within a window
- status bar : displayed at the bottom of the screen

## Commands for session
- prefix key
```
ctrl + b, <key>
```
- command mode
```
ctrl + b, :
```
- create a new session
```
tmux new -s <session-name>
```

- change session name
```
ctrl + b, $
```

- quit session
```
(within) exit
```

- detach session
```
ctrl + b, d
```

- list sessions
```
tmux ls
```

- attach session
```
tmux attach -t <session-number or session-name>
```

## Commands for window
- create a new window
```
ctrl + b, c
```

- create a new session with a window
```
tmux new -s <session-name> -n <window-name>
```

- change the window name
```
ctrl + b, ,
```

- quit the window
```
ctrl + b, &
ctrl + d
```

- switch between windows
```
ctrl + b, 0-9 : window number
            n : next window
            p : prev window
            l : last window
            w : window selector
            f : find by name
```

## Commands for pane
- split pane
```
ctrl + b, % : split horizontally
          " : split vertically
```

- switch between panes
```
ctrl + b, q <pane number>
ctrl + b, o : move to next pane in order
ctrl + b, arrow : move to the pane with arrow direction
```

- remove pane
```
ctrl + b, x
ctrl + d
```

- resize pane
```
(ctrl + b, :)
resize-pane -L 10
            -R 10
            -D 10
            -U 10
```

- change layout for pane
```
ctrl + b, spacebar
```

## Commands for shortcut
- list shortcuts
```
ctrl + b, ?
```

- bind or unbind key
```
(ctrl + b, :)
bind-key [-cnr] [-t key-table] key command [arguments]
unbind-key [-acn] [t key-table] key
```

- set options
```
set -g <option-name> <option-value> : set-option
setw -g <option-name> <option-value> : set-window-option
```

## Copy Mode
In copy mode, you can scroll the console or copy the contents
- switch to copy mode
```
ctrl + b, [
```

- exit out of copy mode
```
(in copy mode) q or ESC
```

- move
```
arrow : move cursor
pageUp, pageDown : move throuth pages
```

## Configuration file
- ~/.tmux.conf
