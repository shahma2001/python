def compare(s1, s2, n):
    # Check if the first n characters of both strings are the same
    return s1[:n] == s2[:n]
print(compare("hello", "helicopter", 2))  # True
print(compare("hello", "world", 3))       # False
print(compare("abc", "abc", 3))           # True
print(compare("abc", "ab", 4))            # False


