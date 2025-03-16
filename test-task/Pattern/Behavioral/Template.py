import abc

class Transmitter(metaclass=abc.ABCMeta):
    def _voice_record(self):
        print('Запись фрагмента речи')

    def _simpling(self):
        pass
    def _digitalization(self):
        pass

    def _modulation(self):
        pass
    def _transmission(self):
        print('Передача сигнала по радиоканалу')

    def process_start(self):
        self._voice_record()
        self._simpling()
        self._digitalization()
        self._modulation()
        self._transmission()

class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print('Модуляция аналогового сигнала')

class DigitTransmitter(Transmitter):
    def _simpling(self):
        print('Дискретизация записанного фрагмента')

    def _digitalization(self):
        print('Оцифровка')

    def _modulation(self):
        print('Модуляция цифрового сигнала')

analog_transmiter=AnalogTransmitter()
analog_transmiter.process_start()

print()

digit_transmiter=DigitTransmitter()
digit_transmiter.process_start()
