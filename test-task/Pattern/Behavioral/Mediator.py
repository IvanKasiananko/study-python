import abc

class IMediator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self,emp:'Employee',msg:str):
        pass

class Employee(metaclass=abc.ABCMeta):
    def __init__(self,mediator:IMediator):
        self.mediator=mediator

    def set_mediator(self,med:IMediator):
        self._mediator=med

class Designer(Employee):
    def __init__(self,med:IMediator=None):
        super().__init__(med)
        self.__is_working=False

    def execute_work(self):
        print('<-Дизайнер в работе')
        self._mediator.notify(self,'Дизайнер проектирует ...')

    def set_work(self,state:bool):
        self.__is_working=state
        if state:
            print('Дизайнер освобожден от работы')
        else:
            print('<-Дизайнер занят')

class Director(Employee):
    def __init__(self,med:IMediator=None):
        super().__init__(med)
        self.__text:str=None

    def give_command(self,txt:str):
        self.__text=txt
        if txt=='':
            print('->Директор знает что дизайнер уже работает')
        else:
            print('->Директор дал команду:'+txt)
        self._mediator.notify(self,txt)

class Controller(IMediator):
    def __init__(self,designer:Designer,director:Director):
        self.__designer=designer
        self.__director=director
        designer.set_mediator(self)
        director.set_mediator(self)

    def notify(self,emp:'Employee',nsg:str):
        if isinstance(emp,Director):
            if nsg=='':
                self.__designer.set_work(False)
            else:
                self.__designer.set_work(True)
        if isinstance(emp,Designer):
            if nsg=='Дизайнер проектирует':
                self.__director.give_command('')

designer=Designer()
director=Director()

mediator=Controller(designer,director)
director.give_command('Проектировать')
print()
designer.execute_work()

