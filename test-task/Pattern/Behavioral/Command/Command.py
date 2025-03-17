import abc

class ICommand(metaclass=abc.ABCMeta):
    def positive(self):
        pass
    def negative(self):
        pass

class Conveyor:
    def on(self):
        print("Конвейер запущен")

    def off(self):
        print("Конвеер остановлен")

    def speed_increase(self):
        print('Увеличена скорость конвеера')

    def speed_decreasa(self):
        print('Сниженна скорость конвеера')

class ConveyorWorkCommand(ICommand):
    def __init__(self,conveyor:Conveyor):
        self.conveyor:Conveyor=conveyor
    def positive(self):
        self.conveyor.on()
    def negative(self):
        self.conveyor.off()

class ConveyorAdjustCommand(ICommand):
    def __init__(self,conveyor:Conveyor):
        self.conveyor:Conveyor=conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decreasa()

class Multipult:
    def __init__(self):
        self.__commands:List[ICommand]=[None,None]
        self.__history:Deque[ICommand]=[]

    def set_command(self,button:int,command:ICommand):
        self.__commands[button]=command

    def press_on(self,button:int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        if len(self.__history)!=0:
            self.__history.pop().negative()

conveyor=Conveyor()
multipult=Multipult()
multipult.set_command(0,ConveyorWorkCommand(conveyor))
multipult.set_command(1,ConveyorAdjustCommand(conveyor))

multipult.press_on(0)
multipult.press_on(1)
multipult.press_cancel()
multipult.press_cancel()