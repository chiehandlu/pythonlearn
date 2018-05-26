
"""
Names defined inside a def can only be seen by the code within that def.
You cannot even refer to such names from outside the function.
"""


# Global scope
x = 99
print('x =', x)
# 這邊的x是全局變量global scope
x += 1

print('x =', x)

def tryTest():
    z = x + 1
    print('z =', z)
# 這邊的z是局部變量local scope
tryTest()

def test():
    global x
# 表示這裡的x是global的x，所以global的x就被更改了
    x += 1
    # print('z =', z)

test()

print('x =', x)
