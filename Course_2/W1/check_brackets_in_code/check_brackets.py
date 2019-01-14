# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i + 1))
            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top[0], next[0]):
                    return i + 1
            pass
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][1]
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    '''
    for i in range(1, 55):
        with open('./tests/' + '{:02d}'.format(i), 'r') as inputt:
            text = inputt.readline()
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        with open('./tests/' + '{:02d}'.format(i) + '.a', 'r') as inputt:
            res = inputt.readline()
        #print(res.strip())
        #print(mismatch)
        if res.strip() != mismatch:
            print(i)
            print(res.strip())
            print(mismatch)
        print()
    '''


if __name__ == "__main__":
    main()
