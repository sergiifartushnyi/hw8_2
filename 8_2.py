import re

def is_palindrome(s: str) -> bool:

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    return cleaned == cleaned[::-1]

print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))

print("ОК")