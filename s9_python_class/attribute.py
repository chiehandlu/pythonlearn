# class attribute and instance attribute

class Student(object):
    count = 0
# 運用class attribute來計算整體class運作過幾次
    def __init__(self, name):
        Student.count += 1
        self.name = name


s1 = Student('Jack')
s1.age = 30


print(s1.name)
print(s1.age)
print(Student.count)
# instance的attribute優先於class的attribute
s2 = Student('Tom')
s2.age = 20

print(s2.name)
print(s2.age)
print(Student.count)
