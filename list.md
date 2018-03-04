[Index](/python-training)  |  [Introduction](/python-training/intro)  |  [List](/python-training/list) 

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

### FOR and IN

_for var in list -- is an easy way to look at each element in a list_

```
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  ## 30
```

_The *in* construct on its own is an easy way to test if an element appears in a list_
```
gto = ['Bengaluru', 'Paris', 'Bucharest']
if 'Paris' in gto:
    print('yay')
```
