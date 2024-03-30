# 44

class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms
    
    def get_ohms(self):
        return self._ohms
    
    def set_ohms(self, ohms):
        self._ohms = ohms
        

r0 = OldResistor(50e3)
print("이전: ", r0.get_ohms())  # 이전:  50000.0
r0.set_ohms(10e3)
print("이후: ", r0.get_ohms())  # 이후:  10000.0





class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print(f'이전: {r2.current: .2f} 암페어') # 이전:  0.00 암페어
r2.voltage = 10
print(f'이전: {r2.current: .2f} 암페어') # 이전:  0.01 암페어



class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        
    @property
    def ohms(self):
        return self._ohms
    
    ## 잘못된 값 입력이 에러 발생하도록.
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0 이어야 합니다. 입력값: {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
# r3.ohms= 0 # ValueError: 저항 > 0 이어야 합니다. 입력값: 0


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
    
    @property
    def ohms(self):
            return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError('Ohms는 불변 객체. 한번만 초기화됨')

        self._ohms = ohms

r4 = FixedResistance(1e3)
# r4.ohms = 2e3 # AttributeError: Ohms는 불변 객체. 한번만 초기화됨

class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'이전: {r7.voltage: .2f}')   # 이전:  0.00

r7.ohms
print(f'이후: {r7.voltage: .2f}')   # 이전:  0.00


이후:  0.10