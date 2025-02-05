# def digital_root(n):
#     digit_len = len(str(n))
#     digit_str = str(n)
#     rootResult = 0
#     while digit_len > 1:
#         for i, item in enumerate(digit_str):
#             rootResult += int(digit_str[i])
#         digit_str = str(rootResult)
#         digit_len = len(digit_str)
#         rootResult = 0

def digital_root(n):
    digit_len = len(str(n))
    digit_str = str(n)
    rootResult = 0
    while digit_len > 1:
        for i, item in enumerate(digit_str):
            rootResult += int(digit_str[i])
        digit_str = str(rootResult)
        digit_len = len(digit_str)
        rootResult = 0
    return int(digit_str)



print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
digital_root(493193)
