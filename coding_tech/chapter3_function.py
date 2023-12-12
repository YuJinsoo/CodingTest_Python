# 19
# def get_stats(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum

# lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

# minimum, maximum = get_stats(lengths)
# print(f'최소:{minimum}, 최대:{maximum}')
# # 최소:60, 최대:73


# # 평균 대비 길이 비율
# def get_avg_ration(numbers):
#     average = sum(numbers)/len(numbers)
#     scaled = [x/average for x in numbers]
#     scaled.sort(reverse=True)
#     return scaled

# longest, *middle, shortest = get_avg_ration(lengths)
# print(f'최대길이 : {longest:>4.0%}') # 최대길이 : 108%
# print(f'최소길이 : {shortest:>4.0%}') # 최소길이 :  89%


# # 결과가 많은경우

# def get_stats(numbers):
#     ...
#     return minimum, maximum, average, median, count

# minumum, maximum, average, median, count = get_stats(lengths)

# # 줄바꿈할경우는
# minumum, maximum, average, median, count = get_stats(
#     lengths)

# minumum, maximum, average, median, count = \
#     get_stats(lengths)


# minumum, maximum, average, 
# median, count = get_stats(lengths)

# (minumum, maximum, average, median, count
#  ) = get_stats(lengths)


# 20
## 이렇게 특이한 경우 None을 반환하는 경우
# def careful_divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return None

# ## 제수가 0이 입력되면 None을 반환하는 위 함수를 활용해 문자열이 출력됩니다.
# x, y = 1, 0
# result = careful_divide(x, y)
# if result is None:
#     print('잘못된 입력')

# ## 숫자
# x, y = 0, 5
# result = careful_divide(x, y)
# if not result:
#     print('잘못된 입력') # 이 코드가 실해오디는데 사실 이 코드가 실행되면 안됨..
    
# if not 0:
#     print('gjf')
    
# if 0 == False:
#     print('hhhh')
    
# assert not 0 == True
# assert 0 == False


# def careful_divide(a, b):
#     try:
#         return True, a/b
#     except ZeroDivisionError:
#         return False, None

# x, y = 0, 5
# success, result = careful_divide(x, y)
# if not success:
#     print('잘못된 입력') # 이 코드가 실행되면 안됨..

# def careful_divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         raise ValueError('잘못된 입력입니다.')

# x, y = 5, 2
# try:
#     result = careful_divide(x, y)
# except ValueError:
#     print('잘못된 입력')
# else:
#     print('결과는 %.1f 입니다.' % result)

# # 결과는 2.5 입니다.

# def careful_divide(a: float, b: float) -> float:
#     """a를 b로 나눕니다.
#     Raise:
#         ValueError: b가 0이어서 나눗셈을 할 수 없을 때
#     """
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         raise ValueError('잘못된 입력입니다.')

# x, y = 5, 2
# try:
#     result = careful_divide(x, y)
# except ValueError:
#     print('잘못된 입력')
# else:
#     print('결과는 %.1f 입니다.' % result)

# # 결과는 2.5 입니다.




# 22

# def log(message, values):
#     if not values:
#         print(message)
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print(f'{message}: {values_str}')

# log('내 숫자는', [1, 2]) # 내 숫자는: 1, 2
# log('안녕', []) # 안녕

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는', 1, 2) # 내 숫자는: 1, 2
log('안녕') # 안녕

favorites = [7,33,99]
log('좋아하는 숫자는', *favorites) # 좋아하는 숫자는: 7, 33, 99

def my_generator():
    for i in range(10):
        yield i
        
def my_func(*args):
    print(args)

def my_func2(args):
    print(args)
    
it = my_generator()
my_func(*it) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

it = my_generator()
my_func(it) # (<generator object my_generator at 0x000001871B1C0A50>,)



def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {value_str}')

log(1, '좋아하는 숯자는', 7, 33)     # 1 - 좋아하는 숮자는: 7, 33
log(1, '안녕')                      # 1 - 안녕
log('좋아하는 숮자는', 7, 33)        # 좋아하는 숮자는 - 7: 33