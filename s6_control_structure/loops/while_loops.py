
"""
A while loop statement in Python programming language repeatedly executes a target statement
as long as a given condition is true.

Syntax
The syntax of a while loop in Python programming language is −

while expression:
   statement(s)

當while後面的expression是true的時候，就會執行下面的statement，
執行完後會再重覆判斷espression是否為true，若true的話，就重覆執行
直到espression為fulse，才會停止

Here, statement(s) may be a single statement or a block of statements.

The condition may be any expression, and true is any non-zero value.

The loop iterates while the condition is true.

When the condition becomes false, program control passes to the line immediately following the loop.
"""

a = 10
while a > 0:
    print('a =', a)
    a = a - 1
# 如果沒有 a = a - 1 這行，那他就會無限循環，只能自行中止
print('finished')