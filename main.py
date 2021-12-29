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
