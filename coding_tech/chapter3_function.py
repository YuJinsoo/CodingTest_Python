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

def careful_divide(a: float, b: float) -> float:
    """a를 b로 나눕니다.
    Raise:
        ValueError: b가 0이어서 나눗셈을 할 수 없을 때
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력입니다.')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('잘못된 입력')
else:
    print('결과는 %.1f 입니다.' % result)

# 결과는 2.5 입니다.