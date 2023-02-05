n = int(input())


def isPalindrome(param):
    return param == param[::-1]


def isPseudoPalindrome(string):
    for i in range(len(string)):
        if string[i] != string[-i - 1]:
            return isPalindrome(string[:i] + string[i + 1:]) or isPalindrome(
                string[:len(string) - i - 1] + string[len(string) - i:])
    return False


for _ in range(n):
    string = input()
    if isPalindrome(string):
        print(0)
    elif isPseudoPalindrome(string):
        print(1)
    else:
        print(2)
