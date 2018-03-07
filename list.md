[Index](/python-training)  |  [Introduction](/python-training/intro) |  [String](/python-training/string) |  [List](/python-training/list) 

### Python List

- List literals are written within square brackets []
- Works like string - len() function works
- Index starts from 0
- The "empty list" is just an empty pair of brackets [ ]
- The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] 

```
gto = ['Bengaluru', 'Paris', 'Bucharest']
print(gto[1])   ## Paris
print(len(gto)) ## 3
```

**Assignment with an = on lists does not make a copy**
```
# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.
gto = ['Bengaluru', 'Paris', 'Bucharest']
global_tools = gto
global_tools.append('test')
print(gto)
print(global_tools)
```
[Download](list_assignment.py)


### FOR and IN

**for var in list -- is an easy way to look at each element in a list**
```
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  ## 30
```

**The *in* construct on its own is an easy way to test if an element appears in a list**
```
gto = ['Bengaluru', 'Paris', 'Bucharest']
if 'Paris' in gto:
    print('Found!!')
```

**You can also use for/in to work on a string**
```
str = 'Global Tools'
for i in str:
    print(i)
```

### Range

**range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number**
```
## print the numbers from 0 through 9
for i in range(10):
    print(i)
```

**xrange() is used for performance sensitive algo. in Python2. Python3 this is achieved in range()**

### While Loop

**Python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java, altering the course of the innermost loop**
```
## Access every 3rd element in a list
i = 0
a = range(20);
while i < len(a):
    print(a[i])
    i = i + 3
```

**List Methods**
Here are some other common list methods.

- list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
- list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
- list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
- list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
- list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
- list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
- list.reverse() -- reverses the list in place (does not return it)
- list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

__Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.__

```
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
```

__Common error: note that the above methods do not *return* the modified list, they just modify the original list.__
```
list = [1, 2, 3]
print(list.append(4))   ## NO, does not work, append() returns None
## Correct pattern:
list.append(4)
print(list)  ## [1, 2, 3, 4]
```

### List Build Up

__One common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:__
```
list = []          ## Start as the empty list
list.append('a')   ## Use append() to add elements
list.append('b')
print(list)
```

### List Slices

__Slices work on lists just as with strings, and can also be used to change sub-parts of the list.__
```
list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']
```

