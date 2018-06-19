Python
========

Install python
------
### Mac
#### python2
```shell
brew install python@2
```
#### python3
```shell
brew install python3
```

Source Code Encoding
--------

```python
# -*- coding: encoding -*-
# -*- coding: cp-1252 -*-
```

```python
#!/usr/bin/env python3
# -*- coding: utf8 -*-
```


Numbers
--------
```python
17 / 3   # 5.666666666666667
17 // 3  # 5
17 % 3   # 2
5 ** 2   # 25
```

Strings
--------
```python
'spam eggs'
"spam eggs"
print('C:\some\name')

#raw string
print(r'C:\some\name') # C:\some\name

#multiple lines
print("""
Usage: thingy [OPTIONS]
    -h                              Display this usage message
    -H hostname                     Hostname to connect to
""")

# \ 쓰면 \n이 자동으로 붙는거를 방지함
print("""\
Usage: thingy [OPTIONS]
    -h                              Display this usage message
    -H hostname                     Hostname to connect to
""")


print('''\
Usage: thingy [OPTIONS]
    -h                              Display this usage message
    -H hostname                     Hostname to connect to
''')
```

### string concatenation
```python
3 * 'un' + 'ium'   # unununium
'Py' 'thon'     # Python
```

### string index & slicing
```python
word = 'Python'
word[0]         # 'P'
word[5]         # 'n'
word[-1]        # 'n'
word[-2]        # 'o'
word[-6]        # 'P'

word[0:2]       # 'Py'
word[2:5]       # 'tho'
word[:2] + word[2:] # 'Python'
word[:4] + word[4:] # 'Python'
word[:2]        # 'Py'
word[4:]        # 'on'
word[-2:]       # 'on'
word[42]        # exception
word[4:42]      # 'on'
word[42:]       # ''

# string length
len('alpa44')   # 6
```

Lists
--------
```python
squres = [1,4,9,16,25]

# index & slice
squares[0]      # 1
squares[-1]     # 25
squares[-3:]    # [9, 16, 25]
squares[:]      # [1,4,9,16,25]

# concatenation
squares + [36,49,64,81,100]     # [1,4,9,16,25,36,49,64,81,100]

# mutable type
cubes = [1,8,27,65,125]
cubes[3] = 64
cubes           # [1,8,27,64,125]

# add element
cubes.append(216)
cubes.append(7 ** 3)
cubes                   # [1,8,27,64,125,216,343]

# assignment to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters                             # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []                   # ['a', 'b', 'f', 'g']
letters[:] = []                     # []

# length of list
letters = ['a', 'b', 'c', 'd']
len(letters)                        # 4


# nest lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)                            # [['a', 'b', 'c'], [1, 2, 3]]
x[0]                                # ['a', 'b', 'c']
x[0][1]                             # 'b'
```

Multiple Assignment
--------

```python
#fibonacci series
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```

print
--------
```python
i = 256*256
print('The value of i is', i)       #  The value of i is 65536

# keyword argument end, \n을 대체함
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

>>> 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

if statements
--------

```python
if x < 0:
    x = 0
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```


for statements
--------

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

cat 3
window 6
defenestrate 12

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)     
print(words)

>>> ['defenestrate', 'cat', 'window', 'defenestrate']

# range
for i in range(5):
    print(i)
>>>
0
1
2
3
4

range(5,10)         # 5 ... 9
range(0, 10, 3)     # 0, 3, 6, 9
range(-10, -100, -30)   # -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
>>>
0 Mary
1 had
2 a
3 little
4 lamb

# break and continue, else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
>>>
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
>>>
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9

# pass
while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass
```

enumerate
--------

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
>>> [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]


list(enumerate(seasons, start=1))
>>> [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```


Functions
--------
```python
def fib(n):
    """Print a Fibonacci series up to n."""     # docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
>>>
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 


def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)
>>>
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

### Default Argument Values
```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# default values는 최초 1번만 evaluated됨 (mutable object일때는 주의해서 사용)
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
>>> [1]
print(f(2))
>>> [1, 2]
print(f(3))
>>> [1, 2, 3]
```


### Keyword Arguments
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                # 1 positional argument
parrot(voltage=1000)                        # 1 keyword argument
parrot(voltage=100000, action='VOOOOOM')    # 2 keyword arguments
parrot(action='VOOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')   # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword


# formal parameter : *name, **name 
# *name : formal parameter이후 positional arguments를 tuple형태로 받는다
# **name : formal parameter를 제외한 keyworkd arguments를 dict형태로 받는다
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("arguments = ", arguments)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print("keywords = ", keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger"
        ,"It's very runny, sir."
        ,"It's really very, VERY runny, sir."
        ,shopkeeper="Michael Palin"
        ,client="John Cleese"
        ,sketch="Cheese Shop Sketch")
>>>
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
arguments =  ("It's very runny, sir.", "It's really very, VERY runny, sir.")
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
keywords =  {'shopkeeper': 'Michael Palin', 'client': 'John Cleese', 'sketch': 'Cheese Shop Sketch'}
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

### Arbitrary Argument Lists
```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):     # *args 뒤에는 keyword-arg만 올수 있다
    return sep.join(args)

concat("earth", "mars", "venus")
>>> 'earch/mars/venus'
concat("earth", "mars", "venus", sep=".")
>>> 'earth.mars.venus'
```

### Unpacking Argument Lists
```python
list(range(3, 6))
>>> [3, 4, 5]

args = [3, 6]
list(range(*args))
>>> [3, 4, 5]

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action":"VOOM"}
parrot(**d)
```

### Lambda Expressions
```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
>>> 42

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
>>> [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### Documentation strings
```python
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)
```

### Function Annotations
```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
```

Coding Style
--------
### PEP8
* 4-space indentation, and no tabs
* Wrap lines so that they don't exceed 79 characters
* When possible, put comments on a line of their own
* Use docstrings
* Use spaces around operators and after commas, but not directly inside bracketing constructs : a = f(1, 2) + g(3, 4) 
* CamelCase for classes and lower_case_with_underscores for functions and methods

Virtualenv
--------
* install
```shell
pip3 install virtualenv
```

Setuptools
--------
### easy_install

Pip
--------
### for pyton2
### for python3
* install packages
```shell
pip3 install <package>
```
* update package
```shell
pip3 install --upgrade <package>
pip3 install --upgrade pip setuptools wheel
```

Wheel
--------


Anaconda
--------
### Uninstall in Mac
* Remove the configs
```shell
conda install anaconda-clean
anaconda-clean --yes
```
* Delete the anaconda install folder
```shell
rm -rf ~/anaconda
```
* Delete backup of configs that is created by `anaconda-clean --yes`
```shell
rm -rf ~/.anaconda_backup
```

