from random import randint
# generate a number 1 - 10
answer = randint(1, 10)

# input from user
# check that input is a num from 1-10
# check the num is correct guess else ask again
while True:
    try:
        print(answer)
        guess = int(input('guess number between 1-10: '))

        if 0 < guess < 11:
            if guess == answer:
             print("you are a genius")
             break
        else:
            print('Hey bozo, I said 1-10')
    except ValueError:
        print("please enter a number")
        continue

