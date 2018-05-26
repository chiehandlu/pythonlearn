# class definition
# class可以是一個抽象的數據集合，它可以是不存在的，像是"水果"


class MyClass:
    pass

my_class = MyClass()
# 運用my_class實例化MyClass，將MyClass賦予給my_class

# The __init__() Method
# 在class裡面定義的function稱為method
# class裡面有兩個重要的元素：attributes屬性和methods方法
# attributes屬性:像是下面例子class People 中的 name, age


class People:

    def __init__(self, name, age):
#  __init__為class初始化的一個函數，而所有method的第一個參數一定叫self, self代表class本身，後面才接其他參數
        self.__name = name
# 第一個name代表class People中name這個instance的attribute，後面的name則是給予的參數，這個參數賦予前面的attribute一個值
        self.__age = age

    def sayhi(self):
# 這個method只有一個默認的參數self
        print("Hi, my name is %s, and I'm %s" % (self.__name, self.__age))
# 我們可以透過self.name或self.age去訪問其他method的attribute之value

    def get_age(self):
        return self.__age

    def set_age(self, num):
        if isinstance(num, int):
            if num > 0:
                self.age = num
                return
        print('format error')


# class instance 將class實例化

someone = People(name='Jack', age=20)
# 實例化People這個class叫做someone, 20就是age這個instance的attribute
# print(someone.get_age())
someone.set_age(num=30)
print(someone.sayhi())
# print(someone.get_age())