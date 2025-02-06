

def duplicate_count(text):
    count = 0
    char_list = [Char for Char in text]
    s = set()
    d = set()

    for (char) in char_list:
        char = char.lower()
        if char in s and char not in d:
            count += 1
            d.add(char)
        else:
            s.add(char)
    return count

test_data = ['','abcde','abcdeaa','abcdeaB','Indivisibilities']
for i in test_data:
    print(f'Amount of dupes in <{i}> is: {duplicate_count(i)}')