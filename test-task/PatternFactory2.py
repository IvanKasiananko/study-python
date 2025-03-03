class Product:
    def release(self):
        pass

class Car(Product):
    def release(self):
        print('Выпущен легковой автомобиль')

class Track(Product):
    def release(self):
        print('Выпущен грузовой автомобиль')

class WorkCar:
    def create(self):
        pass

class ShopCar(WorkCar):
    def create(self):
        return Car()

class ShopTrack(WorkCar):
    def create(self):
        return Track()


creator=ShopCar()
car = creator.create()

creator = ShopTrack()
track = creator.create()
car.release()
track.release()
