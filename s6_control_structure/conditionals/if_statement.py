
# In Python, True and False are Boolean objects of class 'bool' and they are immutable.
# Python assumes any non-zero and non-null values as True, otherwise it is False value.
# Python does not provide switch or case statements as in other languages.


# if statement

x = int(input('please enter an integer: '))
# x = int(.......)表示將裡面的東西轉換為int
# input(.......)用來表示要在terminal中輸入東西，而裡面的...是提示，顯示要打什麼進去，可為數字或string
# 在這例子裡面只能打數字，如果打string，會報錯
if x < 0:
# if語句後面記得加:
    print('negative number')

# if..else statement

y = int(input('please enter an integer: '))
if y < 0:
    print('negative number')
else:
    print('positive number')

# if...elif...else statement

y = int(input('please enter an integer: '))
if y < 0:
    print('negative number')
elif y > 0:
    print('positive number')
else:
    print('zero')

# if...elif...else statement 當中的elif可重覆運用

y = int(input('please enter an integer: '))
if -5< y < 0:
    print('0 to -5')
elif y > 0:
    print('positive number')
elif y < -5:
    print('small than -5')
else:
    print('zero')