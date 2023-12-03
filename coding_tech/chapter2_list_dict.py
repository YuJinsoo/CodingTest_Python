
# 11
# # a = ['a','b','c','d','e','f','g','h']
# print('가운데 2개:', a[3:5]) # 가운데 2개: ['d', 'e']
# print('마지막을 제외한 나머지:', a[0:7]) # 마지막을 제외한 나머지: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# assert a[0:5] == a[:5]
# assert a[3:len(a)] == a[3:]

# a = ['a','b','c','d','e','f','g','h']
# print(a[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(a[:5])    # ['a', 'b', 'c', 'd', 'e']
# print(a[:-1])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(a[4:])    #                     ['e', 'f', 'g', 'h']
# print(a[-3:])   #                          ['f', 'g', 'h']
# print(a[2:5])   #           ['c', 'd', 'e']
# print(a[2:-1])  #           ['c', 'd', 'e', 'f', 'g']
# print(a[-3:-1]) #                          ['f', 'g']
# print(a[:20])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(a[-20:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# a = ['a','b','c','d','e','f','g','h']

# b = a[:3]
# print('인덱싱 할당 이전:', b)
# b[1] = 99 # 하나에 할당
# print('인덱싱 할당 이후:', b)
# print('원본(변화없음):', a)

# # 인덱싱 할당 이전: ['a', 'b', 'c']
# # 인덱싱 할당 이후: ['a', 99, 'c']
# # 원본(변화없음): ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# # 대입되는 리스트 값과 슬라이싱 부분의 길이는 관계없습니다.
# a = ['a','b','c','d','e','f','g','h']
# print('슬라이싱 할당 이전:', a)
# a[2:7] = [99, 22, 14]
# print('슬라이싱 할당 이후:', a)
# # 슬라이싱 할당 이전: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# # 슬라이싱 할당 이후: ['a', 'b', 99, 22, 14, 'h']

# a = ['a','b','c','d','e','f','g','h']
# b = a[:] ## 전체 리스트 복사되어 값은 같지만 다른 list
# assert b == a and b is not a
# print('a id:', id(a)) # a id: 1996685917440
# print('b id:', id(b)) # b id: 1996685924672


# b = a ## 복사되는 것이 아니라 얕은복사 되어서 같은 list를 가리키는 상황
# print('이전 a:', a)  # 이전 a: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print('이전 b:', b)  # 이전 b: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a[:] = [101, 102, 103]
# assert a is b
# print('이후 a:', a)   # 이후 a: [101, 102, 103]
# print('a id:', id(a)) # a id: 1941179284736
# print('b id:', id(b)) # b id: 1941179284736

# 12
# x = ['빨','주','노','초','파','남','보']
# odd = x[::2]    # ['빨', '노', '파', '보']
# even = x[1::2]  # ['주', '초', '남']

# x = b'mongoose'
# y = x[::-1]
# print(y)


# w = '스시'
# x = w.encode('utf-8')
# y = x[::-1]
# z = y.decode('utf-8')
# # Traceback (most recent call last):
# #   File "c:\Users\ABO\Desktop\Study_Python\coding_tech\chapter2_list_dict.py", line 70, in <module>
# #     z = y.decode('utf-8')
# # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 0: invalid start byte

# x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(x[::2])       # ['a', 'c', 'e', 'g']
# print(x[::-2])      # ['h', 'f', 'd', 'b']

# print(x[2::2])      # ['c', 'e', 'g']
# print(x[-2:2:-2])   # ['g', 'e']
# print(x[2:2:-2])    # []

# y = x[::2] # ['a', 'c', 'e', 'g']
# z = y[1:-1] # ['c', 'e']

# 13

# car_ages = [0,9,4,8,7,20,19,1,6,15]
# car_ages_desc = sorted(car_ages, reverse=True)

# # 일반적으로 슬라이싱과 인덱스를 사용하면 이렇게 가져와야함
# oldest = car_ages_desc[0]
# second_oldest = car_ages_desc[1]
# others = car_ages_desc[2:]              # 나머지
# print(oldest, second_oldest, others)    # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# # # 하지만 나머지 언패킹을 사용하면 간단하게 처리할 수 있습니다.

# oldest, second_oldest, *others = car_ages_desc
# print(oldest, second_oldest, others)    # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]


# oldest, *others, youngest = car_ages_desc
# print(oldest, others, youngest)         # 20 [19, 15, 9, 8, 7, 6, 4, 1] 0

# *others, second_youngest, youngest = car_ages_desc
# print(others, second_youngest, youngest)# [20, 19, 15, 9, 8, 7, 6, 4] 1 0

# # *others = car_ages # SyntaxError: starred assignment target must be in a list or tuple
# start, *part1, *part2, end = car_ages_desc

# car_inventory = {
#     '시내': ('그랜져', '아반떼', '티코'),
#     '공항': ('제네시스', '소나타', 'K5', '엑센트'),
# }

# ((loc1, (best1, *rest1)),
#  (loc2, (best2, *rest2))) = car_inventory.items()

# print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)}종')
# print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)}종')
# # 시내 최고는 그랜져, 나머지는 2종
# # 공항 최고는 제네시스, 나머지는 3종

# short_list = [1, 2]
# first, second, *others = short_list
# print(first, second, others) # 1 2 []


def generate_csv():
    yield('날짜', '제조사', '모델', '연식', '가격')
    yield('2021', '제조사1', '모델1', '연식1', '가격1')
    yield('2021', '제조사2', '모델2', '연식2', '가격2')
    yield('2021', '제조사3', '모델3', '연식3', '가격3')
    yield('2021', '제조사2', '모델2', '연식2', '가격2')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수:', len(rows))
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수: 4

## * 연산을 활용하면
it = generate_csv()
header, *rows = it
print('CSV 헤더:', header)
print('행 수:', len(rows))
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수: 4