# 27
# a= [1,2,3,4,5,6,7,8,9,10]
# squares = [x**2 for x in a]
# print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# even_squares = [x**2 for x in a if x%2==0]
# print(even_squares) # [4, 16, 36, 64, 100]

# alt = map(lambda x:x**2, filter(lambda x:x%2==0, a))
# print(alt) # [4, 16, 36, 64, 100]

# even_squares_dict = {x: x**2 for x in a if x%2==0}
# threes_cubed_set = {x**3 for x in a if x%3 == 0}
# print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# print(threes_cubed_set) # {216, 729, 27}

# alt_dict = dict(map(lambda x: (x,x**2), filter(lambda x: x%2==0, a)))
# alt_set = set(map(lambda x:x**3, filter(lambda x:x%3==0, a)))
# print(alt_dict)
# print(alt_set)
# # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# # {216, 729, 27}

# 28

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# flat = [x for row in matrix for x in row]
# print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squared = [[x**2 for x in row] for row in matrix]
# print(squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]] 

# my_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
# flat = [x for sublist1 in my_list
#         for sublist2 in sublist1
#         for x in sublist2]

# print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# flat2 = []
# for sublist1 in my_list:
#     for sublist2 in sublist1:
#         flat2.extend(sublist2)

# print(flat2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# filtered = [[x for x in row if x%3==0] for row in matrix if sum(row)>=10]
# print(filtered) # [[6], [9]]


# 29

# stock = {
#     '못': 125,
#     '나사못': 35,
#     '나비너트': 8,
#     '와셔': 24,
# }

# order = ['나사못', '나비너트', '클립']

# def get_batches(count, size):
#     return count//size

# result = {}
# for name in order:
#     count = stock.get(name, 0)
#     batches = get_batches(count, 8)
#     if batches:
#         result[name] = batches
# print(result) # {'나사못': 4, '나비너트': 1}

# found = {name: get_batches(stock.get(name, 0), 8) for name in order if get_batches(stock.get(name, 0), 8)}
# print(found) #{'나사못': 4, '나비너트': 1}


# real_found = {name: batches 
#               for name in order 
#               if (batches := get_batches(stock.get(name, 0), 8))}
# print(real_found) #{'나사못': 4, '나비너트': 1}

# # NameError: name 'tenth' is not defined
# # result = {name: (tenth := count // 10) for name, count in stock.items() if tenth >0}


# result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
# print(result) # {'못': 12, '나사못': 3, '와셔': 2}

# half = [(last := count // 2) for count in stock.values()]
# print(f'{half}의 마지막 원소는 {last}') #  [62, 17, 4, 12]의 마지막 원소는 12


# for count in stock.values():
#     pass
# print(f'{list(stock.values())}의 마지막 원소는 {count}')
# # [125, 35, 8, 24]의 마지막 원소는 24

# half = [count2 // 2 for count2 in stock.values()]
# print(half)
# # print(count2) #NameError: name 'count2' is not defined

# found = ((name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8)))

# print(next(found)) # ('나사못', 4)
# print(next(found)) # ('나비너트', 1)

# 30
# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             result.append(index + 1)
#     return result

# address = '컴퓨터(영어: Computer, 문화어: 콤퓨터  , 순화어: 전산기)는 진공관'

# print(index_words(address)) # [0, 8, 18, 23, 27, 28, 30, 35, 41]

# ## 개선
# def index_word_iter(text):
#     if text:
#         yield 0
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             yield index + 1

# it = index_word_iter(address)
# print(next(it)) # 0
# print(next(it)) # 8


# 31

# def normalize(numbers):
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value / total
#         result.append(percent)
#     return result

# visits = [15,35, 80]
# percentages = normalize(visits)
# print(percentages)
# assert sum(visits) == 100


# ##
# def read_visits(data_path):
#     with open(data_path) as f:
#         for line in f:
#             yield int(line)

# it = read_visits('my_numbers.txt')
# percentages = normalize(it)
# print(percentages) ## []


# ##
# def normalize_copy(numbers):
#     numbers_copy = list(numbers)
#     total = sum(numbers_copy)
#     result = []
#     for value in numbers_copy:
#         percent = 100 * value / total
#         result.append(percent)
#     return result

# def read_visits(data_path):
#     with open(data_path) as f:
#         for line in f:
#             yield int(line)

# it = read_visits('my_numbers.txt')
# percentages = normalize(it)
# print(percentages) ## 정확한 출력이 나옴


# ## 새 컨테이너 정의
# class ReadVisits:
#     def __init__(self, data_path):
#         self.data_path = data_path
    
#     def __iter__(self):
#         with open(self.data_path) as f:
#             for line in f:
#                 yield int(line)

# visits = ReadVisits('my_numbers.txt')
# percentages = normalize(visits)
# print(percentages) ## 정상
# assert sum(percentages) == 100 ## 정상


# ##
# from collections.abc import Iterator

# def normalize_defensive(numbers):
#     if isinstance(numbers, Iterator): ## True가 되면 __iter__가 없는 객체라는 뜻.
#         raise TypeError('컨테이너를 제공해야 합니다')
#     total = sum(numbers) ## __iter__ 호출
#     result = []
#     for value in numbers: ## __iter__ 호출
#         percent = 100 * value / total
#         result.append(percent)
#     return result

# 33

# #움직임 함수와 멈춤함수
# def move(period, speed):
#     for _ in range(period):
#         yield speed

# def pause(delay):
#     for _ in range(delay):
#         yield 0

# # 애니메이션 동작은
# def animate():
#     for delta in move(4, 5.0):
#         yield delta
#     for delta in pause(3):
#         yield delta
#     for delta in move(2, 3.0):
#         yield delta

# def render(delta):
#     print(f'Delta: {delta:.1f}')
    
# def run(func):
#     for delta in func():
#         render(delta)

# run(animate)
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 0.0
# # Delta: 0.0
# # Delta: 0.0
# # Delta: 3.0
# # Delta: 3.0


# def animate_composed():
#     yield from move(4, 5.0)
#     yield from pause(3)
#     yield from move(2, 3.0)

# run(animate_composed)
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 5.0
# # Delta: 0.0
# # Delta: 0.0
# # Delta: 0.0
# # Delta: 3.0
# # Delta: 3.0

# import timeit

# ## 제너레이터
# def child():
#     for i in range(1_000_000):
#         yield i

# ## for문으로 호출
# def slow():
#     for i in child():
#         yield i

# ## yield from으로 호출
# def fast():
#     yield from child()

# baseline = timeit.timeit(
#     stmt='for _ in slow(): pass',
#     globals=globals(),
#     number=50)
# print(f'수동 내포: {baseline:.2f}s')

# comparison = timeit.timeit(
#     stmt='for _ in fast(): pass',
#     globals=globals(),
#     number=50)
# print(f'합성 사용: {comparison:.2f}s')

# reduction = -(comparison - baseline) / baseline
# print(f'{reduction:.1%} 시간이 적게 듦')

# # 수동 내포: 3.15s
# # 합성 사용: 2.64s
# # 16.1% 시간이 적게 듦


# 34
## 주어진 간격과 진폭에 따른 사인파를 생성하는 함수
# import math

# def wave(amplitude, steps):
#     step_size = 2 * math.pi / steps
#     for step in range(steps):
#         radians = step * step_size
#         fraction = math.sin(radians)
#         output = amplitude * fraction
#         yield output

# # wave 제너레이터를 이터레이션하면서 진폭이 고정된 파형 신호를 송신
# def transmit(output):
#     if output is None:
#         print(f'출력: None')
#     else:
#         print(f'출력: {output:>5.1f}')

# def run(it):
#     for output in it:
#             transmit(output)

# run(wave(3.0, 8))
# # 출력:   0.0
# # 출력:   2.1
# # 출력:   3.0
# # 출력:   2.1
# # 출력:   0.0
# # 출력:  -2.1
# # 출력:  -3.0
# # 출력:  -2.1

# ## 

def my_generator():
    received = yield 1
    print(f'받은 값 = {received}')
    
it = iter(my_generator())
output = next(it)
print(f'출력값 = {output}')

try:
    next(it)
except StopIteration:
    pass

# 출력값 = 1
# 받은 값 = None

it = iter(my_generator())
output = it.send(None) # 첫 제너레이터 출력을 얻음
print(f'출력값 = {output}')

try:
    it.send('안녕!') # 값을 제너레이터에 넣음
except StopIteration:
    pass
# 출력값 = 1
# 받은 값 = 안녕!



import math

# send로 진폭을 전달하여 aplitude에 값을 저장
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield   # 초기 진폭을 받음
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # 다음 진폭을 받음

# wave 제너레이터를 이터레이션하면서 진폭이 고정된 파형 신호를 송신
def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')


# run함수를 바꿔 매 이터레이션마다 
# 변조에 사용할 진폭을 wave_modulating 제너레이터에 스트리밍 하도록 만든다.

def run_modulating(it):
    amplitudes = [ None, 7,7,7,2,2,2,2,10,10,10,10,10 ]
    for amp in amplitudes:
        output = it.send(amp)
        transmit(output)

run_modulating(wave_modulating(12))
# 출력: None
# 출력:   0.0
# 출력:   3.5
# 출력:   6.1
# 출력:   2.0
# 출력:   1.7
# 출력:   1.0
# 출력:   0.0
# 출력:  -5.0
# 출력:  -8.7
# 출력: -10.0
# 출력:  -8.7
# 출력:  -5.0

def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())
# 출력: None
# 출력:   0.0
# 출력:   6.1
# 출력:  -6.1
# 출력: None
# 출력:   0.0
# 출력:   2.0
# 출력:   0.0
# 출력: -10.0
# 출력: None
# 출력:   0.0
# 출력:   9.5
# 출력:   5.9

print('======================')
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # 전달한 이터레이터 값을 순서대로 입력
        output = amplitude * fraction
        yield output
        
def complex_wave_casecading(amplitude_it):
    yield from wave_cascading(amplitude_it,3)
    yield from wave_cascading(amplitude_it,4)
    yield from wave_cascading(amplitude_it,5)
    
def run_cascading():
    amplitude_it = [7,7,7,2,2,2,2,10,10,10,10,10]
    it = complex_wave_casecading(iter(amplitude_it))
    for amp in amplitude_it:
        output = next(it)
        transmit(output)
    
run_cascading()
# 출력:   0.0
# 출력:   6.1
# 출력:  -6.1
# 출력:   0.0
# 출력:   2.0
# 출력:   0.0
# 출력:  -2.0
# 출력:   0.0
# 출력:   9.5
# 출력:   5.9
# 출력:  -5.9
# 출력:  -9.5