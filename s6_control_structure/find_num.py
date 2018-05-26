
"""
continue and break
"""

a = 1

while a < 100:
    if a % 2 == 0:
        a = a + 1
        continue
# 表示當a除以2的餘數為0時，直接進入到下個循環再從頭判斷，不繼續往下走
    print(a)
    a = a + 1

b = 1
while b < 100:
    if b % 13 ==0:
        break
    print(b)
    b = b + 1

for i in range(10):
    if i % 2:
        continue
# 表示i除以2如果餘數為0的話，是false，要繼續往下走，如果不為0的話是true，就可以進入到下個循環再從頭判斷，不繼續往下走
    print(i)