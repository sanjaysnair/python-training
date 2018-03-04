[Index](/python-training)  |  [Introduction](/python-training/intro) |  [String](/python-training/string) 

## String

- Python has a built-in string class named "**str**"
- String literals can be enclosed by either double or single quotes
- A double quoted string literal can contain single quotes (e.g. "I didn't do it")
- A string literal **can span multiple lines**, but there must be a backslash \ at the end of each line to escape the newline
- String literals inside triple quotes, """" or ''', can span multiple lines of text
- Python strings are "**immutable**" which means they cannot be changed after they are created
- Characters in a string can be accessed using the standard [ ] syntax
- Python uses **zero-based indexing**
- **"slice" syntax** works to extract any substring from a string
- **len(string)** function returns the length of a string
- The [ ] syntax and the len() function actually work on any sequence type -- strings, lists, etc
- '+' operator can concatenate two strings

```
>>> sggsc = 'Bangalore'
>>> print(sggsc[1])
a
>>> print(sggsc[-11])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> print(sggsc[-1])
e
>>> print(len(sggsc))
9
>>> print(sggsc + ', Paris, Bucharest')
Bangalore, Paris, Bucharest
```

**str() function converts values to a string**
```
>>> pi = 3.14
>>> print(pi)
3.14
>>> print('The value of pi is ' + pi)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not float
>>> print('The value of pi is ' + str(pi))
The value of pi is 3.14
```

**For numbers, the standard operators, +, /, * work in the usual way. There is no ++ operator, but +=, -=, etc. work**
**If you want integer division, it is most correct to use 2 slashes -- e.g. 6 // 5 is 1**
```
>>> 6/5
1.2
>>> 6//5
```

### Print()

**Concat strings by comma separation**
```
>>> print('Bangalore', 'Paris', 'Bucharest')
Bangalore Paris Bucharest
```

**new line and tabs**
```
>>> print("this\t\n and that")
this
 and that
>>>
```

**row output**
```
>>> print(r"this\t\n and that")
this\t\n and that
>>>
```

**docstring**
```
>>> print("""It was the best of times.
...   It was the worst of times.""")
It was the best of times.
  It was the worst of times.
>>>
```


### String methods

- s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
- s.strip() -- returns a string with whitespace removed from the start and end
- s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
- s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
- s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
- s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
- s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
- s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

**![Reference](https://docs.python.org/3/library/stdtypes.html#string-methods)**

### String slice

**The slice s[start:end] is the elements beginning at start and extending up to but not including end**
Suppose we have s = "Hello"
[Hello](hello.png)

- s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
- s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
- s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
- s[1:100] is 'ello' -- an index that is too big is truncated down to the string length

**Python uses negative numbers to give easy access to the chars at the end of the string**
- s[-1] is 'o' -- last char (1st from the end)
- s[-4] is 'e' -- 4th from the end
- s[:-3] is 'He' -- going up to but not including the last 3 chars.
- s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

**(Slice Rule)For any index n, s[:n] + s[n:] == s**

### String %

_Python has a printf()-like facility to put together a string. The % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point), and the matching values in a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parentheses):_

```
>>> print("%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down'))
3 little pigs come out or I'll huff and puff and blow down
```

_You cannot just split the line after the '%' as you might in other languages, since by default Python treats each line as a separate statement (on the plus side, this is why we don't need to type semi-colons on each line). To fix this, enclose the whole expression in an outer set of parenthesis -- then the expression is allowed to span multiple lines. This code-across-lines technique works with the various grouping constructs detailed below: ( ), [ ], { }._

```
>>> text = ("%d little pigs come out or I'll %s and %s and %s" %
...     (3, 'huff', 'puff', 'blow down'))
>>> print(text)
3 little pigs come out or I'll huff and puff and blow down
```

### If Statement
- Python does not use { } to enclose blocks of code for if/loops/function etc
- Python uses the colon (:) and indentation/whitespace to group statements
- Boolean test for an if does not need to be in parenthesis
- It can have *elif* and *else* clauses
- The "zero" values all count as false: None, 0, empty string, empty list, empty dictionary
- Boolean type with two values: True and False
- Python has the usual comparison operations: ==, !=, <, <=, >, >=
- Boolean operators are the spelled out words *and*, *or*, *not*

**example**
```
speed = int(input('Enter your vehicle speed: '))
mood = input('Enter police mood(terrible / bad / cool): ')

if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
      print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
      print("I'm going to have to write you a ticket.")
      #write_ticket()
    else:
      print("Let's try to keep it under 80 ok?")
else:
    print("You drive safe :)")
```

**output**
```
Sanjays-MacBook-Air:sggsc sanjaysnair$ python3 if_statement.py
Enter your vehicle speed: 100
Enter police mood(terrible / bad / cool): terrible
License and registration please
You have the right to remain silent.
```

[Download](if_statement.py)

