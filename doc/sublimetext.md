# About Sublime Text


## Package Control

### Installation via Sublime Text console
- The console is accessed via the `ctrl+`` shortcut or the `View>Show Console` menu 
```
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

### Usage
- open the palette : press `cmd+shift+p`

## Babel
- adds proper syntax highlighting to your ES6/2015 and React JSX code

## SublimeLinter
- provides ESLint and JSHint integration into Sublime
- SublimeLinter-eslint or SublimeLinter-jshint
- must include a linter either into your project dependencies or install it globally
```
npm install --save-dev eslint
```

## Vue Syntax Highlight

## SideBar Enhancements
- manipulate files in your sidebar file tree

## JsPrettier
- allows developers to run Prettier on the current file they're editing from whin Sublime
- if you're already using ESLint for your project, then ESLint-Formatter would probably be more beneficial, as it will run `eslint --fix` on the file you're currently editing

## TrailingSpaces

## GitGutter
1. Gutter Icons, indicating inserted, modified or deleted lines
2. Diff Popup, with details about modified lines
3. Status Bar Text, with information about file and repository
4. Goto Change, to easily navigate between modified lines


## BracketHighlighter
- adds in cutter icons and color coding to the matching bracket, brace, parenthesis, or tag

## Vintage Mode
- Vintage is a vi mode editing package for Sublime Text

### Enabling Vintage
- disabled by default, via the `ignored_packages` setting
- remove `"Vintage"` from the list of ignored packages
   1. Select the `Preferences > Settings` menu item
   2. Edit the ignored_packages setting : remove Vintage
- execute the following in a terminal to fix a problem of slow key repeat
```
defaults write com.sublimetext.3 ApplePressAndHoldEnabled -bool false
```
