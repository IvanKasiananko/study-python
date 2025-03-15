import abc
from itertools import product


class IObserver(metaclass=abc.ABCMeta):
    def update(self,p:int):
        pass

class IObservable(metaclass=abc.ABCMeta):
    def add_observer(self,o:IObserver):
        pass
    def remove_observer(self,o:IObserver):
        pass
    def notify(self):
        pass

class Product(IObserver):
    def __init__(self,price:int):
        self.__price=price
        self.__observer:List[IObserver]=[]

    def change_price(self,price:int):
        self.__price=price
        self.notify()

    def add_observer(self,o:IObserver):
        self.__observer.append(o)

    def remove_observer(self,o:IObserver):
        self.__observer.remove(o)

    def notify(self):
        for o in self.__observer:
            o.update(self.__price)

class Wholesale(IObserver):
    def __init__(self,obj:IObservable):
        self.__product=obj
        obj.add_observer(self)

    def update(self,p:int):
        if p<300:
            print('Оптовик закупил товар по цене {}'.format(p))
            self.__product.remove_observer(self)


class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 350:
            print('Покупатель закупил товар по цене {}'.format(p))
            self.__product.remove_observer(self)

product=Product(400)

wholesale=Wholesale(product)
buyer=Buyer(product)

product.change_price(320)
product.change_price(280)
