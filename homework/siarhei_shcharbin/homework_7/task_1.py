num = 7
input('Please guess the number:')
while True:
    if int(input()) != num:
        print('Please try again:')
        continue
    else:
        print('Congratulations! You have guessed right!')
        break
