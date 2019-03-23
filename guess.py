

secret=9
i=1
while i<=3:
 guess = int(input('Guess: '))
 if guess== secret:
    print('You win!')
    i=4
 else:
    i+=1