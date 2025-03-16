import abc

class IVisitor(metaclass=abc.ABCMeta):
    def visit(self,place:'IPlace'):
        pass

class IPlace(metaclass=abc.ABCMeta):
    def accept(self,visitor:IVisitor):
        pass

class Zoo(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)

class Cinema(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)

class Circus(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)

class HolidayMarker(IVisitor):
    def __init__(self):
        self.value=''

    def visit(self,place:IPlace):
        if isinstance(place,Zoo):
            self.value='Слон в зоопарке'
        elif isinstance(self,Cinema):
            self.value='Властелин колец'
        elif isinstance(place,Circus):
            self.value=('Клоун в цирке')

places: list[IPlace]=[Zoo(),Circus(),Cinema()]
for place in places:
    visitor=HolidayMarker()
    place.accept(visitor)
    print(visitor.value)