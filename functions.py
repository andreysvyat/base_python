from utils.print_util import separate_and_wait


def write_to_file(path, content):
    f = open(path, 'w')
    f.write(str(content))
    f.close()


def multiply(a, b):
    return a * b


write_to_file('new_text.txt', multiply(14, 222))

multiply_alias = multiply
print(multiply_alias)
print(multiply)
print(multiply_alias(2, 3))
print(multiply(2, 3))
separate_and_wait()


def call_back(operation, *args):
    print(operation)
    return operation(*args)


cbr = call_back(multiply, 14, 22)
print("14 * 22 = ", cbr)
separate_and_wait()


def summ(a, b): return a + b


def subtract(a, b): return a - b


def divide(a, b): return a / b


def select_operation(char):
    match char:
        case '*':
            return multiply
        case '+':
            return summ
        case '-':
            return subtract
        case ':':
            return divide


for c in '+*:-':
    do = select_operation(c)
    print(do.__name__ + " " + str(do(14, 10)))
separate_and_wait()

print(call_back(lambda x, y: x ** y, 43, 4))
print(call_back(lambda *args: print(*args, sep='\n'), 'first line', 'second line', call_back.__name__))
