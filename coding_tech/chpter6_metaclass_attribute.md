# 목록
1. [BetterWay44. ]()
2. [BetterWay45. 애트리뷰트를 리팩터릴하는 대신 @property를 사용해라](#betterway45-애트리뷰트를-리팩터릴하는-대신-property를-사용해라)
3. [BetterWay46. 재사용 가능한 @property 메서드를 만들려면 디스크립터를 사용해라.](#betterway45-애트리뷰트를-리팩터릴하는-대신-property를-사용해라)
4. [BetterWay47. 지연 계산 애트리뷰트가 필요하면 __getattr__, __getattribute__, __setattr__ 을 사용하라.](#betterway47-지연-계산-애트리뷰트가-필요하면-getattr-getattribute-setattr-을-사용하라)
5. [BetterWay48. __init_subclass__를 사용해 하위 클래스를 검증하라.](#betterway48-__init_subclass__를-사용해-하위-클래스를-검증하라)
6. [BetterWay49. __init_subclass__를 사용해 클래스 확장을 등록하라.](#betterway49-__init_subclass__를-사용해-클래스-확장을-등록하라)
7. [BetterWay50. __set_name__으로 클래스 애트리뷰트를 표시하라.](#betterway50-__set_name__으로-클래스-애트리뷰트를-표시하라)
8. [BetterWay51. 합성 가능한 클래스 확장이 필요하면 메타클래스보다는 클래스 데코레이터를 사용하라.](#betterway51-합성-가능한-클래스-확장이-필요하면-메타클래스보다는-클래스-데코레이터를-사용하라)

# Chapter6 : 메타클래스와 애트리뷰트

- 메타클래스
    - 파이썬의 class 문을 가로채서 클래스가 정의될 때마다 특별한 동작을 제공할 수 있다.

- 기능
    - 동적으로 애트리뷰트 접근을 커스텀화

- 함정
    - 동적 애트리뷰트로 객체를 오버라이드하면 부작용.. ? 어떤?


## BetterWay44. 세터와 게터 메서드 대신 평범한 애트리뷰트를 사용해라

- 애트리뷰트를 얻고 저장하는 함수 게터, 세터 함수
    - 이렇게 사용하면 python답지 않은 코드가 됨
    - 그냥 애트리뷰트를 사용하면 됨
    - 애트리뷰트를 사용하면 애트리뷰트에 대한 연산이 훨씬 자연스럽다.
```python
## 게터/세터: 파이썬 답지 않음
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


## 그냥 애트리뷰트 활용. 심플!
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms = 50e3
```

- 만일 애트리뷰트가 설정될 때 특별한 기능을 수행해야 한다면, 애트리뷰트를 `@property` 데코레이터와 대응하는 setter 애트리뷰트로 옮겨갈 수 있다.
    - 이런 식으로 setter를 지정하면 어트리뷰트에 값이 set 될때 추가 작업을 할 수 있다.

```python
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


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
```

- `@property`의 setter로 입력 값의 유효성 검사
```python
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
r3.ohms= 0 # ValueError: 저항 > 0 이어야 합니다. 입력값: 0
```

- `@property`로 부모 클래스에 정의된 애트리뷰트르 불변으로 구현
```python
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
r4.ohms = 2e3 # AttributeError: Ohms는 불변 객체. 한번만 초기화됨
```

- 게터 프로퍼티 메서드에서 다른 애트리뷰트를 설정하면 코드가 아주 이상하게 동작할 수 있다.
```python
## 주의해야 할 예제
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
```

- getter, setter를 정의할 때 가장 좋은 정책
    - 관련이 있는 객체 상태를 @property.setter 메서드 안에서만 변경하는 것
        - 동적인 모듈 임포트, I/O작업, 대기시간이 긴 DB질의 등 은 피하기.
    - 복잡하거나 느린 연산의 경우에는 일반 메서드로 구현한다.

- `@property`의 가장 큰 단점
    - 애트리뷰트를 처리하는 메서드가 하위 클래스 사이에서만 공유됨
    - 서로 관련없는 클래스 사이에 같은 프로퍼티 구현을 공유할 수 없음
    - 다른 클래스에 재사용할 프로퍼티는 `디스크립터`를 제공함

### 기억해야 할 Point
> - 새로운 클래스 인터페이스를 정의할 때는 간단한 공개 애트리뷰트에서 시작하고, 세터/게터 메서드는 가급적 사용하지 말자<br>
> - 객체에 있는 애트리뷰트에 접근할 때, 특별한 동작이 필요하면 `@property`로 이를 구현할 수 있다.<br>
> - `@property` 메서드를 만들 때는 최소 놀람의 법칙을 다른다.<br>
> - `@property` 메서드가 빠르게 실행되도록 유지한다.<br>

<br>

## BetterWay45. 애트리뷰트를 리팩터릴하는 대신 @property를 사용해라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay46. 재사용 가능한 @property 메서드를 만들려면 디스크립터를 사용해라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay47. 지연 계산 애트리뷰트가 필요하면 __getattr__, __getattribute__, __setattr__ 을 사용하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay48. __init_subclass__를 사용해 하위 클래스를 검증하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay49. __init_subclass__를 사용해 클래스 확장을 등록하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay50. __set_name__으로 클래스 애트리뷰트를 표시하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay51. 합성 가능한 클래스 확장이 필요하면 메타클래스보다는 클래스 데코레이터를 사용하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>
