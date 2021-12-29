# Functions

## Define

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

## Arguments

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
        print(f'{what} is None')
    elif what:
        print(f'{what} is something')
    else:
        print(f'{what} is False')
check_nones(None)
check_nones(42)
check_nones(False)
check_nones('')
check_nones([])
```

### Positional and keyword arguments

By default, the position of the arguments has a meaning in a function; arguments that are identified solely by their position are called _positional arguments_. This is error-prone, and can be solved through _keyword arguments_.

```python
def tale(papa, mama, baby, goldilocks):
    print(f'{papa}, {mama}, and {baby}, found out {goldilocks} had eaten their meal')
tale('a big bear', 'a mid bear', 'a small bear', 'a little girl')
tale('a little girl', 'a small bear', 'a mid bear', 'a big bear')
tale(
    goldilocks='a little girl',
    baby='a small bear',
    mama='a mid bear',
    papa='a big bear'
    )
```

Another way to prevent errors when invoking a function is to provide defaul parameter values, which enter into action in case we forget to specify the value of one of the arguments.

```python
def clinical(height=1.90, weight=82):
    print(f'My height is {height} m and my weight is {weight} kg')
clinical()
clinical(1.80)
clinical(1.80, 90)
clinical(weight=100)
```

Default parameters are calculated when the function is defined, not run, so make sure you do not use mutable data types as default parameters. Else you may run into trouble as in the next example.

```python
def garbage_accumulator(garbage, accumulator=[]):
    accumulator.append(garbage)
    return accumulator
garbage_accumulator('one') 
garbage_accumulator('one') 
```

### Explode / gather positional arguments

When we do not know the number of arguments that our function will receive, the `*` sign helps put "everthing" or "everything else" (depending on whether there is a positional argument before) into a tuple.

```python
def shopping(must_have, nice_to_have, *args):
    print(f'I need to buy {must_have} and probably {nice_to_have}')
    print(f'I may also need {args}')
shopping('milk', 'cereals', 'bread')
```
 Note how the optional argument is wrapped in a tupple. Calling it `args` is not necessary but is a typical Python convention.

We can "explode" a tuple argument to positional parameters *args inside the function, which will be "regathered" inside into the tuple parameter `args`.

```python
args = ('bread', 'olive oil')
shopping('milk', 'cereals', *args)
shopping('milk', 'cereals', args)
```

Note the difference with and without the `*`.

### Explode / gather keyword arguments

The sign `**` allows us to group keyword arguments into a dictionary. Remember that inside the function we call it a (dictionary) _parameter_, and outside an _argument_. `kwargs` is just a conventional name.

The order of the arguments is:
1. Required positional arguments
2. Optional positional arguments (`*args`)
3. Optional keyword arguments (`**kwargs`)

Remember that the `**` again "explodes" the arguments outside the function, and "gathers" them as parameters inside the function. Let's run a couple of examples to get familiar with the casuistry.

```python
def clothes(**kwargs):
    print(f'I will buy {kwargs}')
kwargs = {'shirt': 'M', 'jeans':34}
clothes(socks='M')
clothes(socks='M', **kwargs)
```

Let's use what we learned on iterations to make the output cleaner.

```python
def clothes_size(hat='L', **kwargs):
    for key, value in kwargs.items():
        print(f'I will buy {key} of size {value}')
clothes_size(socks='M', hat='M')
```

