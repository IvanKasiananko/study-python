from abc import ABCMeta,abstractmethod

class IEngine(metaclass=ABCMeta):
    def release_engine(self):
        pass
    
class  JapanesEngine(IEngine):
    def release_engine(self):
        print("Японский двигатель")

class  AmericanEngine(IEngine):
    def release_engine(self):
        print("Американский двигатель")

class ICar(metaclass=ABCMeta):
    def release_car(self,engine:IEngine):
        pass

class JapaneseCar(ICar):
    def release_car(self,engine:IEngine):
        print("Собрали японский автомобиль")
        engine.release_engine()

class AmericanCar(ICar):
    def release_car(self,engine:IEngine):
        print("Собрали американский  автомобиль")
        engine.release_engine()

class IFactory(metaclass=ABCMeta):
    def create_engine(self):
        pass
    def create_car(self):
        pass

class JapaneseFactory(IFactory):
    def create_engine(self):
        return  JapanesEngine()
    def create_car(self):
        return JapaneseCar()

class AmericanFactory(IFactory):
    def create_engine(self):
        return  AmericanEngine()
    def create_car(self):
        return AmericanCar()

j_factory=JapaneseFactory()
j_engine=j_factory.create_engine()
j_car=j_factory.create_car()
j_car.release_car(j_engine)

a_factory=AmericanFactory()
a_engine=a_factory.create_engine()
a_car=a_factory.create_car()
a_car.release_car(a_engine)


