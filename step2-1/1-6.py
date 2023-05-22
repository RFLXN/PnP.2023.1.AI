from math import floor


def is_palindrome(word):
    is_pal = False
    for c in range(floor(len(word) / 2)):
        front = word[c]
        back = word[-c - 1]
        is_pal = front == back
    return is_pal


# 테스트 코드
print(is_palindrome("racecar"))     # True
print(is_palindrome("stars"))       # False
print(is_palindrome("토마토"))       # True
print(is_palindrome("kayak"))       # True
print(is_palindrome("hello"))       # False
