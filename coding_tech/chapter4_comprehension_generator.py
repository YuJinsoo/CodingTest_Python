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

stock = {
    '못': 125,
    '나사못': 35,
    '나비너트': 8,
    '와셔': 24,
}

order = ['나사못', '나비너트', '클립']

def get_batches(count, size):
    return count//size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
print(result) # {'나사못': 4, '나비너트': 1}

found = {name: get_batches(stock.get(name, 0), 8) for name in order if get_batches(stock.get(name, 0), 8)}
print(found) #{'나사못': 4, '나비너트': 1}


real_found = {name: batches 
              for name in order 
              if (batches := get_batches(stock.get(name, 0), 8))}
print(real_found) #{'나사못': 4, '나비너트': 1}

# NameError: name 'tenth' is not defined
# result = {name: (tenth := count // 10) for name, count in stock.items() if tenth >0}


result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(result) # {'못': 12, '나사못': 3, '와셔': 2}

half = [(last := count // 2) for count in stock.values()]
print(f'{half}의 마지막 원소는 {last}') #  [62, 17, 4, 12]의 마지막 원소는 12


for count in stock.values():
    pass
print(f'{list(stock.values())}의 마지막 원소는 {count}')
# [125, 35, 8, 24]의 마지막 원소는 24

half = [count2 // 2 for count2 in stock.values()]
print(half)
# print(count2) #NameError: name 'count2' is not defined

found = ((name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8)))

print(next(found)) # ('나사못', 4)
print(next(found)) # ('나비너트', 1)

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