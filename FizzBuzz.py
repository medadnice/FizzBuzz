# set counter variable
i = 0
occured = []
for x in range(1, 101):

    # check numbers against modulo and display value of X
    if x % 3 == 0 and x % 5 == 0:
        number = str(x)
        occured.append(number)
        print(number + ': ' + 'FizzBuzz')
        i = i + 1

    elif x % 3 == 0:
        number = str(x)
        print(number + ': ' + 'Fizz')

    elif x % 5 == 0:
        number = str(x)
        print(number + ': ' + 'Buzz')

    # Print numbers generated that fail to meet conditions
    else:
        print(x)


print("")
print('FizzBuzz occured ' + str(i) + ' times!')
print('At these numbers ',  occured)
print('BAZINGA!')
