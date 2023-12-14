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

# 21

# def sort_priority(values, group):
#     def helper(x):
#         if x in group:
#             return (0, x)
#         return (1, x)
#     values.sort(key=helper)
    
# numbers = [ 8,3,1,2,5,4,7,6]
# group = {2,3,5,7}
# sort_priority(numbers, group)
# print(numbers) # [2, 3, 5, 7, 1, 4, 6, 8]

# def sort_priority2(values, group):
#     found = False
#     def helper(x):
#         if x in group:
#             found = True
#             return (0, x)
#         return (1, x)
#     values.sort(key=helper)
#     return found
    
# numbers = [8,3,1,2,5,4,7,6]
# group = {2,3,5,7}
# result = sort_priority2(numbers, group)
# print(numbers, result) # [2, 3, 5, 7, 1, 4, 6, 8] False

# def sort_priority2(values, group):
#     found = False
#     def helper(x):
#         nonlocal found
#         if x in group:
#             found = True
#             return (0, x)
#         return (1, x)
#     values.sort(key=helper)
#     return found
    
# numbers = [8,3,1,2,5,4,7,6]
# group = {2,3,5,7}
# result = sort_priority2(numbers, group)
# print(numbers, result) # [2, 3, 5, 7, 1, 4, 6, 8] True


# class Sorter():
#     def __init__(self, group):
#         self.group = group
#         self.found = False
    
#     def __call__(self, x):
#         if x in self.group:
#             self.found = True
#             return (0, x)
#         return (1,)

# numbers = [8,3,1,2,5,4,7,6]
# group = {2,3,5,7}

# sorter = Sorter(group)
# numbers.sort(key=sorter)
# assert sorter.found is True

# 22

# def log(message, values):
#     if not values:
#         print(message)
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print(f'{message}: {values_str}')

# log('내 숫자는', [1, 2]) # 내 숫자는: 1, 2
# log('안녕', []) # 안녕

# def log(message, *values):
#     if not values:
#         print(message)
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print(f'{message}: {values_str}')

# log('내 숫자는', 1, 2) # 내 숫자는: 1, 2
# log('안녕') # 안녕

# favorites = [7,33,99]
# log('좋아하는 숫자는', *favorites) # 좋아하는 숫자는: 7, 33, 99

# def my_generator():
#     for i in range(10):
#         yield i
        
# def my_func(*args):
#     print(args)

# def my_func2(args):
#     print(args)
    
# it = my_generator()
# my_func(*it) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# it = my_generator()
# my_func(it) # (<generator object my_generator at 0x000001871B1C0A50>,)



# def log(sequence, message, *values):
#     if not values:
#         print(f'{sequence} - {message}')
#     else:
#         value_str = ', '.join(str(x) for x in values)
#         print(f'{sequence} - {message}: {value_str}')

# log(1, '좋아하는 숯자는', 7, 33)     # 1 - 좋아하는 숮자는: 7, 33
# log(1, '안녕')                      # 1 - 안녕
# log('좋아하는 숮자는', 7, 33)        # 좋아하는 숮자는 - 7: 33

# 23

# def remainder(num, div):
#     return num % div

# assert remainder(20, 7) == 6
# assert remainder(20, div=7) == 6
# assert remainder(num=20, 7) == 6 ## StntaxError
# assert remainder(num=20, div=7) == 6
# assert remainder(div=7, num=20) == 6

# my_kwargs = {
#     'num': 20,
#     'div': 7
# }

# def remainder(num, div):
#     return num % div

# assert remainder(**my_kwargs) == 6

# my_kwargs = {
#     'div': 7
# }

# def remainder(num, div):
#     return num % div

# assert remainder(num = 20, **my_kwargs) == 6

# def print_parameters(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# print_parameters(alpha=1.5, beta=9, 감마=4)
# # alpha: 1.5
# # beta: 9
# # 감마: 4

def flow_rate(weight_diff, time_diff):
    return weight_diff/time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg/s') # 0.167 kg/s

# 전형적인 경우 시간당 유립량이 초당 킬로그램(kg/s)입니다.
# 더 긴 시간 단위의 양을 계산하고 싶어 period 파라메터를 추가하게되면 아래와 같습니다.
# 하지만 이럴 겨웅 flow_rate의 모든 호출 부분에 period를 추가해야 하고,
# 일반적인 경우에도 period를 1로 지정해주어야 합니다.
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff/time_diff)*period

# 하지만 default 값을 설정하면 period 파라미터로 값을 전달하지 않으면 default로 설정된 값으로 인자가 전달됩니다.
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff/time_diff)*period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)