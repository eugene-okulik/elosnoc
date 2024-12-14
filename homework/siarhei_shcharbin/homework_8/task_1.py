import random


def give_me_a_bonus():
    bonus = bool(random.randint(0, 1))
    salary = int(input('What is your actual salary?:'))
    if bonus is True:
        new_salary = int(salary + salary * random.random())
    else:
        new_salary = salary
    print(salary, bonus, f'${new_salary}')


give_me_a_bonus()
