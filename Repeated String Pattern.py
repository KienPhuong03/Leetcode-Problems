# def repeatedSubstringPattern(s: str) -> bool:
#     current_pattern = ""
#     i = 0
#     while i < len(s):
#         if not current_pattern:
#             current_pattern += s[i]
#             i += 1
#             continue
#         l = len(current_pattern)
#         if s[i:i+l] == current_pattern:
#             i = i + l
#             print(f"pattern successfully matched, moving to index {i} next")
#             continue
#         else:
#             current_pattern += s[i]
#             print(f"pattern is not right, new pattern is {current_pattern}")
#             i += 1
#     return len(s) % len(current_pattern) == 0 and len(current_pattern) != len(s)

# print(repeatedSubstringPattern("abaababaab"))

def repeatedSubstringPattern(s: str) -> bool:
    def match(pattern, string):
        """
        if a string is entirely matched by this pattern, return True, otherwise return False
        """
        p = len(pattern)
        s = len(string)
        if not string: return True
        if string[:p] != pattern: return False
        else:
            return match(pattern, string[p:])

    current_pattern = ""
    i = 0
    while i < len(s):
        if not current_pattern:
            current_pattern += s[i]
            i += 1
            continue
        if match(current_pattern, s):
            return True
        else:
            current_pattern += s[i]
            i += 1
    return False


# def match(pattern, string):
#     """
#     if a string is entirely matched by this pattern, return True, otherwise return False
#     """
#     p = len(pattern)
#     s = len(string)
#     if not string: 
#         print(f"hit trivial base case when string is matched")
#         return True
#     if string[:p] != pattern: 
#         print(f"a part is not matched!")
#         return False
#     else:
#         print(f"recursive call")
#         return match(pattern, string[p:])
    
# print(match("ab", "abab"))

### Other Approach
def repeatedSubstringPattern(s: str) -> bool:
    return s in (s+s)[1:-1]