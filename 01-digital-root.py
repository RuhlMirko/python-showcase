def digital_root(n):
    while n >= 10:
        print(int(digit) for digit in str(n))
        n = sum(int(digit) for digit in str(n))
    return n

test_data = [16, 942, 132189, 493193]
for i in test_data:
    print(f'The digital root of {i} is: {digital_root(i)}')

