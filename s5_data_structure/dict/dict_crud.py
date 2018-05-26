

d = {
    'Name': 'Jood',
    'Age': 9,
    'Grade': 5,
}


print("dict['Age'] =", d['Name'])
print("dict['Age'] =", d['Age'])


print(d.keys())

print(d.values())

print(d.get('Name'))
# get方法當所找的是不存在的key，不會報錯，只會回傳沒有(None)
# 一般直接用[]的話，如果找的是不存在的key，會報錯
del d['Name']
print(d)

d.clear()
print(d)
