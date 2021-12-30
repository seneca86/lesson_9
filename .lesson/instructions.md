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

### Keyword-only arguments

Python let's you specify keyword-only arguments by placing a `*` after the positional arguments and before the obligatorily-named arguments.

```python
def naming(one, *, two):
    print(f'{one} are positional')
    print(f'{two} must be named')
naming(('this', 'that'), two='keyword-only')
```

### Alter mutable arguments

Remember that mutable variables can be changed by a function even without explicitly returning anything.

```python
def alter(l1):
    l1[0] = 'Beware'
l2 = ['Ignore', 'the', 'risk']
alter(l2)
print(l2)
```

### Docstrings

Docstrings are string that provide information on a function. They can be invoked with the `help()` function. Docstrings are enclosed by triple quotes.

```python
def give_me_one():
    """
    Returns a one. This function is:
    - Useless
    - Just for illustrative purposes
    """
    return 1
give_me_one()
help(give_me_one)
```

### Functions are objects

A Python mantra states that _everything (in Python) is an object_. This includes function, which therefore become _first-class citizens_ in computer science jargon.

Imagine we build a function whose sole purpose is to run another function passed as argument.

```python
def run(fun_):
    return fun_()
run(give_me_one)
```

Although useless, this illustrates how a function can be passed to another function _as an object_. Importantly, we execute `run(give_me_one)` and not `run(give_me_one())`, because we want to pass the function, not the resuls.

Let's try an example with arguments:

```python
def do_sum(x, y):
    print(x + y)
def run_fun(fun_, x, y):
    fun_(x, y)
run_fun(do_sum, 3, 5)
```
An another example with positional arguments:

```python
def add_up(*args):
    return sum(args)
def run_with_args(fun_, *args):
    return fun_(*args)
run_with_args(add_up, 1, 2, 3)
```

## Inner functions

### Definition

Inner functions are functions defined within other functions, and the reationale for using them is the same as for using a regular function: to perform a repetitive, complex task.

```python
def reminder(*args):
    print(f'This is what I must do:')
    def print_task(t):
        print(f'do {t}')
        print(f'-------------')
    for a in args:
        print_task(a)
reminder('homework', 'cleaning', 'tidying up')
```

### Closures

A _closure_ is a function that is dynamically generated by another function and can both change and rememeber the values of variables that were created outside the function. Think of it as a dynamically created function that knows where it came from.

```python
def task_reminder(task):
    print(f'Generating specialized task printer ...')
    def task_printer():
        print(f'do {task}')
    return task_printer
specialized_homework_printer = task_reminder('homework')
specialized_cleaning_printer = task_reminder('cleaning')
```

The only output here is the "specialized" function, that we now can invoke.

```python
specialized_homework_printer()
specialized_cleaning_printer()
```

## Lambda functions

Lambda functions are anonymous functions expressed as a single statement, that are typically use to replace tiny functions.

For instance, the following function is so short it is a candidate for becoming a lambda function.

```python
def capitalize(word):
    return word.upper() + '!?'
capitalize('what')
```

If we pass it as an argument for another function, we can even define it within the call.

```python
def shout(sentence, fun_):
    for word in sentence:
        print(fun_(word))
shout('what is this', capitalize)
```

```python
shout('what is this', lambda x: x.upper() + '!?')
```

## Generators

### Definition

A generator is a Python sequence creation object, which allows to iterate through sequences of data with no need to create and store the sequence in memory.

We have already used `range()`, which is a generator (in older versions of Python it generated a list).

```python
sum(range(0, 10))
for i in range(5):
    print(i)
```

You may think of a generators as a function that keeps track of where it was the last time it was called, and starts from there. Once the generator runs its course, though, it becomes tapped out as we will see in the examples. 

### Generator functions

A generator function is a normal function that returns a generator object over which we can iterate. The only difference with a regular function is the use of `yield` instead of `return`. 

```python
def produce_generator(begin, end, step):
    n = begin
    while n < end:
        yield n
        n += step
type(produce_generator)
```

```python
gen_ = produce_generator(begin=10, end=20, step=2)
for i in gen_:
    print(i)
```

A generator can only be run once, meaning that we cannot restart a generator, that is why it has "memory". The generator in the example has become exhausted.

```python
for i in gen_:
    print(i)
```

### Generator comprehensions

A generator comprehension is similar to a list or dictionary comprehension, but is surrounded by parentheses and returns a generator object. You may think of it as a shorthand of a generator function that does the _yield_ invisibly.

```python
mini_gen = (x**2 for x in [1, 2, 3])
mini_gen
for i in mini_gen:
    print(i)
```

## Decorators

Decorators are functions that take one function as input and return another function, modifying it without changing its source code.

```python
def decorator_(fun_):
    def verbose(*args, **kwargs):
        print('This is an improved function')
        print('Positional arguments are ', args)
        print('Keyword arguments are ', kwargs)
        output = fun_(*args, **kwargs)
        print('The output is ', output)
        return output
    return verbose

def simple_fun(r, n):
    return (1 + r)**n

simple_fun(0.05, 10)
nicer_fun = decorator_(simple_fun)
nicer_fun(0.05, 10)
```

In the example above, when we pass the function to the decorator we obtain a new function that includes some additional statements.

A shortcut for this is to use the syntax `@decorator` right before the function we want to decorate.

```python
@decorator_
def compound(r, n, t):
    return (1 + r/n)**(n*t)
compound(r=0.05, n=4, t=10)
```

We can add several decorators to a function. The ones closer to the function are the ones executed first.

```python
def pretty_print(fun_):
    def five_digits(*args, **kwargs):
        output = fun_(*args, **kwargs)
        return f'{output:.5}'
    return five_digits

@pretty_print
@decorator_
def compound(r, n, t):
    return (1 + r/n)**(n*t)
compound(r=0.05, n=4, t=10)
```

## Namespaces and scope

