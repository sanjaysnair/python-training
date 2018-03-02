## Introduction

### Characteristics
- dynamic, interpreted (bytecode-compiled) language
- no type declaration
- no compile time type checking
- interactive shell
- case sensitive
- everything is an object

### Interactive Shell
```
Sanjays-MacBook-Air:~ sanjaysnair$ python3
Python 3.6.1 (default, Jun  5 2017, 01:51:51) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a=10
>>> a
10
>>> a+2
12
>>> a='gto'
>>> a
'gto'
>>> len(a)
3
>>> a+len(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> a+str(len(a))
'gto3'
>>> foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
>>>
```

