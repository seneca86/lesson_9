# Functions

### Define

Although Python is not _stricto sensu_ a functional language, functions play an important role in it. Functions are pieces of code that usually take an input and return an output, although there are functions that just perform an action. Functions are _defined_ once and _invoked_ typically more than once.

Definition of a function requires the keyword `def` and the `:`. Let's practice with a few simple examples:

```python
def minimal_fun():
    pass
minimal_fun()
```

```python
def say_hello():
    print('Hello')
say_hello()
```

```python
def tell_me_true():
    return True
tell_me_true()
```

### Arguments

The functions above did not have any argument. We call _arguments_ the values we pass into a function, which internally become _paramters_.

```python
def introduce(name):
    print(f'My name is {name}')
introduce('Javier')
```

`if-else` clauses and loops are often found in functions. Let's see an example of this with a function that tells us what to do during debt crises.

```python
def debt_crisis(lever):
    if lever=='austerity':
        print('spend less')
    elif lever=='default':
        print('restructure your debt')
    elif lever=='print money':
        print('monetize your debt')
    elif lever=='fiscal policy':
        print('redistribute wealth')
    else:
        print('Disaster')
debt_crisis('austerity') 
debt_crisis('default') 
debt_crisis('print money') 
debt_crisis('fiscal policy') 
```

If we do not explicitly `return` an output and we try to assign the output to a variable, it will be `None`.

```python
what_to_do = debt_crisis('austerity')
print(what_to_do)
```

### None

`None` is an important value in Python that is used for missing values, and should not be confused with `False`.

```python
def check_nones(what):
    if what is None:
        print('this is None')
    elif what:
        print('this is something')
    else:
        print('this is False')
check_nones(None)
check_nones(42)
check_nones(False)
```

