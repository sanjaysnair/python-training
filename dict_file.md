[Index](/python-training)  |  [Introduction](/python-training/intro) |  [String](/python-training/string) |  [List](/python-training/list) |  [Sorting](/python-training/sort) |  [Dict and Files](/python-training/dict_file)

## Dict Hash Table

- Python's efficient key/value **hash table** structure is called a "**dict**".
- The contents of a dict can be written as a series of key:value pairs within braces { }
- e.g. dict = {key1:value1, key2:value2, ... }
- The "empty dict" is just an empty pair of curly braces {}
- **Strings, numbers, and tuples work as keys, and any type can be a value**
- Looking up a value which is not in the dict throws a KeyError
- **use "in" to check if the key is in the dict**
- **use dict.get(key) which returns the value or None if the key is not present**
- (or get(key, not-found) allows you to specify what value to return in the not-found case).

```
## Can build up a dict by starting with the the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print(dict['z'])                  ## Throws KeyError
if 'z' in dict: print(dict['z'])     ## Avoid KeyError
print(dict.get('z'))  ## None (instead of KeyError)
```

- A for loop on a dictionary iterates over its keys by default.
- The keys will appear in an arbitrary order.
- The methods dict.keys() and dict.values() return lists of the keys or values explicitly.
- There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary.
- All of these lists can be passed to the sorted() function.

```
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict: print(key)
## prints a g o

## Exactly the same as above
for key in dict.keys(): print(key)

## Get the .keys() list:
print(dict.keys())  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print(dict.values())  ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)
## a > alpha    o > omega     g > gamma
```


**Removed on Python3**
There are "iter" variants of these methods called iterkeys(), itervalues() and iteritems() which avoid the cost of constructing the whole list -- a performance win if the data is huge. However, I generally prefer the plain keys() and values() methods with their sensible names. In Python 3000 revision, the need for the iterkeys() variants is going away.
```
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

## works  only on python2
for k in dict.iterkeys():
    print(k)
```

## Dict Formatting

The % operator works conveniently to substitute values from a dict into a string by name:

```
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
# 'I want 42 copies of garfield'
print(s)
```

## Del

The "del" operator does deletions. In the simplest case, it can remove the definition of a variable, as if that variable had not been defined. Del can also be used on list elements or slices to delete that part of the list and to delete entries from a dictionary.
```
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print(list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print(dict)      ## {'a':1, 'c':3}
```

## File

- The open() function opens and returns a file handle that can be used to read or write a file in the usual way.
- The code f = open('name', 'r') opens the file into the variable f, ready for reading operations, and use f.close() when finished.
- Instead of 'r', use 'w' for writing, and 'a' for append.
- The standard for-loop works for text files, iterating through the lines of the file (this works only for text files, not binary files).
- The for-loop technique is a simple and efficient way to look at all the lines in a text file:

```
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:   ## iterates over the lines of the file
    print(line,)    ## trailing , so print does not add an end-of-line char
            ## since 'line' already includes the end-of line.
f.close()
```

**The f.readlines() method reads the whole file into memory and returns its contents as a list of its lines. The f.read() method reads the whole file into a single string, which can be a handy way to deal with the text all at once.**

**For writing, f.write(string) method is the easiest way to write data to an open output file**

## Files Unicode

The "codecs" module provides support for reading a unicode file.

```
import codecs

f = codecs.open('foo.txt', 'rU', 'utf-8')
for line in f:
  # here line is a *unicode* string
```
