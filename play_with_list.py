import random

words = ['alibaba', 'master', 'shadow', 'internal']
nums = random.sample(population=range(100), k=10)
people = [
    {'name': 'Alex', 'age': 25},
    {'name': 'Ruth', 'age': 15},
    {'name': 'Alice', 'age': 82},
    {'name': 'John', 'age': 32},
    {'name': 'April', 'age': 12}
]

[print(line) for line in words]
print([x ** 5 for x in nums if x % 2 == 0])
[print(adult) for adult in people if adult['age'] >= 18]
print(*people, sep='\n')
print('test', 'some', 'print')
print(people)
u_people = tuple(people)
ax, r, ae, j, al = people
print(ae)
