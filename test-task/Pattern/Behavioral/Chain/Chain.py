import abc

class IWorker(metaclass=abc.ABCMeta):
    def set_next_worker(self,worker:'IWorker'):
        pass

    def execute(self,command:str):
        pass
class AbsWorker(IWorker):
    def __init__(self):
        self.__next_worker:IWorker=None

    def set_next_worker(self,worker:'IWorker'):
        self.__next_worker=worker
        return worker
    def execute(self,command:str):
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)
        return ''
class Designer(AbsWorker):
    def execute(self,command:str):
        if command=='спроектировать дом':
            return 'Проектировщик выполнил команду:'+command
        else:
            return super().execute(command)


class Carpentner(AbsWorker):
    def execute(self, command: str):
        if command == 'Класть кирпич':
            return 'Плотник выполнил команду:' + command
        else:
            return super().execute(command)


class FinishingWorker(AbsWorker):
    def execute(self, command: str):
        if command == 'Клеить обои':
            return 'Рабочий внутренней отделки выполнил команду:' + command
        else:
            return super().execute(command)

def give_command(worker:IWorker,command:str):
    string:str=worker.execute(command)
    if string=='':
        print(command+'-никто не умеет делать')
    else:
        print(string)

designer=Designer()
carpenter=Carpentner()
finishworeker=FinishingWorker()


designer.set_next_worker(carpenter).set_next_worker(finishworeker)
give_command(designer,'спроектировать дом')
give_command(designer,'Класть кирпич')
give_command(designer,'Клеить обои')

give_command(designer,'провести проводку')