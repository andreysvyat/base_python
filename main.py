from math import pi
import random
import utils
import utils.file_util
import fibo


def main():
    fibo.fib(15)
    utils.print_util.print_and_separate(fibo.fib2(10))
    utils.file_util.print_descriptor('.gitignore')
    print(random.randint(1, 6))
    print(pi)


if __name__ == '__main__':
    main()
