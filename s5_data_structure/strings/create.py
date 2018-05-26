

# Python Strings are Immutable objects that cannot change their values.

# You can update an existing string by (re)assigning a variable to another string.

# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals.

a = 'abcdefg'

print(a)

b = """ABCDEFG"""

print(b)

c = '''123456'''

print(c)

# \反斜線後面的字符表示其是屬於string中的一部分
d = 'doesn\'t'

print(d)

e = """This is the frist line
This is the second line
This is the third line
"""
# 如果有多行要換行，可以直接用""" asdkfs;f """三引號

print(e)

f = "abc\nABC"
# \反斜線+n 後面的string會換行

print(f)

# https://docs.python.org/3.5/tutorial/introduction.html#strings
