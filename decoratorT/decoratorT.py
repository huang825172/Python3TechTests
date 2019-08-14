def setTag(tag):
    def decoratorT(func):
        def wrapperT(*arg, **kvargs):
            sign = '<' + tag + '>'
            return sign + func(*arg, **kvargs) + sign

        return wrapperT

    return decoratorT


def mD(func):
    def wrap(*arg, **kvargs):
        return "kksk " + func(*arg, **kvargs)

    return wrap


def newEat(newCls):
    class newEatCls():
        def __init__(self, food, water):
            self.new = newCls(food)
            self.water = water

        def __priv(self):
            print("launch from inner")

        def display(self):
            print("lunch " + self.new.food + " with " + self.water)
            self.__priv()

    return newEatCls


@newEat
class eat(object):
    def __init__(self, food):
        # super(object, self).__init__()
        self.food = food

    def display(self):
        print("lunch " + self.food)


@setTag("div")
@mD
def hello(name):
    e = eat("rice", "milk")
    e.display()
    return "hello " + name
