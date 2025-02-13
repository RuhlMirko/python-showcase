titleProject = 'Sum of Digits / Digital Root'
summaryProject = '''
Description:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until 
a single-digit number is produced. The input will be a non-negative integer.'''


def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


# test_data = [16, 942, 132189, 493193]
# for i in test_data:
#     print(f'The digital root of {i} is: {digital_root(i)}')


def printData():
    titleProject = 'Sum of Digits / Digital Root'
    summaryProject = '''
    Description:
    Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until 
    a single-digit number is produced. The input will be a non-negative integer.'''
    test_data = [16, 942, 132189, 493193]
    result_data = ', '.join(map(str, (digital_root(i) for i in test_data)))
    full_str = f"Test Data: {', '.join(map(str, test_data))}\nResult Data: {result_data}"

    allData = [titleProject, summaryProject, full_str]
    return allData
