import abc

class State(metaclass=abc.ABCMeta):

    def __init__(self):
        self._traffic_ligth:'TrafficLigth'=None

    def next_state(self):
        pass

class TrafficLigth:
    def __init__(self,st:State):
        self.set_state(st)

    def set_state(self,st:State):
        self.__state=st
        self.__state._traffic_ligth=self

    def next_state(self):
        self.__state.next_state()

    def previouse_state(self):
        self.__state.previouse_state()

class GreenState(State):
    def next_state(self):
        print('Из зеленого в желтый')
        self._traffic_ligth.set_state(YellowState())

    def previouse_state(self):
         print('Зеленый цвет')

class YellowState(State):
    def next_state(self):
        print('Из желтого в красный')
        self._traffic_ligth.set_state(RedState())

    def previouse_state(self):
        print('Из желтого в зеленый цвет')
        self._traffic_ligth.set_state(RedState())

class RedState(State):
    def next_state(self):
        print('Красный цвет')

    def previouse_state(self):
        print('Из красного в желтый')
        self._traffic_ligth.set_state(YellowState())

traffic_ligth=TrafficLigth(YellowState())
traffic_ligth.next_state()
traffic_ligth.next_state()
traffic_ligth.previouse_state()
traffic_ligth.previouse_state()
traffic_ligth.previouse_state()