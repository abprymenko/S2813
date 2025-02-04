from iteratorcounter import Counter
from generator import Generator
from callobject import Helper
from decorator import Calculator

#what is iterable objects?
#students = [["Student_Name0", 15, True], ["Student_Name1", 17, False], ["Student_Name2", 16, False]]
#1 Iterate by for loop
'''
for loops automatically create an iterator behind the scenes when looping over a collection.
These types can be looped over with a for loop:
	1.	Sequences: str, list, tuple, range;
	2.	Collections: set, frozenset, dict (iterates over keys by default);
	3.	Custom Iterators: any object with an __iter__() or __getitem__() method;
	4.	Generators and Generator Expressions.
'''
'''
for student in students:
    print(student)
'''
#2 Iterate by while loop
#2.1 without the iter() method
'''
i = 0
while i < len(students):
    print(students[i])
    i += 1
'''
#2.2 with only the next() method
'''
while True:
    print(next(students))#TypeError: 'list' object is not an iterator
print("Hello Iterators")
'''
#2.3 with the next() and the iter() methods
'''
iter_students = iter(students)
while True:
    try:
        print(next(iter_students))
    except StopIteration:
        break
print("Hello Iterators")
'''

#3 Iterator -> Counter
#counter = Counter(25, 40)
#3.1 for
'''
for i in counter:
    print(i)
'''
#3.2 while
'''
try:
    while(True):
        print(next(counter))
except StopIteration:
    pass
'''

#4 Generator :: yield
#generator = Generator(students)
#4.1 for
'''
for i in generator:
    print(i)
'''
#4.2 while
'''
i=0
while True:
    try:
        print(generator[i])
        i += 1
    except IndexError:
        break
'''

#5 Closures
'''
def HelperFunc(work):
    #Data Encapsulation: Closures provide a way to encapsulate data within a function, 
    #limiting its visibility and accessibility from outside.
    work_in_memory = work
    def HelperInnerFunction(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return HelperInnerFunction
#stores pointer to HelperInnerFunction()
helper = HelperFunc("homework")#<function HelperFunc.<locals>.HelperInnerFunction at 0x00000230E2FA4B80>
print(helper("cleaning"))# f"I will help you with your homework. Afterwards I will help you with cleaning"
print(helper("driving"))# f"I will help you with your homework. Afterwards I will help you with driving"
'''
#5 Closures :: __call__(param) objects
'''
helper = Helper("homework")
print(helper("cleaning"))
print(helper("driving"))
'''
#6 Decorator
'''
try:
    calculator = Calculator()
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    operation = input("Select operation[/*-+]: ")
    res = calculator.Calculate(f'{digit1}{operation}{digit2}')
    print(res)
    print("No exception")
except Exception as ex:
    print(ex)
'''