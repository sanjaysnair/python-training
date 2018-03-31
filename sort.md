[Index](/python-training)  |  [Introduction](/python-training/intro) |  [String](/python-training/string) |  [List](/python-training/list) |  [Sorting](/python-training/sort) |  [Dict and Files](/python-training/dict_file)

## Python Sorting

sorted(list) function, takes a list and returns a new list with those elements in sorted order
```
a = [5, 1, 4, 3]
print(sorted(a))  ## [1, 3, 4, 5]
print(a)  ## [5, 1, 4, 3]
```

list.sort() method is an alternative

The sorted() function can be customized through optional arguments. The sorted() optional argument reverse=True, e.g. sorted(list, reverse=True), makes it sort backwards.
```
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']
```


### Custom Sorting With key=

For more complex custom sorting, sorted() takes an optional "key=" specifying a "key" function that transforms each element before comparison.

```
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
```

specifying "str.lower" as the key function is a way to force the sorting to treat uppercase and lowercase the same
```
## "key" argument specifying str.lower function to use for sorting
print(sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']
```


```
## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']

print(sorted(strs))  ## ['wa', 'xc', 'yd', 'zb']
```

### sort() method

```
alist.sort()            ## correct
alist = blist.sort()    ## NO incorrect, sort() returns None
```

- The sort() method must be called on a list; it does not work on any enumerable collection (but the sorted() function above works on anything).
- The sort() method changes the underlying list and returns None



## Tuples
- A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate.
- Tuples are like lists, except they are immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be mutable).
- Tuples play a sort of "struct" role in Python -- a convenient way to pass around a little logical, fixed size bundle of values.
- A function that needs to return multiple values can just return a tuple of the values. For example, if I wanted to have a list of 3-d coordinates, the natural python representation would be a list of tuples, where each tuple is size 3 holding one (x, y, z) group.

```
tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])    ## hi
tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
```

To create a size-1 tuple, the lone element must be followed by a comma.
```
 tuple = ('hi',)   ## size-1 tuple
```

Assigning a tuple to an identically sized tuple of variable names assigns all the corresponding values. If the tuples are not the same size, it throws an error. This feature works for lists too.
```
(x, y, z) = (42, 13, "hike")
print z  ## hike
(err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple
```


### List Comprehensions

A list comprehension is a compact way to write an expression that expands to a whole list.

Suppose we have a list nums [1, 2, 3, 4], here is the list comprehension to compute a list of their squares [1, 4, 9, 16]:
```
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
```

```
strs = ['hello', 'and', 'goodbye']

shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']
```


You can add an if test to the right of the for-loop to narrow the result. The if test is evaluated for each element, including only the elements where the test is true.

```
## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANNANA']
```
