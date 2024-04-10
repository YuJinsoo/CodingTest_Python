# # 44

# class OldResistor:
#     def __init__(self, ohms):
#         self._ohms = ohms
    
#     def get_ohms(self):
#         return self._ohms
    
#     def set_ohms(self, ohms):
#         self._ohms = ohms
        

# r0 = OldResistor(50e3)
# print("이전: ", r0.get_ohms())  # 이전:  50000.0
# r0.set_ohms(10e3)
# print("이후: ", r0.get_ohms())  # 이후:  10000.0





# class Resistor:
#     def __init__(self, ohms):
#         self.ohms = ohms
#         self.voltage = 0
#         self.current = 0

# r1 = Resistor(50e3)
# r1.ohms = 10e3

# class VoltageResistance(Resistor):
#     def __init__(self, ohms):
#         super().__init__(ohms)
#         self._voltage = 0
    
#     @property
#     def voltage(self):
#         return self._voltage

#     @voltage.setter
#     def voltage(self, voltage):
#         self._voltage = voltage
#         self.current = self._voltage / self.ohms


# r2 = VoltageResistance(1e3)
# print(f'이전: {r2.current: .2f} 암페어') # 이전:  0.00 암페어
# r2.voltage = 10
# print(f'이전: {r2.current: .2f} 암페어') # 이전:  0.01 암페어



# class BoundedResistance(Resistor):
#     def __init__(self, ohms):
#         super().__init__(ohms)
        
#     @property
#     def ohms(self):
#         return self._ohms
    
#     ## 잘못된 값 입력이 에러 발생하도록.
#     @ohms.setter
#     def ohms(self, ohms):
#         if ohms <= 0:
#             raise ValueError(f'저항 > 0 이어야 합니다. 입력값: {ohms}')
#         self._ohms = ohms

# r3 = BoundedResistance(1e3)
# # r3.ohms= 0 # ValueError: 저항 > 0 이어야 합니다. 입력값: 0


# class FixedResistance(Resistor):
#     def __init__(self, ohms):
#         super().__init__(ohms)
    
#     @property
#     def ohms(self):
#             return self._ohms
    
#     @ohms.setter
#     def ohms(self, ohms):
#         if hasattr(self, '_ohms'):
#             raise AttributeError('Ohms는 불변 객체. 한번만 초기화됨')

#         self._ohms = ohms

# r4 = FixedResistance(1e3)
# # r4.ohms = 2e3 # AttributeError: Ohms는 불변 객체. 한번만 초기화됨

# class MysteriousResistor(Resistor):
#     @property
#     def ohms(self):
#         self.voltage = self._ohms * self.current
#         return self._ohms
    
#     @ohms.setter
#     def ohms(self, ohms):
#         self._ohms = ohms

# r7 = MysteriousResistor(10)
# r7.current = 0.01
# print(f'이전: {r7.voltage: .2f}')   # 이전:  0.00

# r7.ohms
# print(f'이후: {r7.voltage: .2f}')   # 이전:  0.00


# 이후:  0.10



# 45

# from datetime import datetime, timedelta

# class Bucket:
#     def __init__(self, period):
#         self.period_delta = timedelta(seconds=period)
#         self.reset_time = datetime.now()
#         self.quote = 0
        
#     def __repr__(self):
#         return f'Bucket(quota={self.quote})'

# def fill(bucket, amount):
#     now = datetime.now()
    
#     if (now - bucket.reset_time) > bucket.period_delta :
#         bucket.quote = 0
#         bucket.reset_time = now
    
#     bucket.quote += amount

# def deduct(bucket, amount):
#         now = datetime.now()
        
#         if (now - bucket.reset_time) > bucket.period_delta:
#             return False # 새 주기가 시작됐는데 아직 버킷 할당량이 재설정 되지 않음
        
#         if bucket.quote - amount < 0:
#             return False # 버킷의 가용 용량이 충분하지 못함
#         else:
#             bucket.quote -= amount
#             return True # 버킷의 가용 욜야이 충분하므로 필요한 분량을 사용
        

# bucket = Bucket(60)
# fill(bucket, 100)
# print(bucket) # Bucket(quota=100)

# ## 그 후 사용할 때마다 필요한 용량을 버킷에서 빼야 함

# if deduct(bucket, 99):
#     print('99 용량 사용') # 이게 출력됨
# else:
#     print('가용 용량이 작아서 99 용량을 처리할 수 없음')
    
# print(bucket) # Bucket(quota=1)

# if deduct(bucket, 3):
#     print('3 용량 사용')
# else:
#     print('가용 용량이 작아서 3 용량을 처리할 수 없음') ## 이게 출력됨
# print(bucket) # Bucket(quota=1)

# from datetime import datetime, timedelta

# class NewBucket:
#     def __init__(self, period):
#         self.period_delta = timedelta(seconds=period)
#         self.reset_time = datetime.now()
#         self.max_quota = 0
#         self.quota_consumed = 0
        
#     def __repr__(self):
#         return (f'NewBucket(max_quota={self.max_quota}), ' 
#                 f'quota_consumed={self.quota_consumed}')
        
#     @property
#     def quota(self):
#         return self.max_quota - self.quota_consumed

#     @quota.setter
#     def quota(self, amount):
#         delta = self.max_quota - amount
        
#         if amount == 0:
#             # 새로운 주기가 되고 가용 용량을 재설정 하는 경우
#             self.quota_consumed = 0
#             self.max_quota = 0
#         elif delta < 0:
#             # 새로운 주기가 되고 가용 용량을 추가하는 경우
#             assert self.quota_consumed == 0
#             self.max_quota = amount
#         else:
#             # 어떤 주기 안에서 가용 용량을 소비하는 경우
#             assert self.max_quota >= self.quota_consumed
#             self.quota_consumed += delta


# def fill(bucket, amount):
#     now = datetime.now()
    
#     if (now - bucket.reset_time) > bucket.period_delta :
#         bucket.quota = 0
#         bucket.reset_time = now
    
#     bucket.quota += amount

# def deduct(bucket, amount):
#         now = datetime.now()
        
#         if (now - bucket.reset_time) > bucket.period_delta:
#             return False # 새 주기가 시작됐는데 아직 버킷 할당량이 재설정 되지 않음
        
#         if bucket.quota - amount < 0:
#             return False # 버킷의 가용 용량이 충분하지 못함
#         else:
#             bucket.quota -= amount
#             return True # 버킷의 가용 욜야이 충분하므로 필요한 분량을 사용


# bucket = NewBucket(60)
# print('최초', bucket)
# fill(bucket, 100)
# print('보충 후', bucket)

# if deduct(bucket, 99):
#     print('99 용량 사용') # 이게 출력됨
# else:
#     print('가용 용량이 작아서 99 용량을 처리할 수 없음')
    
# print('사용 후', bucket) 

# if deduct(bucket, 3):
#     print('3 용량 사용')
# else:
#     print('가용 용량이 작아서 3 용량을 처리할 수 없음')  # 이게 출력됨
# print('여전히', bucket)

# # 최초 NewBucket(max_quota=0), quota_consumed=0
# # 보충 후 NewBucket(max_quota=100), quota_consumed=0
# # 99 용량 사용
# # 사용 후 NewBucket(max_quota=100), quota_consumed=99
# # 가용 용량이 작아서 3 용량을 처리할 수 없음
# # 여전히 NewBucket(max_quota=100), quota_consumed=99 s


# 46

# class Homework:
#     def __init__(self):
#         self._grade = 0
    
#     @property
#     def grade(self):
#         return self._grade
    
#     @grade.setter
#     def grade(self, value):
#         if not (0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
        
#         self._grade = value

# ## @property를 사용해서 이 클래스를 쉽게 사용가능
# galileo = Homework()
# galileo.grade = 95




# class Exam:
#     def __init__(self):
#         self._writing_grade = 0
#         self._math_grade = 0
    
#     @staticmethod
#     def _check_grade(value):
#         if not (0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')

#     # 이런 식으로 확장하려면
#     # 시험 과목을 이루는 각 부분마다 새로운 @property를 지정하고
#     # 검증 메서드를 구현해야 함.
#     # 코드 반복이 너무 많아진다.
    
#     @property
#     def writing_grade(self):
#         return self._writing_grade
    
#     @writing_grade.setter
#     def writing_grade(self, value):
#         if not (0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
    
#     @property
#     def math_grade(self):
#         return self._math_grade
    
#     @math_grade.setter
#     def math_grade(self, value):
#         if not (0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')


# class Grade:
#     def __init__(self):
#         self._value = 0
        
#     def __get__(self, instance, instance_type):
#         return self._value
    
#     def __set__(self, instance, value):
#         if not(0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
#         self._value = value
        
        
# class Exam:
#     # 클래스 애트리뷰트
#     math_grade = Grade()
#     writing_grade = Grade()
#     science_grade = Grade()

# first_exma = Exam()
# first_exma.writing_grade = 82
# first_exma.science_grade = 99
# print('쓰기', first_exma.writing_grade) # 쓰기 82
# print('과학', first_exma.science_grade) # 과학 99


# second_exam = Exam()
# second_exam.writing_grade = 75
# print(f'두 번째 쓰기 점수 {second_exam.writing_grade} 맞음')
# print(f'첫 번째 쓰기 점수 {first_exma.writing_grade} 틀림; '
#       f'82점이어야 함')
# # 두 번째 쓰기 점수 75 맞음
# # 첫 번째 쓰기 점수 75 틀림; 82점이어야 함



# ## _values에 등록한 instance들이 모두 참조되어 GC로 삭제되지 않음
# class Grade:
#     def __init__(self):
#         self._values = {}
        
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return self._values.get(instance, 0)
    
#     def __set__(self, instance, value):
#         if not(0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
#         self._values[instance] = value
        
        
# from weakref import WeakKeyDictionary

# class Grade:
#     def __init__(self):
#         ## 약한 참조로 이 참조만 있다면 GC로 정리가능
#         self._values = WeakKeyDictionary() 
        
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return self._values.get(instance, 0)
    
#     def __set__(self, instance, value):
#         if not(0 <= value <= 100):
#             raise ValueError('점수는 0과 100 사이의 값이어야 합니다.')
#         self._values[instance] = value


# class Exam:
#     # 클래스 애트리뷰트
#     math_grade = Grade()
#     writing_grade = Grade()
#     science_grade = Grade()

# first_exam = Exam()
# first_exam.writing_grade = 82
# second_exam = Exam()
# second_exam.writing_grade = 75
# print(f'두 번째 쓰기 점수 {second_exam.writing_grade} 맞음')
# print(f'첫 번째 쓰기 점수 {first_exam.writing_grade} 맞음')

# 47

from typing import Any


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

print('===============================')
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


# class BrokenDictionaryRecord:
#     def __init__(self, data):
#         self._data = {}
    
#     def __getattribute__(self, name):
#         print(f'* 호출: __getattribute__({name!r})')
#         return self._data[name]

# data = Brokedata = BrokenDictionaryRecord({'foo': 3})
# data.foo # RecursionError: maximum recursion depth exceeded

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
