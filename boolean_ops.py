from utils import separate_and_wait

print('How works "not" on constant True and False')
print(not True)
print(not False)
separate_and_wait()

print('How works "or" on constant True and False')
print(True or True)
print(True or False)
print(False or True)
print(False or False)
separate_and_wait()

print('How works "and" on constant True and False')
print(True and True)
print(True and False)
print(False and True)
print(False and False)
separate_and_wait()

t = True
f = False

print(f'Lets test how "not" works on variables t = {t} nad f = {f}')
print(not t)
print(not f)
separate_and_wait()

print(f'Lets test how "or" works on variables t = {t} nad f = {f}')
print(t or t)
print(t or f)
print(f or t)
print(f or f)
separate_and_wait()

print(f'Lets test how "and" works on variables t = {t} nad f = {f}')
print(t and t)
print(t and f)
print(f and t)
print(f and f)
separate_and_wait()


def how_comparing_operators_works():
    x: int = int(input())
    y: int = int(input())
    print(f'is {x} not equals {y}? - {x != y}')
    print(f'is {x} greater {y}? - {x > y}')
    print(f'is {x} less {y}? - {x < y}')
    print(f'is {x} equals or greater {y}? - {x >= y}')
    print(f'is {x} equals or less {y}? - {x <= y}')
    print(f'is {x} equals {y}? - {x == y}')


while input('need more? (y/n):') == 'y':
    how_comparing_operators_works()
