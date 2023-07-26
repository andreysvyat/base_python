def outer():
    n = 5

    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner


fn = outer()
fn()
fn()
fn()


def trace_func_call(f):
    def decorator(*args, **kwargs):
        print('***************************')
        print('function name = ' + f.__name__)
        print('positional args = ' + str(args))
        print('named args = ' + str(kwargs))
        result = f(*args, **kwargs)
        print('result is ' + str(result))
        print('***************************')
        return result
    return decorator


@trace_func_call
def do_stuff():
    print("Stuff is done")


@trace_func_call
def calculate_some(a, b):
    return a + b


do_stuff()
calculate_some(15, b=22)
