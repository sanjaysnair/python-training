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

### Source Code
- source files use the ".py" extension and are called "modules"
- executed as "python <filename>"

**Example: Command line argument**
```
# import modules used here -- sys is a very standard one
import sys

print("Hello there ", sys.argv[1])
```

**output**
```
Sanjays-MacBook-Air:python_training sanjaysnair$ python3 hello.py sanjay
Hello there  sanjay
```

**[Download](cmd_argv.py)**

### User-defined Functions
```
# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

def repeat_with_star(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * s * s 
    if exclaim:
        result = result + '!!!'
    return result

print(repeat("Sanjay", True))
print(repeat("GTO", True))
```

**[Download](function_repeat_str.py)**

- Repeating a string works with operators **'+'** or **'*'**
- Repeat operators are overloaded because it behaves different for numbers and string
- The **def** keyword defines the function with its parameters within parentheses and its code indented
- **Docstring** inside triple quotes define what function does


### Indentation
- [PEP8](https://www.python.org/dev/peps/pep-0008/#indentation) says 4 space indentaion as standard
- Code is based on whitespace indentation
- No semicolon delimiter for statements
- Before new line the statement ends
- Indentation is important
- Keep the same indentation for the same logical block always (eg: if, for, while, function, class)


### Code Checked at Runtime
```
import function_repeat_str

"""
This module will compile successfully even thoug we have called function 'repeeat' with typo
Only when it runs, it throws: NameError: name 'repeeat' is not defined
"""

name = input('Enter your company name: ')
if name == 'SG':
    print(repeeat(name)) # function name is called wrongly
```
_This example shows how the compiler passes the code even though the function is called incorrectly_

[Download](compile_success.py)


### Variable Names
- Python prefers the underscore
- use "name" if it's a single name, and "names" if it's a list of names, and "tuples" if it's a list of tuples
- do not use keywords like 'print' and 'while' as variable names
- do not use built-ins like 'str' and 'list' as variable names

### More on Modules and their Namespaces
```
  import sys

  # Now can refer to sys.xxx facilities
  sys.exit(0)
```

- Here we have imported "sys" on top and then used "sys.exit(0)"
- Another way we can do "from sys import argv, exit" on top, and then direct use "exit(0)"
- In the first way: "sys" is a namespace

**Python Standar Library**
_many modules and packages which are bundled with a standard installation of the Python interpreter_

- sys — access to exit(), argv, stdin, stdout, ...
- re — regular expressions
- os — operating system interface, file system

### help(), and dir()
- help() function pulls up documentation strings for various modules, functions, and methods
- dir() function tells you what the attributes of an object are
- help(len) — help string for the built-in len() function; note that it's "len" not "len()", which is a call to the function, which we don't want
- help(sys) — help string for the sys module (must do an import sys first)
- dir(sys) — dir() is like help() but just gives a quick list of its defined symbols, or "attributes"
- help(sys.exit) — help string for the exit() function in the sys module
- help('xyz'.split) — help string for the split() method for string objects. You can call help() with that object itself or an example of that object, plus its attribute. For example, calling help('xyz'.split) is the same as calling help(str.split).
- help(list) — help string for list objects
- dir(list) — displays list object attributes, including its methods
- help(list.append) — help string for the append() method for list objects

```
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
>>> dir(sys.argv)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(sys.argv.__add__)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__objclass__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']


>>> help(sys.argv.count)
Help on built-in function count:

count(...) method of builtins.list instance
    L.count(value) -> integer -- return number of occurrences of value
(END)
```


