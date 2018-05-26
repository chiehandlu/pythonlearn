# instance method and class method


class A(object):

    @classmethod
    def test(cls, y):
        pass

    # Instance method
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        self.test(x)
# instance method 只能調用同樣是instance 的 method
    # class method
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        cls.test(x)

# class method 只能調用同樣是class 的 method

    # static method
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
# static method不能調用其他的method