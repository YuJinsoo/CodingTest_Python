# 목록
1. [BetterWay44. ]()
2. [BetterWay45. 애트리뷰트를 리팩터릴하는 대신 @property를 사용해라](#betterway45-애트리뷰트를-리팩터릴하는-대신-property를-사용해라)
3. [BetterWay46. 재사용 가능한 @property 메서드를 만들려면 디스크립터를 사용해라.](#betterway46-재사용-가능한-property-메서드를-만들려면-디스크립터를-사용해라)
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

## BetterWay45. 애트리뷰트를 리팩터링하는 대신 @property를 사용해라

- `@property` 데코레이터
    - 지능적인 로직을 수행하는 애트리뷰트 정의할 수 있음 (getter, setter)
    - 기존 클래스를 호출하는 부분을 수정하지 않고도 동작을 변경할 수 있음

- leaky bucket 흐름 제어 알고리즘 예제
    - 남은 가용 용량(quota)과 가용 용량의 잔존 시간을 표현한다.
    - 시간을 일정한 간격으로 구분하고 가용 용량을 소비할 때마다 시간을 검사해 주기가 달라질 경우에 이전 주기에 미사용한 가용 용량이 새로운 주기로 넘어오지 못하게 함
    - 가용 용량을 소비하는 쪽에서 어떤 작업을 하고 싶을 때마다 먼저 리키 버킷으로부터 자신의 작업에 필요한 용량을 할당받아야 한다.

```python
from datetime import datetime, timedelta

class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quote = 0
        
    def __repr__(self):
        return f'Bucket(quota={self.quote})'

def fill(bucket, amount):
    now = datetime.now()
    
    if (now - bucket.reset_time) > bucket.period_delta :
        bucket.quote = 0
        bucket.reset_time = now
    
    bucket.quote += amount

def deduct(bucket, amount):
        now = datetime.now()
        
        if (now - bucket.reset_time) > bucket.period_delta:
            return False # 새 주기가 시작됐는데 아직 버킷 할당량이 재설정 되지 않음
        
        if bucket.quote - amount < 0:
            return False # 버킷의 가용 용량이 충분하지 못함
        else:
            bucket.quote -= amount
            return True # 버킷의 가용 욜야이 충분하므로 필요한 분량을 사용
        

bucket = Bucket(60)
fill(bucket, 100)
print(bucket) # Bucket(quota=100)

## 그 후 사용할 때마다 필요한 용량을 버킷에서 빼야 함

if deduct(bucket, 99):
    print('99 용량 사용') # 이게 출력됨
else:
    print('가용 용량이 작아서 99 용량을 처리할 수 없음')
    
print(bucket) # Bucket(quota=1)

if deduct(bucket, 3):
    print('3 용량 사용')
else:
    print('가용 용량이 작아서 3 용량을 처리할 수 없음') ## 이게 출력됨
print(bucket) # Bucket(quota=1)
```

- 위 예제의 문제는 가용 용량이 얼마인지 알 수 없다는 문제가 있음
    - 만야 `deduct()`함수가 실패했을 때, 용량이 부족한지, 주기에 따른 양을 초기화하지 않았는지 원인을 알 수 없음
    - `max_qoute`와 `quota_consumed`를 추적하도록 기능 추가
    - 원래 `Bucket` 클래스와 인터페이스르 동일하게 제공하기 위해 `@property`가 붙은 메서드를 사용해 클래스의 두 애트리뷰트(`max_quota`, `qouta_consumed`)에서 현재 사용 용량 수준을 그때그때 계산하게 한다.

```python
from datetime import datetime, timedelta

class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
        
    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}), ' 
                f'quota_consumed={self.quota_consumed}')
        
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        
        if amount == 0:
            # 새로운 주기가 되고 가용 용량을 재설정 하는 경우
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 새로운 주기가 되고 가용 용량을 추가하는 경우
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # 어떤 주기 안에서 가용 용량을 소비하는 경우
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.now()
    
    if (now - bucket.reset_time) > bucket.period_delta :
        bucket.quota = 0
        bucket.reset_time = now
    
    bucket.quota += amount

def deduct(bucket, amount):
        now = datetime.now()
        
        if (now - bucket.reset_time) > bucket.period_delta:
            return False # 새 주기가 시작됐는데 아직 버킷 할당량이 재설정 되지 않음
        
        if bucket.quota - amount < 0:
            return False # 버킷의 가용 용량이 충분하지 못함
        else:
            bucket.quota -= amount
            return True # 버킷의 가용 욜야이 충분하므로 필요한 분량을 사용


bucket = NewBucket(60)
print('최초', bucket)
fill(bucket, 100)
print('보충 후', bucket)

if deduct(bucket, 99):
    print('99 용량 사용') # 이게 출력됨
else:
    print('가용 용량이 작아서 99 용량을 처리할 수 없음')
    
print('사용 후', bucket) 

if deduct(bucket, 3):
    print('3 용량 사용')
else:
    print('가용 용량이 작아서 3 용량을 처리할 수 없음')  # 이게 출력됨
print('여전히', bucket)

# 최초 NewBucket(max_quota=0), quota_consumed=0
# 보충 후 NewBucket(max_quota=100), quota_consumed=0
# 99 용량 사용
# 사용 후 NewBucket(max_quota=100), quota_consumed=99
# 가용 용량이 작아서 3 용량을 처리할 수 없음
# 여전히 NewBucket(max_quota=100), quota_consumed=99
```

- `@property`활용의 좋은점
    - `Bucket.quota`를 사용하는 코드 변경이 필요 없음
    - 새로운 `NewBucket`은 기존 `Bucket`과 똑같이 잘 동작함
    - 

- 하지만 `@property`를 남용하면 안됨.
    - 과도하게 사용하게 된다면 클래스를 리팩토링 하는 선택지를 고려해야 함.

### 기억해야 할 Point
> - `@property`를 사용해 기존 인스턴스 애트리뷰트에 새료운 기능을 제공할 수 있다.<br>
> - `@property`를 사용해 데이터 모델을 점진적으로 개선하라.<br>
> - `@property` 메서드를 과하게 쓰고 있다면 클래스와 클래스를 사용하는 모든 코드를 리팩터링하는 것을 고려하자 <br>

<br>

## BetterWay46. 재사용 가능한 @property 메서드를 만들려면 디스크립터를 사용해라

- `@property`의 가장 큰 문제점은 재사용성이 떨어지는 것이다.
    - `@property`로 데코레이션하는 메서드를 같은 크래스에 속하는 여러 애트리뷰트로 사용할 수 없다.
    - 무관한 클래스 사이에서 `@property` 데코레이터를 적용한 메서드를 재사용 할 수 없다.

- 학생 숙제 점수가 백뷸율 값인지 검증하는 예제
    - Homework는 편리하게 사용할 수 있음
    - 하지만 Exam같이 확장하고자 한다면
        - 각 카테고리 점수마다 `@property`와 세터를 통해 검증을 구형해줘야 함.
        - 코드 반복이 너무 많아진다.
```python
class Homework:
    def __init__(self):
        self._grade = 0
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
        
        self._grade = value

## @property를 사용해서 이 클래스를 쉽게 사용가능
galileo = Homework()
galileo.grade = 95


class Exam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
    
    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
    
    @property
    def writing_grade(self):
        return self._writing_grade
    
    @writing_grade.setter
    def writing_grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
    
    @property
    def math_grade(self):
        return self._math_grade
    
    @math_grade.setter
    def math_grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
```

- 위의 번거로운 작업에서 적용할 수 있는 방법은 `디스크립터`를 사용하는 것입니다.
- `디스크립터 프로토콜`
    - 파이썬에서 애트리뷰트 접근을 해석하는 방법을 정의
    - `__get__`과 `__set__`메서들르 제공
    - 위 두 메서드를 사용하면 별다른 준비 코드 없이 원하는 동작을 재사용할 수 있다.
    - 같은 로직을 한 클래스 안에 속한 여러 애트리뷰트에 적용할 수 있다. (믹스인 보다 나음)

- grade 디스트립터를 구현한 사용 예제
    - Exam 클래스 인트턴스에서 각 클래스 애트리뷰트에 접근할 때 다음과 같이 접근됨
        `Exam.__dict__['wirting_grade'].__set__(exam, 40)`,
        `Exam.__dict__['wirting_grade'].__get__(exam, Exam)`,
    - `__get__`과 `__set__`메서드가 정의된 객체라면 파이썬은 디스크립터프로토콜을 따라야 한다고 결정한다.

```python
class Grade:
    def __init__(self):
        self._value = 0
        
    def __get__(self, instance, instance_type):
        return self._value
    
    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
        self._value = value
        
        
class Exam:
    # 클래스 애트리뷰트
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exma = Exam()
first_exma.writing_grade = 82
first_exma.science_grade = 99
print('쓰기', first_exma.writing_grade) # 쓰기 82
print('과학', first_exma.science_grade) # 과학 99
```

- 하지만 여러 Exam 인스턴스 객체에 대해 애트리뷰트 접근을 시도하면 예상하지 못한 동작을 볼 수 있다.
    - first인데도 second에 넣은 값이 불려와짐.
    - 문제는 writing_grade 클래스 애트리뷰트로 한 Grade 인스턴스를 모든 Exam 인스턴스가 공유한다는 점이다.
    - 프로그램이 실행되는 동아 Exam 클래스가 처음 정의될 때 이 애트리뷰트에 대한 Grade 인스턴스가 단 한 번만 생성된다.( 매번 생성되지 않아 모두 같음.. )
```python
second_exam = Exam()
second_exam.writing_grade = 75
print(f'두 번째 쓰기 점수 {second_exam.writing_grade} 맞음')
print(f'첫 번째 쓰기 점수 {first_exma.writing_grade} 틀림; '
      f'82점이어야 함')
# 두 번째 쓰기 점수 75 맞음
# 첫 번째 쓰기 점수 75 틀림; 82점이어야 함
```

- Grade 클래스가 각가 유일한 Exam 인스턴으세 대해 따로 값을 추적하게 해야함.
    - 인스턴스별 상태를 딕셔너리에 저장하면 구현이 가능
    - 하지만 아래 방식은 `메모리 누수`가 발생함
        - values에서 모든 생성된 인스턴스를 참조하므로 GC가 정리하지 못함.

```python
## _values에 등록한 instance들이 모두 참조되어 GC로 삭제되지 않음
class Grade:
    def __init__(self):
        self._values = {}
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)
    
    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
        self._values[instance] = value
```

- 메모리 누수 문제를 해결하기 위해 `weakref` 내장 모듈 사용
    - `WeakKeyDictionary`는 딕셔너리에 객체를 저장할 때 강한참조 대신 약한참조를 사용함.
    - 파이썬 GC는 약한 참조로만 된 객체가 사용 중인 메모리를 언제든지 재활용 할 수 있음 >> 누수 해결

```python
from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        ## 약한 참조로 이 참조만 있다면 GC로 정리가능
        self._values = WeakKeyDictionary() 
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)
    
    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
        self._values[instance] = value


class Exam:
    # 클래스 애트리뷰트
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print(f'두 번째 쓰기 점수 {second_exam.writing_grade} 맞음')
print(f'첫 번째 쓰기 점수 {first_exam.writing_grade} 맞음')

```

### 기억해야 할 Point
> - `@property` 메서드의 동작과 검증 기능을 재사용 하고 싶다면 디스크립터 클래스를 만들자<br>
> - 디스크립터 클래스를 만들 때에는 메모리 누수를 방지하기 위해 `WeakKeyDictionary`를 사용하자<br>
> - `__getattribute__`가 디스크립터 프로토콜을 사용해 애트리뷰트 값을 읽거나 설정하는 방식을 이해하자.<br>
> - <br>

<br>



## BetterWay47. 지연 계산 애트리뷰트가 필요하면 `__getattr__`, `__getattribute__`, `__setattr__` 을 사용하라.

- python object 훅 을 사용하면 시스템을 서로 접합하는 제너릭 코드를 쉽게 작성할 수 있다.

- DB 레코드를 객체로 표현하는 예제에서...
    - DB와 python object를 이어주는 클래스를 일반적으로 만들어야 모든 스키마에 적용할 수 있다.
    - 그러기 위해서 어떻게 해야할까?
        - `@property`, 디스크립터 등은 미리 정의해야 해서 사용 불가.
        - `__getattr__`를 이용해 위와 같은 동적 기능을 사용 가능
            (객체에 없는 애트리뷰트에 접근할 때 호출되는 매직메서드)

```python
## DB 레코드를 객체로 표현하는 기본 예제
class LazyRecord:
    def __init__(self):
        self.exists = 5
        
    def __getattr__(self, name):
        value = f'{name}를 위한 값'
        setattr(self, name, value)
        return value
    

data = LazyRecord()
print('이전: ', data.__dict__)  # 이전:  {'exists': 5}
print('foo: ', data.foo)        # foo:  foo를 위한 값
print('이후: ', data.__dict__)  # 이후:  {'exists': 5, 'foo': 'foo를 위한 값'}
```

- 기본 예제에 로그를 추가해서 `__getattr__`이 실제 언제 호출되는지 확인해보자.
    - LazyRecord 클래스에 exists 애트리뷰트가 있으니 `__getattr__` 호출 X
    - 첫 번째 foo 호출 `__getattr__` 호출 O
    - 두 번째 foo 호출 `__getattr__` 호출 X
```python
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* 호출: __getattr__({name!r}), '
              f'인스턴스 딕셔너리 채워 넣음')
        result = super().__getattr__(name)
        print(f'* 반환: {result!r}')
        return result
    
data = LoggingLazyRecord()
print('exists: ', data.exists)
print('첫 번째 foo: ', data.foo)
print('두 번째 foo: ', data.foo)

# exists:  5
# * 호출: __getattr__('foo'), 인스턴스 딕셔너리 채워 넣음
# * 반환: 'foo를 위한 값'
# 첫 번째 foo:  foo를 위한 값
# 두 번째 foo:  foo를 위한 값
```

- 이런 기능은 스키마가 없는 데이터에 지연 계산으로 접근하는 등의 활용에 유용.
    - 스키마가 없으면 `__getattr__`이 실행되어 프로퍼티를 적재하는 힘든 작업을 모두 처리
    - 이후에는 데이터를 읽어오는 동작으로 실행됨

- 이 DB 안에서 트랜잭션이 필요하다고 한다면
    - 프로퍼티에 접근시 레코드가 유효한지, 트랜잭션이 유효한지 판단해야 함.
    - 위 기능을 `__getattr__` 훅 으로 이런 기능을 안정적으로 사용할 수 있음.

- `__getattribute__` 매직메서드
    - 애트리뷰트에 접근할 때마다 호출됨
    - 프로퍼티에 접근할 때 항상 전역 트랜잭션 상태를 검사하는 등의 작업 수행 가능
    - 비용이 많이 들고 성능에 부정적인 영향을 줄 수 있기도 하지만, 비용을 감수해야 하는 경우도 있다.

- 프로퍼티 호출 시 로그를 남기는 예제
    - 존재하지 않는 프로퍼티에 동적으로 접근하는 경우 `AttributeError` 예외 발생
    - `__getattr__`과 `__getattribute__`에서 존재하지 않은 프로퍼티를 사용할 때 `AttributeError` 발생.

```python
## __getattribute__예제

class ValidatingRecord:
    def __init__(self):
        self.exists = 5
    
    def __getattribute__(self, name: str) -> Any:
        print(f'* 호출: __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* {name!r} 찾음, {value!r} 반환')
            return value
        except AttributeError:
            value = f'{name}을 위한 값'
            print(f'* {name!r}를 {value!r}로 설정')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print('exists: ', data.exists)
print('첫 번째 foo: ', data.foo)
print('두 번째 foo: ', data.foo)

# exists:  5
# * 호출: __getattribute__('foo')
# * 'foo'를 'foo을 위한 값'로 설정
# 첫 번째 foo:  foo을 위한 값
# * 호출: __getattribute__('foo')
# * 'foo' 찾음, 'foo을 위한 값' 반환
# 두 번째 foo:  foo을 위한 값
```

- `__getattr__`과 `__getattribute__`의 차이
    - `hasattr()`과 `getattr()`메서드에서 차이가 발생합니다.
    - `__getattr__`은 한 번만 호출되만 `__getattribute__`는 `getattr()`이든 `hasattr()`이든 호출 될 때마다 호출됩니다.
```python
## getattr 구현
data1 = LoggingLazyRecord()
print('이전: ', data1.__dict__)
print('최초에  foo가 있나: ', hasattr(data1, 'foo'))
print('이후: ', data1.__dict__)
print('두 번째 foo가 있나: ', hasattr(data1, 'foo'))

# 이전:  {'exists': 5}
# * 호출: __getattr__('foo'), 인스턴스 딕셔너리 채워 넣음
# * 반환: 'foo를 위한 값'
# 최초에  foo가 있나:  True
# 이후:  {'exists': 5, 'foo': 'foo를 위한 값'}
# 두 번째 foo가 있나:  True
# * 호출: __getattribute__('__dict__')
# * '__dict__' 찾음, {'exists': 5} 반환

## getattribute 구현
data2 = ValidatingRecord()
print('이전: ', data2.__dict__)
print('최초에  foo가 있나: ', hasattr(data1, 'foo'))
print('두 번째 foo가 있나: ', hasattr(data1, 'foo'))

# 이전:  {'exists': 5}
# 최초에  foo가 있나:  True
# 두 번째 foo가 있나:  True
```

- DB 예제에서, 파이썬 객체에 값이 대입된 경우, 나중에 데이터베이스에 다시 저장하고 싶은 경우
    - 임의 애트리뷰트에 값을 설정할 때마다 호출되는 `__setattr__`을 사용
    - `setattr()` 함수를 통해 입력되든 직접 입력되든 호출됨

```python
class SavingRecord():
    def __seattr__(self, name, value):
        # 데이터를 db에 저장
        super().__setattr__(name, value)


class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f'* 호출: __setattr__({name!r}, {value!r})')
        super().__setattr__(name, value)
        
data = LoggingSavingRecord()
print('이전:', data.__dict__)
data.foo = 5
print('이후:', data.__dict__)
data.foo = 7
print('최후:', data.__dict__)

# 이전: {}
# * 호출: __setattr__('foo', 5)
# 이후: {'foo': 5}
# * 호출: __setattr__('foo', 7)
# 최후: {'foo': 7}
```

- `__getattr__` 이나 `__setattr__`은 모든 애트리뷰트에서 접근된다는 단점이 있음
    - 무한 재귀에 걸릴 가능성이 있음
    - 무한재귀를 피하기 위해서는 `super().__getattribute__`를 호출해 인스턴스 애트리뷰트 딕셔너리에서 값을 가져오는 것이다.
    - `__setattr__`도 같은 문제를 가지는데 `super().__setattr__`를 호출해서 해결한다.
```python
## 무한재귀
class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}
    
    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        return self._data[name]

data = Brokedata = BrokenDictionaryRecord({'foo': 3})
data.foo # RecursionError: maximum recursion depth exceeded

## 재귀 피하는 법
## 인스턴스 애트리뷰트 딕셔너리에서 값을 가져옴
class DictionaryRecord:
    def __init__(self, data):
        self._data = data
    
    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

data = DictionaryRecord({'foo': 3})
print('foo: ', data.foo)
# * 호출: __getattribute__('foo')
# foo:  3

```

### 기억해야 할 Point
> - `__getattr__`, `__setattr__`를 사요해 객체의 애트리뷰트를 지연해 가져오거나 저장할 수 있다<br>
> - `__getattr__`은 애트리뷰트가 존재하지 않을 때만 호출.<br>
> - `__getattribute__`는 애트리뷰트를 읽을 때 항상 호출<br>
> - `__getattribute__`와 `__setattr__`에서 무한 재귀를 피하려면 `super()`(object 클래스)에 있는 메서드를 사용해 인스턴스 애트리뷰트에 접근한다<br>

<br>




## BetterWay48. `__init_subclass__`를 사용해 하위 클래스를 검증하라.

- 메타클래스 활용방법
    - 클래스가 제대로 구현되었는지 검증
    - 복잡한 클래스 계층을 설계할 때 스타일을 강제
    - 메서드를 오버라이드하도록 요청
    - 클래스 애트리뷰트 사이에 엄격한 관계를 가지도록 설계

-  클래스 생성 시 검증 로직을 `__init__`에 구현하는 경우가 종종 있음
- 메타클래스를 사용하면 import 시점에 검증이 이뤄지기 때문에 예외가 훨씬 빨리 발생한다.


- 일반적인 객체에 대해 메타클래스가 작동하는 원리 예제
    - 메타클래스는 `type`를 상속해 정의됨
    - 기본적인 경우 `__new__` 메서드를 통해 자신과 연관된 클래스 내용을 받음
    - 어떤 타입이 구성되기 전 클래스 정보를 살펴보고 변경하는 예제
    - 연관퇸 클래스가 정의되기 전에 클래스의 모든 파라미터를 검증하려면 `Meta.__new__`에 기능을 추가해야 한다.

```python
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* 실행: {name}dml apxk {meta}.__new__')
        print('기반 클래스들:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    stuff = 123
    
    def foo(self):
        pass


class MYSubclass(MyClass):
    other = 567
    
    def bar(Self):
        pass
    

# * 실행: MyClass의 메타 <class '__main__.Meta'>.__new__
# 기반 클래스들: ()
# {'__module__': '__main__', '__qualname__': 'MyClass', 'stuff': 123, 'foo': <function MyClass.foo at 0x000002DCD0928FE0>}      
# * 실행: MYSubclass의 메타 <class '__main__.Meta'>.__new__
# 기반 클래스들: (<class '__main__.MyClass'>,)
# {'__module__': '__main__', '__qualname__': 'MYSubclass', 'other': 567, 'bar': <function MYSubclass.bar at 0x000002DCD0929080>}
```

- 검증 수행 메타클래스 구현
    - 모든 다각형 클래스 계층 구조의 기반 클래스로 사용
    - 이 검증은 class 문에서 변 개수가 3보다 작은 경우에 해당 class 본문이 실행된 직후 예외를 발생시킨다.
    - 하지만, 동적으로 임포트되는 모듈에서는 시작되지 않음
```python
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Polygon 클래스의 하위 클래스만 검증
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('다각형의 변은 3개 이상이어야 함')
        
        return type.__new__(meta, name, bases, class_dict)
    

class Polygon(metaclass=ValidatePolygon):
    sides = None
    
    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180
    

class Triangle(Polygon):
    sides = 3
    

class Rectangel(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9

## 무사히 통과
assert Triangle.interior_angles() == 180
assert Rectangel.interior_angles() == 360
assert Nonagon.interior_angles() == 1260


print('class 이전')
class Line(Polygon):
    print('sides 이전')
    sides = 2
    print('sides 이후')
    
print('class 이후')

# class 이전
# sides 이전
# sides 이후
# ValueError: 다각형의 변은 3개 이상이어야 함
```

- 위 예제는 다소 복잡해보임. 기본적인 작업인데 너무 복잡한 코드를 짜야 되는 것처럼 보임
    - 파이썬 3.6 부터는 메타클래스를 정의하지 않고 같은 동작 구현 가능 ( `__init_subclass__` 메서드 정의 )
    - Validation metaclass를 정의하지 않아도 되서 코드가 훨씬 짧아졌다.
```python
### __init_subclass__ 예제
class BetterPolygon:
    sides = None
    
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        
        if cls.sides < 3:
            raise ValueError('다각형 변은 3개 이상이어야 함')
        
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Hexagon(BetterPolygon):
    sides = 6
    
assert Hexagon.interior_angles() == 720
```

- 표준 메타클래스의 또 다른 문제점은
    - 클래스 정의마다 메카틀리스를 단 하나만 지정할 수 있음.
    - (앞에서 말한 하나) 코드가 길어짐
    - polygon 과 filled 를 같이 상속하는 클래스에서 에러남ㅇ

```python
class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # Filled 클래스의 하위 클래스만 검증
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        
        return type.__new__(meta, name, bases, class_dict)

class Filled(metaclass=ValidateFilled):
    color = None

class RedPentagon(Filled, Polygon):
    color = 'red'
    sides = 5

# TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
```

- 검증을 여러 단계로 만들기 위해 복잡한 메타클래스 type 정의를 복잡한 계층으로 설계함으로써 문제 해결 가능
    - 하지만 이런 방식은 합성성(composability)를 해침
    - type을 통한 구현이 이런 방법이 필요함에도 코드 재사용성을 해침
```python
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증
        if not class_dict.get('is_root'):
            if class_dict['sides'] < 3:
                raise ValueError('다각형은 변의 개수가 3개 이상이어야 함')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(metaclass=ValidatePolygon):
    is_root = True
    sides = None


class ValidateFilledPolygon(ValidatePolygon):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증
        if not class_dict.get('is_root'):
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        return type.__new__(meta, name, bases, class_dict)
    

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
    is_root = True
    color = None


class GreenPentagon(FilledPolygon):
    color = 'green'
    sides = 5

greenie = GreenPentagon()
assert isinstance(greenie, Polygon) ## 성공

 
## ValueError: 지원하지 않는 color 값
# class OrangePentagon(FilledPolygon):
#     color = 'orange'
#     sides = 5

## validatepolygon 에러가 발생해야 하는데 안함... 왜지?
class RedLine(FilledPolygon):
    color = 'red'
    sides = 1
``` 

- 위 예제의 복잡성도 `__init_subclass__` 구현을 통해 해결할 수 있음
    - 훨씬 간단해진다. 
```python
class Filled:
    color = None
    
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('지원하지 않는 color')


class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)

# class BlueLine(Filled, Polygon):
#     color = 'blue'
#     sides = 2
# ValueError: 다각형은 변의 개수가 3개 이상이어야 함

# class BeigeTriangle(Filled, Polygon):
#     color = 'beige'
#     sides = 3
# ValueError: 지원하지 않는 color
```

- 심지어 `__init__subclass__`를 다이아몬드 상속 같은 복잡한 경우에도 사용할 수 있다.
    - Bottom 클래스에서 Top에 이르는 상속 경로가 2개 지만, 각 클래스마다 `Top.__ini_subclass__`는 단 한 번만 호출된다.

```python
class Top:
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print(f'{cls}의 Top')

class Left:
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print(f'{cls}의 Left')

class Right:
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print(f'{cls}의 Right')

class Bottom:
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        print(f'{cls}의 Bottom')
        

# <class '__main__.Left'>의 Top
# <class '__main__.Right'>의 Top
# <class '__main__.Bottom'>의 Top
# <class '__main__.Bottom'>의 Right
# <class '__main__.Bottom'>의 Left
```

### 기억해야 할 Point
> - 메타클래스의 `__new__` 메서드는 class문의 모든 본문이 처리된 직후 호출<br>
> - 메타클래스를 사용해 클래스가 정의된 지후이면서 클래스가 생성되지 직전인 시점에 클래스 정의를 변경할 수 있다.  하지만 메타클래스 구현은 코드가 너무 복잡해진다.<br>
> - `__init_subclass__`를 사용해 하위클래스가 정의된 직후, 하위 클래스 타입이 만들어 지기 직전에 해당 클래스가 가진 조건을 잘 갖췄는지 확인하자<br>
> - `__init_subclass__`정의 안에서 `super().__init_usbclass__`를 호출해 여러 계층에 걸쳐 클래스를 검증하고 다중 상혹을 제대로 처리할 수 있다.<br>

<br>


## BetterWay49. `__init_subclass__`를 사용해 클래스 확장을 등록하라.

- 메타클래스로 프로그램이 자동으로 타입 등록 프로그램이 자동으로 타입 등록이 가능
    - 간단한 식별자로 그에 해당하는 클래스를 찾는 역검색 기능에 효과적임
- 파이썬 `object`를 JSON으로 직렬화하하는 표현 방식을 구현하는 예제
    - `object`를 JSON문자열로 변환할 방법이 필요
    - 생성자 파라미터를 기록 
    - JSON 딕셔너리로 변환
```python
import json

class Serializable:
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({'args': self.args})

## 위 클래스를 사용하면 Point 같은 간단한 불변 데이터 구조를 쉽게 직렬화 할 수 있음

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'
    
point = Point2D(5, 3)
print('객체: ', point)
print('직렬화: ', point.serialize())
# 객체:  Point2D(5, 3)
# 직렬화:  {"args": [5, 3]}
```

- 이제 이 JSON 문자열을 역직렬화해서 문자열이 표현하는 Point2D 객체를 구성해야 함
    - Serializable을 부모 클래스로 하며, 부모 클래스를 활용해 데이터를 역직렬화 하는 다른 클래스를 개발
    - 이 방법은 직렬/역직렬 할 데이터의 타입을 알고 있을 때에만 가능
    - 직렬ㅗ하할 클래스가 아누 많더라도 JSON 문자열을 적당한 파이썬 object로 역직렬화하는 함수는 공통으로 하나만 있는 것이 이상적

```python
class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])
    
## Deserializable을 활용하면 간단한 불변 객체를 쉽게 직렬/역직렬 가능

class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'BetterPoint2D({self.x}, {self.y})'


before = BetterPoint2D(5, 3)
print('이전: ', before)
data = before.serialize()
print('직렬화 :', data)
after = BetterPoint2D.deserialize(data)
print('이후: ', after)
# 이전:  BetterPoint2D(5, 3)
# 직렬화 : {"args": [5, 3]}
# 이후:  BetterPoint2D(5, 3)

```

- 역직렬화 하는 공통의 함수
    - 클래스 이름을 객체 생성자로 다시 연결해주는 매핑을 유지
    - `deserializer()`가 항상 제대로 작동하려면 나중에 역직렬화할 모든 클래스에서 `register_class()`를 호출해야 함

```python
class BetterSerializable:
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })
    
    def __repr__(self):
        name = self.__class__.__name__
        args_str = ', '.join(str(x) for x in self.args)
        return f'{name}({args_str})'
    

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class
    
def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y
        
register_class(EvenBetterPoint2D)

before = EvenBetterPoint2D(5, 3)
print('이전: ', before)
data = before.serialize()
print('직렬화한 값: ', data)
after = deserialize(data)
print('이후: ', after)
# 이전:  EvenBetterPoint2D(5, 3)
# 직렬화한 값:  {"class": "EvenBetterPoint2D", "args": [5, 3]}
# 이후:  EvenBetterPoint2D(5, 3)
```

- 위 방식의 문제점은 `register_class()` 호출을 잊어버릴 수도 있다는 점이 있음
    - 등록을 잊어버린 클래스 인스턴스를 역직렬화하려고 시도하면 프로그램이 깨짐
    - `BetterSerializable`을 상속하더라도 함수 호출을 까먹으면 기능을 활용할 수 없음
    - `클래스 데코레이터`도 호출을 까먹는 실수를 할 수 있다. (뭔소리래)

- 클래스가 정의될 때 `register_class()`를 호출 하는 방법은?
- 메타클래스는 하위 클래스가 정의될 때 class 문을 가로채서 가능함
    - 메타 클래스를 사용해서 클래스 본문을 처리 후 새로운 타입을 등록

```python
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls) ## 여기서 호출해줌
        return cls
    

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass

class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z
    
before = Vector3D(10, -7, 3)
data = before.serialize()
print('이전: ', before)
data = before.serialize()
print('직렬화한 값: ', data)
print('이후: ', deserialize(data))
# 이전:  Vector3D(10, -7, 3)
# 직렬화한 값:  {"class": "Vector3D", "args": [10, -7, 3]}
# 이후:  Vector3D(10, -7, 3)

```

- 더 좋은 방법은 `__init__subclass__` 클래스를 사용
    - python 3.6 부터 적용
    - 클래스를 정의할 때 커스텀 로직을 제공할 수 있음
    - 복잡한 메타클래스 구문을 혼동하기 쉬운 점을 개선

```python
class BetterRegisterdSerializable(BetterSerializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls) ## 여기서 호출해줌
    
    
class Vector1D(BetterRegisterdSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude
    
    
before = Vector1D(6)
data = before.serialize()
print('이전: ', before)
data = before.serialize()
print('직렬화한 값: ', data)
print('이후: ', deserialize(data))
# 이전:  Vector1D(6)
# 직렬화한 값:  {"class": "Vector1D", "args": [6]}
# 이후:  Vector1D(6)
```

### 기억해야 할 Point
> - 클래스 등록은 파이썬 프로그램을 모듈화할 때 유용한 패턴<br>
> - 메타클래스를 사용하면, 프로그램 안에서 기반 클래스를 상혹한 하위 클래스가 정의될 때 등록 코스를 자동으로 실행할 수 있다.<br>
> - 메타클래스를 클래스 등록에 사용하면 클래스 등록 함수를 호출하지 않아서 생기는 오류를 피할 수 있다.<br>
> - 메타클래스 방식보다 `__init_subclass__`가 코드가 깔끔하고 이해하기 쉽다.<br>

<br>


## BetterWay50. `__set_name__`으로 클래스 애트리뷰트를 표시하라.

- 매타클래스 유용한 기능
    - 클래스가 정의된 후 클래스가 실제로 사용되기 이전인 시점에 프로퍼티를 변경하거나 표시할 수 있는 기능
    - 애트리뷰트가 포함된 클래스 내부에서 애트리뷰트의 사용을 자세히 관찰하고자 `디스크립터`를 쓸 때 이런 접근 방법을 사용함.(Betterway46)
    

- 데이터베이스의 로우를 표현하는 새클래스 정의 예제
    - 디스크립터 Field 클래스
    - Field를 이용해 데이터베이스 테이블 정의
    - Field 디스크립터가 `__dict__`인스턴스 딕셔너리를 변화시킴
    - 이 예제는 중복이 많음
        - 테이블에서 애트리뷰트 이름을 정했는데 또 Field에 지정해줘야함.
```python
## 디스크립터는 __get__, __set__ 또는 __delete__ 를 정의한 모든 객체.
## 선택적으로 __set_name__을 가지기도 함
class Field:
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + name
    
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
    

class Customer:
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')
    
cust = Customer()
print(f'이전: {cust.first_name!r} {cust.__dict__}') # 이전: '' {}
cust.first_name = '유클리드'
print(f'이후: {cust.first_name!r} {cust.__dict__}') # 이후: '유클리드' {'first_name': '유클리드'}
```

- 위의 중복을 줄이기 위해 메타클래스를 사용
    - 하지만 이 방식의 문제점
    - DatabaseRow를 상속하는 것을 잊어버리거나, 클래스 계층 구조러 인한 제약 때문에 상속할 수 없는 경우, Field 클래스를 프로퍼티에 사용할 수 없음

```python
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        
        cls = type.__new__(meta, name, bases, class_dict)
        return cls
    
class DatabaseRow(metaclass=Meta):
    pass

class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None
    
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        

class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()
    
cust = BetterCustomer()
print(f'이전: {cust.first_name!r} {cust.__dict__}') # 이전: '' {}
cust.first_name = '오일러'
print(f'이후: {cust.first_name!r} {cust.__dict__}') # 이후: '오일러' {'_first_name': '오일러'}
```

- 상속을 잊는 경우나 상속할 수 없는 경우를 보완하는 방법은, 디스크립터에 `__set_name__`메서드를 사용하는 것
    - 클래스가 정의될 때 마다 파이썬은 해당 클래스 안의 디스크립터 인스턴스의 `__set_name__`을 호출함
    - `__set_name__`은 디스크립터 인스턴스를 소유 중인 클래스와 디스크립터 인스턴스가 대입될 애트리뷰트 이름을 인자로 받음
    
- 메타클래스 정의(`__new__`)를 피하고 `__set_name__`으로 전환 예제
    - 메타클래스를 정의하고 기반 클래스를 상속하지 않아도 디스크립터가 제공하는 기능을 모두 사용할 수 있음
```python
class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None
        
    def __set_name__(self, owner, name):
        # 클래스가 생성될 때 모든 스크립터에 대해 이 메서드가 호출
        self.name = name
        self.internal_name = '_' + name
    
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        
class FixedCustomer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

cust = FixedCustomer()
print(f'이전: {cust.first_name!r} {cust.__dict__}') # 이전: '' {}
cust.first_name = '메르센'
print(f'이후: {cust.first_name!r} {cust.__dict__}') # 이후: '메르센' {'_first_name': '메르센'}
```

### 기억해야 할 Point
> - 메타클래스를 사용하면 어떤 클래스가 완전히 정의되기 전에 클래스 애트리뷰트를 변경할 수 있다.<br>
> - 디스크립터와 메타클래스를 조합하면 강력한 실행 시점 코드 검사와 선언적인 동작을 만들 수 있다.<br>
> - `__set_name__` 메서드를 디스크립터 클래스에 정의하면 디스크립터가 포함된 클래스의 프로퍼티 이름을 처리할 수 있다.<br>
> - 디스크립터가 변경한 클래스의 인스턴스 딕셔너리에 데이터를 저장하게 만들면 메모리 누수를 피할 수 있고, `weakref`내장 메서드를 사용하지 않아도 된다.<br>

<br>

## BetterWay51. 합성 가능한 클래스 확장이 필요하면 메타클래스보다는 클래스 데코레이터를 사용하라.

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>
