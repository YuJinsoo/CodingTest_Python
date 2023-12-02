
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