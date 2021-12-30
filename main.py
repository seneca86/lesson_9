# %%
def minimal_fun():
    pass
minimal_fun()
# %%
def say_hello():
    print('Hello')
say_hello()
# %%
def tell_me_true():
    return True
tell_me_true()
# %%
def introduce(name):
    print(f'My name is {name}')
introduce('Javier')
# %%
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
what_to_do = debt_crisis('austerity')
print(what_to_do)
# %%
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
# %%
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
# %%
def clinical(height=1.90, weight=82):
    print(f'My height is {height} m and my weight is {weight} kg')
clinical()
clinical(1.80)
clinical(1.80, 90)
clinical(weight=100)
# %%
def garbage_accumulator(garbage, accumulator=[]):
    accumulator.append(garbage)
    return accumulator
garbage_accumulator('one') 
garbage_accumulator('one') 
# %%
def shopping(must_have, nice_to_have, *args):
    print(f'I need to buy {must_have} and probably {nice_to_have}')
    print(f'I may also need {args}')
shopping('milk', 'cereals', 'bread')
# %%
args = ('bread', 'olive oil')
shopping('milk', 'cereals', *args)
shopping('milk', 'cereals', args)
# %%
def clothes(**kwargs):
    print(f'I will buy {kwargs}')
kwargs = {'shirt': 'M', 'jeans':34}
clothes(socks='M')
clothes(socks='M', **kwargs)
# %%
def clothes_size(hat='L', **kwargs):
    for key, value in kwargs.items():
        print(f'I will buy {key} of size {value}')
clothes_size(socks='M', hat='M')
# %%
def naming(one, *, two):
    print(f'{one} are positional')
    print(f'{two} must be named')
naming(('this', 'that'), two='keyword-only')
# %%
def alter(l1):
    l1[0] = 'Beware'
l2 = ['Ignore', 'the', 'risk']
alter(l2)
print(l2)
# %%
def give_me_one():
    """
    Returns a one. This function is:
    - Useless
    - Just for illustrative purposes
    """
    return 1
give_me_one()
help(give_me_one)

# %%
def run(fun_):
    return fun_()
run(give_me_one)
# %%
def do_sum(x, y):
    print(x + y)
def run_fun(fun_, x, y):
    fun_(x, y)
run_fun(do_sum, 3, 5)

# %%
def add_up(*args):
    return sum(args)
def run_with_args(fun_, *args):
    return fun_(*args)
run_with_args(add_up, 1, 2, 3)
# %%
def reminder(*args):
    print(f'This is what I must do:')
    def print_task(t):
        print(f'do {t}')
        print(f'-------------')
    for a in args:
        print_task(a)
reminder('homework', 'cleaning', 'tidying up')
# %%
def task_reminder(task):
    print(f'Generating specialized task printer ...')
    def task_printer():
        print(f'do {task}')
    return task_printer
specialized_homework_printer = task_reminder('homework')
specialized_cleaning_printer = task_reminder('cleaning')
# %%
specialized_homework_printer()
specialized_cleaning_printer()
# %%
def capitalize(word):
    return word.upper() + '!?'
capitalize('what')
# %%
def shout(sentence, fun_):
    for word in sentence:
        print(fun_(word))
shout('what is this', capitalize)
# %%
shout('what is this', lambda x: x.upper() + '!?')

# %%
sum(range(0, 10))
for i in range(5):
    print(i)
# %%
g = range(10)
for i in g:
    print(i)
    if i==5:
        break
next(g)
# %%
def produce_generator(begin, end, step):
    n = begin
    while n < end:
        yield n
        n += step
type(produce_generator)
# %%
gen_ = produce_generator(begin=10, end=20, step=2)
for i in gen_:
    print(i)
# %%
for i in gen_:
    print(i)
# %%
mini_gen = (x**2 for x in [1, 2, 3])
mini_gen
for i in mini_gen:
    print(i)
# %%
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
# %%
@decorator_
def compound(r, n, t):
    return (1 + r/n)**(n*t)
compound(r=0.05, n=4, t=10)
# %%
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
# %%
planck = 6.62e-34
def print_universal():
    print(f'What we see inside the function is {planck=}')
print_universal()
# %%
planck = 6.62e-34
def print_universal():
    # print(f'Try to access the variable AND change it {planck=}') # This fails
    planck = 42
print_universal()
planck
# %%
planck = 6.62e-34
def print_universal():
    planck = 42
    print(f'What we see inside the function is {planck=} with {id(planck)=}')
print_universal()
planck
id(planck)
# %%
planck = 6.62e-34
def print_universal():
    global planck
    planck = 42
    print(f'What we see inside the function is {planck=} with {id(planck)=}')
print_universal()
print(f'What we see outside the function is {planck=} with {id(planck)=}')
# %%
planck = 6.62e-34
def print_universal():
    global planck
    planck = 42
    internal = 1
    print(locals())
    print(f'What we see inside the function is {planck=} with {id(planck)=}')
print_universal()
print(f'What we see outside the function is {planck=} with {id(planck)=}')
print(globals())
# %%
def dummy():
    '''
    Just a dummy function
    '''
    print(f'My name is: {dummy.__name__}')
    print(f'My docstring says: {dummy.__doc__}')
dummy()
# %%
def infinite():
    return infinite() # This will be trouble
infinite()
# %%
animals = ('dog', 'cat', ('pig', 'sheep', 'hen'), ('gorilla', ('monkey', 'baboon')))
# %%
def flatten(t1):
    for i in t1:
        print(f'Flattening {i} ...')
        if type(i) == tuple:
            for j in flatten(i):
                yield j
        else:
            print(f'nothing to flatten \n')
            yield i
tuple(flatten(animals))
# %%
def flatten(t1):
    for i in t1:
        print(f'Flattening {i} ...')
        if type(i) == tuple:
            yield from flatten(i)
        else:
            print(f'nothing to flatten \n')
            yield i
tuple(flatten(animals))
# %%
five_good_emperors = ('Nerva', 'Trajan', 'Hadrian', 'Antoninus', 'Marcus Aurelius')
position = 5
# five_good_emperors[position] # This will fail
try:
    five_good_emperors[position]
except:
    print(f'there were only {len(five_good_emperors)} good emperors, and you asked for the {position}th')
# %%
while True:
    value=input('Please provide the desired position, or press q to quit')
    if value == 'q':
        break
    try:
        position=int(value)
        print(five_good_emperors[position])
    except IndexError as error:
        print('Wrong index:', error)
    except Exception as error:
        print('Something else went wrong:', error)

# %%
