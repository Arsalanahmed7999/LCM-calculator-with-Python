def lcmCalculator(num1, num2):
    res1 = []
    res2 = []
    # we will be appending the values in these above lists (multiple of these numbers).

    n = max(num1, num2)

    i = 1
    while(n>=i):
        res1.append(num1 * i)
        res2.append(num2 * i)
        i+=1
    
    # return res1 #[5, 10, 15, 20, 25, 30, 35, 40, 45]
    # return res2 # [9, 18, 27, 36, 45, 54, 63, 72, 81]

    myList = set(res1).intersection(res2)
    return min(myList)


while True:
    number1 = int(input('Enter the value of number 1: \n'))
    number2 = int(input('Enter the value of number 2: \n'))
    print(f'LCM of {number1} and {number2} is {lcmCalculator(number1, number2)}')
    userWantstoContinue = input('You want to continue? (yes/no): \n')
    if userWantstoContinue == 'no':
        break




