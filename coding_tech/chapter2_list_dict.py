
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

# def generate_csv():
#     yield('날짜', '제조사', '모델', '연식', '가격')
#     yield('2021', '제조사1', '모델1', '연식1', '가격1')
#     yield('2021', '제조사2', '모델2', '연식2', '가격2')
#     yield('2021', '제조사3', '모델3', '연식3', '가격3')
#     yield('2021', '제조사2', '모델2', '연식2', '가격2')

# all_csv_rows = list(generate_csv())
# header = all_csv_rows[0]
# rows = all_csv_rows[1:]
# print('CSV 헤더:', header)
# print('행 수:', len(rows))
# # CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# # 행 수: 4

# ## * 연산을 활용하면
# it = generate_csv()
# header, *rows = it
# print('CSV 헤더:', header)
# print('행 수:', len(rows))
# # CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# # 행 수: 4

# 14
# numbers = [93, 86, 11, 68, 70]
# numbers.sort()
# print(numbers) # [11, 68, 70, 86, 93]

# numbers.sort(reverse=True)
# print(numbers) # [93, 86, 70, 68, 11]

# class Tool:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
    
#     def __repr__(self):
#         return f'Tool({self.name}, {self.weight})'

# tools = [
#     Tool('수준계', 3.5),
#     Tool('해머', 0.5),
#     Tool('슼크류드라이버', 1.25),
#     Tool('끌', 2.0),
# ]

# # tools.sort() # TypeError: '<' not supported between instances of 'Tool' and 'Tool'

# print('미정렬:', repr(tools))   
# # 미정렬: [Tool(수준계, 3.5), Tool(해머, 0.5), Tool(슼크류드라이버, 1.25), Tool(끌, 2.0)]

# # 이름으로 정렬
# tools.sort(key=lambda x:x.name) 
# print('정렬:', repr(tools))     
# # 정렬: [Tool(끌, 2.0), Tool(수준계, 3.5), Tool(슼크류드라이버, 1.25), Tool(해머, 0.5)]

# # 무게로 정렬
# tools.sort(key=lambda x:x.weight) 
# print('정렬:', repr(tools))
# # 정렬: [Tool(해머, 0.5), Tool(슼크류드라이버, 1.25), Tool(끌, 2.0), Tool(수준계, 3.5)]


# places = ['home', 'work', 'New York', 'Paris']
# places.sort()
# print('대소문자 구분:', places)
# places.sort(key=lambda x: x.lower())
# print('대소문자 무시:', places)
# # 대소문자 구분: ['New York', 'Paris', 'home', 'work']
# # 대소문자 무시: ['home', 'New York', 'Paris', 'work']

# saw = (5, '원형 톱')
# jackhammer = (40, '착암기')
# assert not (jackhammer < saw)

# power_tools=[
#     Tool('드릴', 4),
#     Tool('원형톱', 5),
#     Tool('착암기', 40),
#     Tool('연마기', 4),
# ]
# power_tools.sort(key=lambda x:(x.weight, x.name), reverse=True)
# print(power_tools)
# # [Tool(착암기, 40), Tool(원형톱, 5), Tool(연마기, 4), Tool(드릴, 4)]
# power_tools.sort(key=lambda x:(-x.weight, x.name), reverse=True)
# print(power_tools)
# # [Tool(연마기, 4), Tool(드릴, 4), Tool(원형톱, 5), Tool(착암기, 40)]

# # 정렬 우선순위 무게 - 이름 인 경우
# power_tools.sort(key=lambda x:x.name)  # 이름 오름차순 정렬
# power_tools.sort(key=lambda x:x.weight, reverse=True)  # 무게 내림차순 정렬
# print(power_tools)
# # [Tool(착암기, 40), Tool(원형톱, 5), Tool(드릴, 4), Tool(연마기, 4)]

# 15

# baby_names = {
#     'cat': 'kitten',
#     'dog': 'puppy',
# }
# print(baby_names) # {'cat': 'kitten', 'dog': 'puppy'}

# # 클래스 정의
# from collections.abc import MutableMapping

# class SortedDict(MutableMapping):
#     def __init__(self):
#         self.data = {}
        
#     def __getitem__(self, key):
#         return self.data[key]
    
#     def __setitem__(self, key, value):
#         self.data[key] = value

#     def __delitem__(self, key):
#         del self.data[key]

#     def __iter__(self):
#         keys = list(self.data.keys())
#         keys.sort()
#         for key in keys:
#             yield key

#     def __len__(self):
#         return len(self.data)


# def populate_ranks(votes, ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i

# def get_winner(ranks):
#     return next(iter(ranks))

# vote = {
#     'otter': 1281,
#     'polar bear': 587,
#     'fox': 863,
# }

# ranks = {}
# populate_ranks(vote, ranks)
# print(ranks)    # {'otter': 1, 'fox': 2, 'polar bear': 3}
# winner = get_winner(ranks)
# print(winner)   # otter


# sorted_rank = SortedDict()
# populate_ranks(vote, sorted_rank)
# print(sorted_rank.data)  # {'otter': 1, 'fox': 2, 'polar bear': 3}
# sorted_winner = get_winner(sorted_rank)
# print(sorted_winner)    # fox


# def get_winner(ranks):
#     for name, rank in ranks.items():
#         if rank == 1:
#             return name
        
# def get_winner(ranks):
#     if not isinstance(ranks, dict):
#         raise TypeError('dict 인스턴스가 필요합니다.')
#     return next(iter(ranks))

# from typing import Dict, MutableMapping

# def populate_ranks(votes: Dict[str, int],
#                    ranks: Dict[str, int]) -> None:
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i

# def get_winner(ranks: Dict[str, int]) -> str:
#     return next(iter(ranks))


# 16

# counters = {
#     '품퍼니켈':2,
#     '사워도우':1,
# }
# key = '밀'

# # try catch
# try:
#     count = counters[key] ## 없는 키에 접근하면 KeyError발생
# except KeyError:
#     count = 0

# counters[key] = count + 1

# # get 메서드를 사용해서 간단하게 구현
# count = counters.get(key, 0)
# counters[key] = count + 1

# votes = {
#     '바게트': ['철수', '순이'],
#     '치아파바': ['하니', '유리'],
# }

# key = '브리오슈'
# who = '단이'

# ## in 사용
# if key in votes:
#     names = votes[key]
# else:
#     votes[key] = names = [] # 두줄 짜리를 한줄에.... 이게 가능하네?

# names.append(who) # 참조를 통해 연결되어 있으므로 names에 값을 넣으면 딕셔너리에 들어감
# print(votes) 
# # {'바게트': ['철수', '순이'], '치아파바': ['하니', '유리'], '브리오슈': ['단이']}

# votes = {
#     '바게트': ['철수', '순이'],
#     '치아파바': ['하니', '유리'],
# }
# key = '브리오슈'
# who = '단이'
# ## try 사용
# try:
#     names = votes[key]
# except KeyError:
#     votes[key] = names = []

# names.append(who)
# # {'바게트': ['철수', '순이'], '치아파바': ['하니', '유리'], '브리오슈': ['단이']}

# ## get 사용
# votes = {
#     '바게트': ['철수', '순이'],
#     '치아파바': ['하니', '유리'],
# }
# key = '브리오슈'
# who = '단이'
# names = votes.get(key)
# if names is None:
#     votes[key] = names = []
# names.append(who)
# print(votes)
# # {'바게트': ['철수', '순이'], '치아파바': ['하니', '유리'], '브리오슈': ['단이']}


# data = {}
# key = 'foo'
# value = []
# data.setdefault(key, value)
# print('이전:', data)    # 이전: {'foo': []}
# value.append('hello')
# print('이후:', data)    # 이후: {'foo': ['hello']}


# 17
# visits = {
#     '미국': {'뉴욕', '로스엔젤레스'},
#     '일본': {'하코네' },
# }

# ## dictionary get과 대입식 := 적용
# if (japan := visits.get('일본')) is None:
#     visits['일본'] = japan = set()
# japan.add('교토')
# print(visits)
# # {'미국': {'로스엔젤레스', '뉴욕'}, '일본': {'교토', '하코네'}}

# ## setdefault
# ## 매우 짧다
# visits.setdefault('프랑스', set()).add('칸')
# print(visits)
# # {'미국': {'로스엔젤레스', '뉴욕'}, '일본': {'교토', '하코네'}, '프랑스': {'칸'}}


# class Visits():
#     def __init__(self):
#         self.data = {}
    
#     def add(self, country, city):
#         city_set = self.data.setdefault(country, set())
#         city_set.add(city)

# visits = Visits()
# visits.add('러시아', '예카테린부르크')
# visits.add('탄자니아', '잔지바르')
# print(visits.data) # {'러시아': {'예카테린부르크'}, '탄자니아': {'잔지바르'}}

from collections import defaultdict
class Visits():
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('영국', '바스')
visits.add('영국', '런던')
visits.add('탄자니아', '잔지바르')
print(visits.data) # defaultdict(<class 'set'>, {'영국': {'런던', '바스'}, '탄자니아': {'잔지바르'}})
py_dict = dict(visits.data)
print(type(py_dict), py_dict) ## dict로 바로 변환 가능