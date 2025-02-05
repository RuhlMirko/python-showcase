

n = input('Enter a number: ')
while n!=0:
    rootResult = 0

    for i, item in enumerate(n):
        print(n[i])

    print(f'The digital root is {rootResult} ')
    n = input('Enter a new number: ')