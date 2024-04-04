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
        - 각 카테고리 점수마다 `@propert`와 세터를 통해 검증을 구형해줘야 함.
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
