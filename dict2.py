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

## works  only on python2
for k in dict.iterkeys():
    print(k)