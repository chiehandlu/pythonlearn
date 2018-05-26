"""
It steps through the items of lists, tuples, strings, the keys of dictionaries and other iterables.
The Python for loop starts with the keyword "for" followed by an arbitrary variable name,
which will hold the values of the following sequence object, which is stepped through.

The general syntax looks like this:

for <variable> in <sequence>:
	<statements>
每次會從sequence中取出一個值，然後執行statement，直到取完最後一個值

"""

a = [1, 2, 3]
for x in a:
    print('x = ', x)
    print('yayaya')
print('Next example')

b = (4, 5, 6)

c = 'abc'
for i in c:
    print('i = ', i)
    print('yayaya')
print('Next example')

d = {1: 'a', 2: 'b'}
# 當sequence是dictionary時，取得的會是他的key
for i in d:
    print('i =', i)

print('done')

