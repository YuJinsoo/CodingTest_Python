# 27
a= [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_squares = [x**2 for x in a if x%2==0]
print(even_squares) # [4, 16, 36, 64, 100]

alt = map(lambda x:x**2, filter(lambda x:x%2==0, a))
print(alt) # [4, 16, 36, 64, 100]

even_squares_dict = {x: x**2 for x in a if x%2==0}
threes_cubed_set = {x**3 for x in a if x%3 == 0}
print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(threes_cubed_set) # {216, 729, 27}

alt_dict = dict(map(lambda x: (x,x**2), filter(lambda x: x%2==0, a)))
alt_set = set(map(lambda x:x**3, filter(lambda x:x%3==0, a)))
print(alt_dict)
print(alt_set)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# {216, 729, 27}