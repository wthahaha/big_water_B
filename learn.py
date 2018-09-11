# encoding: utf-8

import inspect # 判断是否是某类对象 如：inspect.isfunction(fun1)


class Dog(object):
    c = 2
    def __init__(self, age):
        print('__init__ 自动输出')
        self.age = age
    # 重写__getattribute__。需要注意的是重写的方法中不能
    # 使用对象的点运算符访问属性，否则使用点运算符访问属性时，
    # 会再次调用__getattribute__。这样就会陷入无限递归。
    # 可以使用super()方法避免这个问题。

    def default_func(self):
        # 默认函数
        print('default func', self.age)

    def __getattribute__(self, key):
        # 访问类的每个属性和方法时，都会先执行内置的__getattribute__方法，这里重写本方法，
        # 如果在调用不存在的方法时，会自动调用指定的方法
        try:
            return super(Dog, self).__getattribute__(key)
        except:
            return super(Dog, self).__getattribute__('default_func')

    def sound(self):
        print("wang wang~")

    def __call__(self, *args, **kwargs):
        print("直接调用实例化对象")


a = Dog(1) # __init__ 自动输出
a()  # 调用__call__函数，输出：直接调用实例化对象
a.sound()  # wang wang~
a.ssss()  # ssss函数不存在，输出： default func 1


def rrr(l=[]):
    l.append(1)
    print(l)

rrr()
rrr()

############含有二个装饰器#########

def outer0(func):#第一个
    def inner(*args, **kwargs):
        print("AAAAAAAAA")
        r = func(*args, **kwargs)
        print("BBBBBBBB")
        # return r
    return inner

def outer(func):  #第二个
    def inner(*args, **kwargs):#要装饰f1（），这里用这俩形式参数，可以接受任意个参数，不管f1定义几个参数
        print("1")
        r = func(*args, **kwargs)#这里要用func，不要用f1
        print("2")
        # return r
    return inner
@outer0  #俩装饰器，流程就是：执行f1()的时候，先执行outer0.inner(),outer0.inner().func调用outer的inner函数（即：将outer0.inner().func替换为outer.inner()），也就是outer.inner()函数作为outer0的参数，
         # 然后outer.inner().func再调用f1()（即：将outer.inner().func替换为f1()）
@outer  #这里outer不要加括号
def f1(a1, a2):
    print("a1 + a2 = %d" %(a1+a2))
    return 1

f1(1,2)


