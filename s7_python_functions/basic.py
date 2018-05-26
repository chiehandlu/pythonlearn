

"""
The def header line specifies a function name that is assigned the function object,
along with a list of zero or more arguments (sometimes called parameters) in parentheses.
The argument names in the header are assigned to the objects passed in parentheses at the point of call.


Function bodies often contain a return statement:

def <name>(argument1, arg2,... argN): ...
    return <value>
"""


# Definition
def sum(a, b):
    c = a + b
    print(c)

# calls
d = sum([1, 2], [3, 4])
print(d)
# 顯示出來的值是在function中直接執行的
# 直接print(d)會顯示None

def sum(a, b):
    c = a*a + b*b
    return c

d = sum (1, 2)
print(d)
# 加上return後才會賦予d一個值，這時print出來的會有東西，而不是None