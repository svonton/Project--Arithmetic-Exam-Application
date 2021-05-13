import random as r
import math as m
possible_operation = ['+','-','*']
task_list = [str(r.randrange(2, 10))+r.choice(possible_operation)+str(r.randrange(2, 10)) for x in range(5)]
task_list_hard = [r.randrange(11, 30) for x in range(5)]
invite_messege = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n"""
level_descriptions = ['simple operations with numbers 2-9','integral squares 11-29']
while True:
    try:
        decision = int(input(invite_messege))
        if decision in [1,2]:
            break
    except:
        print("Incorrect format.")

score = 0
def ez_level(i):
    global score
    right_answer = eval(task_list[i])
    print(task_list[i])
    if int(input()) == right_answer:
        print('Right!')
        score += 1
    else:
        print('Wrong!')

def hard_level(i):
    global score
    right_answer = task_list_hard[i]**2
    print(task_list_hard[i])
    if int(input()) == right_answer:
        print('Right!')
        score += 1
    else:
        print('Wrong!')

for i in range(5):
    while True:
        try:
            if decision == 1:
                ez_level(i)
            else:
                hard_level(i)
            break
        except:
            print("Incorrect format.")
print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.\n")
need_save = str(input())
if need_save in ['yes','YES','y','Yes']:
    name = str(input('What is your name?\n'))
    with open('results.txt','a') as f:
        f.write(f'{name}: {score}/5 in level {decision} ({level_descriptions[decision-1]})')
    print('The results are saved in "results.txt".')


