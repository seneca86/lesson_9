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
        print('this is None')
    elif what:
        print('this is something')
    else:
        print('this is False')
check_nones(None)
check_nones(42)
check_nones(False)
# %%
