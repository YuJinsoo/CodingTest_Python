## 프로그래머스 > 코딩테스트 입문

### 문제 : 저주의 숫자3

- https://school.programmers.co.kr/learn/courses/30/lessons/120871

```python
# 1
def solution(n):
    num_list = [i for i in range(1001) if i%3 !=0 and '3' not in str(i)]
    return num_list[n-1]

# 2
def solution(n):
    number = 1
    xnum = 1
    #3의 배수면 1 더해주고
    # 3이 들어가면 1 더해주고..

    while number < n:
        number += 1
        xnum += 1
        while xnum%3 ==0 or '3' in str(xnum):
            xnum +=1

    return xnum
```

### 문제 : 배열의 평균값

- https://school.programmers.co.kr/learn/courses/30/lessons/120817

```python
# 1
def solution(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# 2 다차원 배열의 경우 numpy 사용 numpy.sum()!
import numpy as np

def solution(numbers):
    return np.sum(numbers)/len(numbers)
```

### 문제 : 짝수의 합

- https://school.programmers.co.kr/learn/courses/30/lessons/120831

```python
# 1
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 ==0:
            answer += i
    return answer

# 2
def solution(n):
    return sum([i for i in range(n+1) if i%2==0])

# 3
def solution(n):
    li = list(filter(lambda x: x%2 ==0, range(n+1)))
    return sum(li)

# 4
def solution(n):
    return sum(list(range(2, n+1, 2)))
```

### 문제 : 중복된 숫자 개수

- https://school.programmers.co.kr/learn/courses/30/lessons/120583

```python
#1
def solution(array, n):
    answer = array.count(n)
    return answer

#2  collections 의 Counter!
from collections import Counter

def solution(array, n):
    return 0 if Counter(array).get(n) == None else Counter(array).get(n)

```

### 문제 : 머쓱이보다 키 큰 사람

- https://school.programmers.co.kr/learn/courses/30/lessons/120585

```python
# 1
def solution(array, height):
    return len(list(filter(lambda x : x> height, array)))

#2
def solution(array, height):
    return len([i for i in array if i > height])

#3
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
```

### 문제 : 양꼬치

- https://school.programmers.co.kr/learn/courses/30/lessons/120830

```python
#1
def solution(n, k):
    answer = (n*12000) + (k-(n//10))*2000
    return answer

```

### 문제 : 자릿수 더하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120906

```python
#1
def solution(n):
    return sum([int(i) for i in list(str(n))])

#2
def solution(n):
    return sum(list(map(int, str(n))))

#3
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
```

### 문제 : 피자 나눠 먹기(3)

- https://school.programmers.co.kr/learn/courses/30/lessons/120816

```python
#1
def solution(slice, n):
    if slice >= n:
        answer = 1
    else:
        if n%slice == 0:
            answer = n/slice
        else:
            answer = n//slice + 1

    return answer

#2
def solution(slice, n):
    for i in range(51):
        if n <= i * slice:
            break
    return i

```

### 문제 : 문자열 뒤집기

- https://school.programmers.co.kr/learn/courses/30/lessons/120822

```python
#1
def solution(my_string):
    return my_string[::-1]

#2
def solution(my_string):
    return ''.join(reversed(my_string)) # list로 바꿔도 되고 안바꿔도 됨

```

### 배열 원소의 길이

- https://school.programmers.co.kr/learn/courses/30/lessons/120854

```python
#1
def solution(strlist):
    return [len(i) for i in strlist]

#2
def solution(strlist):
    return list(map(lambda x : len(x), strlist))

```

### 문제 : 피자 나눠 먹기 (1)

- https://school.programmers.co.kr/learn/courses/30/lessons/120814

```python
#1
def solution(n):
    return n // 7 if n % 7 == 0 else n // 7 + 1

#2 math 모듈 사용. math.ceil
import math

def solution(n):
    return math.ceil(n / 7)

```

### 문제 : 문자열안에 문자열

- https://school.programmers.co.kr/learn/courses/30/lessons/120908

```python
#1
def solution(str1, str2):
    return 1 if str2 in str1 else 2

#2 str의 find 는 없으면 -1 을 있으면 index를 리턴해준다!
def solution(str1, str2):
    return 1 if str1.find(str2) != -1 else 2

# .index(찾는문자) 는 없으면 에러발생

```

### 문제 : 짝수 홀수 개수

- https://school.programmers.co.kr/learn/courses/30/lessons/120824

```python
#1
def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i%2 ==0 :
            even += 1
        else:
            odd += 1

    answer = [even, odd]
    return answer

#2
def solution(num_list):
    even = len(list(filter(lambda x: x%2==0, num_list)))
    odd = len(list(filter(lambda x: x%2, num_list)))
    return [even, odd]

#3
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2] += 1
    return answer

#4
def solution(num_list):
    li = list(map(lambda x: x%2, num_list))
    return [li.count(0), li.count(1)]


```

### 문제 : 배열 뒤집기

- https://school.programmers.co.kr/learn/courses/30/lessons/120821

```python
#1
def solution(num_list):
    return num_list[::-1]

#2
def solution(num_list):
    asnwer = []
    for i in num_list:
        asnwer.insert(0, i)
    return asnwer

#3
def solution(num_list):
    return list(reversed(num_list))

#4
def solution(num_list):
    num_list.reverse()
    return num_list

```

### 문제 : 가장 큰 수 찾기

- https://school.programmers.co.kr/learn/courses/30/lessons/120899

```python
#1
def solution(array):
    value = max(array)
    idx = array.index(value)
    return [value, idx]
    # return [max(array), array.index(max(array))]

#2
def solution(array):
    a = max(enumerate(array), key = lambda x : x[1])
    return [a[1], a[0]]

```

### 문제 : 아이스 아메리카노

- https://school.programmers.co.kr/learn/courses/30/lessons/120819

```python
#1
def solution(money):
    answer = [money//5500, money-(money//5500)*5500]
    return answer

#2
def solution(money):
    return [money//5500, money%5500]

```

### 문제 : 최대값 만들기(1)

- https://school.programmers.co.kr/learn/courses/30/lessons/120847

```python
#1
def solution(numbers):
    m1 = numbers.pop(numbers.index(max(numbers)))
    m2 = numbers.pop(numbers.index(max(numbers)))
    return m1*m2

#2
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

#3
def solution(numbers):
    li = list(reversed(sorted(numbers))) ## sorted의 return은 list
    return li[0] * li[1]

#4

```

### 문제 : 약수 구하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120897

```python
#1
def solution(n):
    answer = [i for i in range(1, n+1) if n % i == 0]
    return answer

#2
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

```

### 문제 : 배열 두 배 만들기

- https://school.programmers.co.kr/learn/courses/30/lessons/120809

```python
#1
def solution(numbers):
    return [i*2 for i in numbers]

#2
def solution(numbers):
    return list(map(lambda x: x*2, numbers))

#3
import numpy as np

def solution(numbers):
    return (np.array(numbers) * 2).tolist()
```

### 문제 : n의 배수 고르기

- https://school.programmers.co.kr/learn/courses/30/lessons/120905

```python
#1
def solution(n, numlist):
    return list(filter(lambda x : x%n == 0, numlist))

#2
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]

#3
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer
```

### 문제 : 제곱수 판별하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120909

```python
#1
def solution(n):
    return 1 if n**0.5 == int(n**0.5) else 2

#2
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

## isinstance(n**0.5, int) 는 항상 False가 나온다...
```

### 문제 : 순서쌍의 개수

- https://school.programmers.co.kr/learn/courses/30/lessons/120836

```python
#1
def solution(n):
    # 약수에다가 어떤 수를 곱하면 n이 되므로 약수의 개수를 구하면 됨
    return len([i for i in range(1, n+1) if n%i == 0])

#2
def solution(n):
    return len(list(filter(lambda x : n%x == 0, range(1, n+1))))

```

### 문제 : 모음 제거

- https://school.programmers.co.kr/learn/courses/30/lessons/120849

```python
#1
def solution(my_string):
    li = [i for i in my_string if i not in 'aeiou']
    answer = ''
    for i in li:
        answer += i
    return answer

#2 string 메서드 replace
def solution(my_string):
    answer = my_string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    return answer

#3 정규 표현식. 파워풀하네....
import re

def solution(my_string):
    return re.sub(r"[aeiou]", "", my_string)

```

### 문제 : 배열의 유사도

- https://school.programmers.co.kr/learn/courses/30/lessons/120903

```python
#1
def solution(s1, s2):
    tmp = set(s1).intersection(set(s2))
    answer = len(tmp)
    return answer

#2
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer +=1
    return answer

#3
# 특이한 풀이
def solution(s1, s2):
    dic = {i:1 for i in s1}
    answer = sum(dic.get(j,0)for j in s2) # .get('key', default) #key가 없을 때 리턴할 값 = default
    return answer
```

### 문제 : 특정 문자 제거하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120826

```python
#1
def solution(my_string, letter):
    return my_string.replace(letter,'')

#2 정규표현식. 어케하는거여...
import re

def solution(my_string, letter):
    s = re.sub(letter, "", my_string)
    return s
```

### 문제 : 숨어있는 숫자의 덧셈(1)

- https://school.programmers.co.kr/learn/courses/30/lessons/120851

```python
#1
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit()) # [] 로 안묶어줘도 잘 되던데..??

#2
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])

#3
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isnumeric():
            answer += int(i)
    return answer

#4 정규표현식
import re

def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))
```

### 문제 : 숨어있는 숫자의 덧셈(1)

- https://school.programmers.co.kr/learn/courses/30/lessons/120851

```python
#1
def solution(my_string):
    li = []
    for i in my_string:
        li.append(i.lower() if i.isupper() else i.upper())
    answer = ''.join(li)
    return answer

#2
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
```

### 문제 : 가위 바위 보

- https://school.programmers.co.kr/learn/courses/30/lessons/120839

```python
#1
def solution(rsp):
    d = {'2':'0', '5':'2', '0':'5'}
    answer = ''
    for i in rsp:
        answer += d[i]
    return answer

```

### 문제 : 문자열 정렬하기(2)

- https://school.programmers.co.kr/learn/courses/30/lessons/120911

```python
## sorted에 list뿐만 아니라 str도 그냥 넣어도 되나봅니다
#1
def solution(my_string):
    answer = ''.join(sorted([i for i in my_string.lower()]))
    return answer

#2
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

```

### 문제 : 배열 회전시키기

- https://school.programmers.co.kr/learn/courses/30/lessons/120844

```python
#1
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = [numbers[i] for i in range(len(numbers)-1) ]
        answer.insert(0, numbers.pop())
    else:
        answer = [numbers[i] for i in range(1,len(numbers)) ]
        answer.append(numbers.pop(0))

    return answer

#2
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right": direction = 1
    if direction == "left": direction = -1
    numbers.rotate(direction)
    return list(numbers)


```
