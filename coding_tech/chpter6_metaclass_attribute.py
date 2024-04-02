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