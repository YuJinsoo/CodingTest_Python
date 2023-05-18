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
    return len(list(filter(lambda x : x > height, array)))

#2
def solution(array, height):
    return len([i for i in array if i > height])

#3
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

#4 list comprehension
def solution(array, height):
    li = [i for i in array if i > height]
    return len(li)
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

#2 변수를 안썼기 때문에 #1보다 공간복잡도가 더 우위
def solution(numbers, direction):
    if direction == 'right':
        tmp = numbers.pop()
        numbers.insert(0, tmp)
    else:
        tmp = numbers.pop(0)
        numbers.append(tmp)

    return numbers

#2-1 더 간소화
def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop()) ## 이렇게 해도 = 좌측에 있는 numbers에 pop적용된상태로됨
    else:
        numbers.append(numbers.pop(0))

    return numbers

#3 deque 사용. 회전초밥, 라디오방송순서 등
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right": direction = 1
    if direction == "left": direction = -1
    numbers.rotate(direction)
    return list(numbers)

```

### 문제 : 배열 회전시키기

- https://school.programmers.co.kr/learn/courses/30/lessons/120834

```python
#1
def solution(age):
    # 'a' = 97
    answer = ''
    for i in str(age):
        answer += chr(int(i)+97)

    return answer

# chr는 숫자를 유니코드 문자로
# 'A' = 65
# 'a' = 97
```

### 문제 : 암호 해독

- https://school.programmers.co.kr/learn/courses/30/lessons/120892

```python
#1
def solution(cipher, code):
    li = [cipher[i] for i in range(code-1, len(cipher), code)]
    answer = ''.join(li)
    return answer

#2
def solution(cipher, code):
    return cipher[code-1::code]
```

### 문제 : 최대값 만들기(2)

- https://school.programmers.co.kr/learn/courses/30/lessons/120862

```python
#1
def solution(numbers):
    li = sorted(numbers, reverse=True)
    if li[0]*li[1] >= li[-1]*li[-2]:
        return li[0]*li[1]
    return li[-1]*li[-2]

#2 두 값 비교... max활용
def solution(numbers):
    li = sorted(numbers, reverse=True)
    return max(li[-1]*li[-2], li[-1]*li[-2])
```

### 문제 : 369게임

- https://school.programmers.co.kr/learn/courses/30/lessons/120891

```python
#1
def solution(order):
    answer = 0
    for i in str(order):
        if int(i) % 3 == 0 and int(i) != 0: answer +=1
    return answer

#2
def solution(order):
    answer = sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
    return answer

#3 정규표현식!
import re

def solution(order):
    answer = len(re.findall('[369]', str(order)))
    return answer
```

### 문제 : 합성수 찾기

- https://school.programmers.co.kr/learn/courses/30/lessons/120846

```python
#1
def solution(n):
    li = []
    for i in range(1, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0 : count += 1
        if count >= 3:
            li.append(i)

    answer = len(li)
    return answer

#2
def solution(n):
    answer = 0
    if n == 1 or n == 2 or n == 3:
        return 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer

```

### 문제 : 모스부호(1)

- https://school.programmers.co.kr/learn/courses/30/lessons/120838

```python
#1
def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    answer = ''
    return ''.join(map(lambda x: morse.get(x) ,letter.split(' ')))

#2
def solution(letter):

    answer = ''
    for i in letter.split(' '):
        answer += morse.get(i)

    return answer

```

### 문제 : 중복된 문자 제거- 12월 14일

- https://school.programmers.co.kr/learn/courses/30/lessons/120838

```python
#1
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

#2
## dict에 순서가 있고 key가 유일하다는 점을 활용한 풀이방법
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

#3 살짝 억지긴 하지만 set 이용
def solution(my_string):
    s = set(my_string)
    answer = ''
    for i in my_string:
        if i in s:
            answer += i
            s.remove(i)

    return answer
```

### 문제 : 2차원으로 만들기

- https://school.programmers.co.kr/learn/courses/30/lessons/120842

```python
#1
def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        li = []
        for j in range(n):
            li.append(num_list[i+j])
        answer.append(li)

    return answer

#2
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()

# 참고
# np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(4, 2) # 4행 2열
```

### 문제 : A로 B 만들기

- https://school.programmers.co.kr/learn/courses/30/lessons/120842

```python
#1
def solution(before, after):
    if len(before) != len(after):
        answer = 0
    sb = set(before)
    sa = set(before)

    if sb == sb.intersection(sa):
        for i in sb:
            if before.count(i) != after.count(i):
                answer = 0
                break;
            answer = 1
    return answer

#2 1개씩 비교하면서 한쪽 리스트에서 제외, 없는순간 0
def solution(before, after):
    if len(before) != len(after):
        return 0
    before = list(before)
    after = list(after)
    for i in before:
        if not i in after:
            return 0
        else:
            after.remove(i)
    return 1

#3 제일 깔끔한듯?
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0

#4
def solution(before, after):
    return 1 if sorted(list(before)) == sorted(list(after)) else 0
```

### 문제 : 팩토리얼 - 12월 15일

- https://school.programmers.co.kr/learn/courses/30/lessons/120848

```python
#1
def factorial(k):
        if k == 0 or k == 1:
            return 1
        return k * factorial(k-1)

def solution(n):
    idx = 1
    while factorial(idx) <= n:
        idx += 1
    answer = idx - 1
    return answer

#2
def solution(n):
    f = 1
    i = 1
    while f <= n:
        i += 1
        f *= i
    return i - 1

#3 math 의 factorial
from math import factorial

def solution(n):
    i = 1
    while factorial(i) <= n:
        i += 1
    return i - 1

```

### 문제 : 가까운 수

- https://school.programmers.co.kr/learn/courses/30/lessons/120848

```python
#1
def solution(array, n):
    array.sort()
    li = [abs(i-n) for i in array]
    idx = li.index(min(li))
    answer = array[idx]
    return answer

#2
array = [3, 10, 25, 28, 15]
n = 20

# 정렬되는 값은 array의 요소들
# 기준은 거리이기 때문에 abs(x-n)을 기준으로 정렬한다. >> 이거만 하면 [25, 15, ...]
# 조건에 거리가 같다면 더 작은수가 앞으로 배치되어야 하기 때문에 두 번째 요소로 x-n 을 넣어준다.
sorted(array, key=lambda x: (abs(x-n), x-n))
```

### 문제 : 한 번만 등장한 문자

- https://school.programmers.co.kr/learn/courses/30/lessons/120896

```python
#1
def solution(s):
    li = []
    for i in s:
        if s.count(i) == 1:
            li.append(i)

    return ''.join(sorted(li))

#2
def solution(s):
    return ''.join(sorted([i for i in s if s.count(i)==1]))
```

### 문제 : 이진수 더하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120885

```python
#1
def solution(bin1, bin2):
    a = int(bin1, 2) + int(bin2, 2)
    return str(bin(a))[2:]

# int(문자로표현된숫자, 진수) # 진수 = 2,8,16
# bin(10진수), oct(10진수), hex(10진수)
```

### 문제 : 잘라서 배열로 저장하기

- https://school.programmers.co.kr/learn/courses/30/lessons/120913

```python
#1
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
# 슬라이싱은 배열(혹은 문자열) 길이를 넘어가도 에러가 발생하지 않는다!

#2 정규표현식
import re
def solution(my_str, n):
    p = re.compile(f'.{{1,{n}}}')
    return p.findall(my_str)
## 정규표현식에서 {, }를 넣고싶으면 두 번씩 입력해야 한다 {{, }}
```

### 진료순서 정하기 - 12월 26일

- https://school.programmers.co.kr/learn/courses/30/lessons/120835

```python
#1
def solution(emergency):
    answer = []
    em_order = sorted(emergency, reverse=True) # 응급도 높은순서
    return [em_order.index(i)+1 for i in emergency]

#2
def solution(emergency):
    answer = []
    em_order = sorted(emergency, reverse=True) # 응급도 높은순서
    return list(map(lambda x: em_order.index(x)+1, emergency))
```

### 문제 : 공 던지기

- https://school.programmers.co.kr/learn/courses/30/lessons/120843

```python
#1
def solution(numbers, k):
    answer = numbers[2*(k-1)%len(numbers)]
    return answer
# 0,1,2,3 중 나와야 되므로 %길이 연산으로 해줌
# 공차는 사람 첫 번째는 인덱스0 두번째는 인덱스 2 세 번째는 인덱스 4인데 다시 0으로 돌아감
# 왜 점화식... ㅠ

#2 배열 자체를 늘려서 계산
def solution(numbers, k):
    numbers = numbers * k ## 배열을 넉넉하게 k배 늘림
    return numbers[(k-1) * 2]
```

### 문제 : 숨어있는 숫자의 덧셈(2)

- https://school.programmers.co.kr/learn/courses/30/lessons/120864

```python
#1
import re
def solution(my_string):
    p = re.compile(r'([0-9]+)') ## r'\d+'
    li = [int(i) for i in p.findall(my_string)]
    return sum(li)

## 한줄로
# sum(map(int,[i for i in re.findall(r'[0-9]+', my_string)]))

# 1.findall
# 2.sub로 알파벳을 +로 바꾼 후 eval('1+1++++1') 가능하기때문에 ok
# 3.모든 문자 기준으로 split을 해서 sum

##
s = "aAb1B2cC34oOp"
for i in s:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        s = s.replace(i, '-')

s.split('-')

##
import re

s = "aAb1B2cC34oOp"
re.split('[a-zA-Z]', s)

## eval()은 안의 text를 python으로 실행시켜버리기 때문에 위험하다.
## 악성코드를 실행시켜서 서버 정보를 자기 메일로 보낸다거나 하는 등....
import re
def solution(my_string):
    my_string= re.sub(r'[a-zA-Z]+', r'+',my_string)
    return eval(my_string) ## 뒤에 + 가 있어서 안됨...
```

### 문제 : 소인수분해

- https://school.programmers.co.kr/learn/courses/30/lessons/120852

```python
# 1
def solution(n):
    origin = n
    s = set()
    for i in range(2, origin+1):
        while n%i == 0:
            s.add(i)
            n = n/i

        if n == 1:
            break
    answer = sorted(list(s))
    return answer

#2
def solution(n):
    d = 2
    s = set()
    while d <= n:
        if n % d == 0:
            s.add(d)
            n = n / d
        else:
            d = d + 1
    return sorted(list(s))
```

<br>
<br>
<br>
<br>
<br>
<br>

### 문제 : 옹알이

- https://school.programmers.co.kr/learn/courses/30/lessons/120956

```python
#1 permutations
from itertools import permutations

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    two = [''.join(i) for i in permutations(words,2)]
    three = [''.join(i) for i in permutations(words,3)]
    four = [''.join(i) for i in permutations(words,4)]

    berb = words + two + three + four
    for i in babbling:
        if i in berb:
            answer += 1

    return answer

#위에거 깔끔하게 줄이면
from itertools import permutations

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    li = [] + words
    for i in range(2, len(words)+1):
        li += [''.join(k) for k in permutations(words, i)]

    for i in babbling:
        if i in li:
            answer += 1

    return answer

#2 정규표현식
import re

def solution(babbling):
    answer = 0
    li = []
    for i in babbling:
        li.append(re.sub(r'aya|ye|woo|ma', r'', i))

    return li.count('')

#
import re

def solution(babbling):
    answer = 0
    li = []
    p = re.compile(r'aya|ye|woo|ma')
    for i in babbling:
        li.append(p.sub(r'', i))

    return li.count('')

## 강사님풀이?
import re

def solution(babbling):
    count = 0
    p = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        print('------------')
        print(i)
        for pattern in p:
            i = re.sub(pattern, ' ', i)
            print(i)
        if i.replace(' ', '') == '':
            count += 1
    return count

solution(["aya", "yee", "u", "maa", "wyeoo"])
```
