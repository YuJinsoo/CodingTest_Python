# Collections 모듈

## collections의 defaultdict

- dict 클래스의 subclass
- collections 라이브러리에 탑재되어 있는 defaultdict는 딕셔너리(dict)와 거의 똑같은 용법으로 사용할 수 있습니다.
- 다른 점은 없는 키로 접근을 해도 KeyError를 일으키지 않고 초기 값(default value)를 내뱉는다는 데 있습니다.
- 초기값은 따로 설정할 수 있습니다.

- 예제

```python
from collections import defaultdict
default_dict = defaultdict(int) # 초기값을 설정해줌
print(type(default_dict))
print(default_dict)         # defaultdict(<class 'int'>, {})

# 없는 키를 조회하면 원소가 추가됨
default_dict['key1']

# int 클래스의 기본 값인 0이 자동으로 들어감
print(default_dict)        # defaultdict(<class 'int'>, {'key1': 0})

# get함수는 조회만 하고 없는 키를 호출해도 생성되지는 않음
default_dict.get('hi')
print(default_dict)         # defaultdict(<class 'int'>, {'key1': 0})

default_dict['key2']
print(default_dict)         # defaultdict(<class 'int'>, {'key1': 0, 'key2': 0})

```

- 활용방법

```python
# 기본값으로 컨벤션 타입으로 지정할 수 있음
from collections import defaultdict
ddict = defaultdict(list) # 초기값을 설정해줌
print(ddict)    # defaultdict(<class 'list'>, {})

# 원소가 리스트이면 같은 key 값에 여러 value를 넣을 수 있게 된다.
l = [('A',123),('B', 45),('C', 6),('A',78),('B',9)]
for k, v in l:
    ddict[k].append(v)

# 없는 key더라도 에러발생하지 않고 생성해서 값을 넣어준다.

print(ddict)    # defaultdict(<class 'list'>, {'A': [123, 78], 'B': [45, 9], 'C': [6]})
```

- to be continue...

## collections의 Counter

```python
from collections import Counter

print(Counter([1,1,1,3,4,2,4,3,4,4,4,4,1,5,2,6,6,6,2,1,3,2]))
print(Counter('hello world! hey~'))
# Counter({4: 6, 1: 5, 2: 4, 3: 3, 6: 3, 5: 1})
# Counter({'l': 3, 'h': 2, 'e': 2, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1, 'y': 1, '~': 1})
```

### get

- 사용된 요소의 개수를 반환합니다
- 없는요소(key)일 경우 `None`을 리턴합니다

```python
from collections import Counter

array = [1,1,2,3,4,4,2,2,5,6,6,7,8,9,7,8,9,7,7,8,6,2,3,5]

def solution(array, n):
    value = Counter(array).get(n)
    return 0 if value == None else value

print(solution(array,4))  # 2
print(solution(array,10)) # 0
```

## collections의 deque

```python
from collections import deque

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = deque(numbers)
numbers.rotate(3) # 양수면 오른쪽으로 돌림. 음수면 왼졲으로 도림
print(numbers)
dir(numbers)
## deque 자주사용하는 메서드
#  'append',
#  'appendleft',
#  'extend',
#  'extendleft',
#  'maxlen',
#  'pop',
#  'popleft',
#  'reverse',
#  'rotate'
```

### key, values, update, get ...

## collections의 deque

<br>

---

<br>

# itertools 모듈

- itertools 모듈에는 반복 가능한 데이터 스트림을 처리하는 데 유용한 많은 함수와 제너레이터가 포함되어 있습니다.

## itertools.chain()

> 함수 형태 : itertools.chain(\*iterables)

- 첫 번째 이터러러블 객체가 끝날 원소를 반환하고 다음 이터러블로 넘어감
- iterables의 모든 이터러블이 소진될 때까지 진행하는 이터레이터를 만듭니다
- 여러 시퀀스를 단일 시퀀스처럼 처리하는 데 사용됩니다.

- 예제: 한 차원의 iterable만 함(2차원 배열의 경우 list채로 출력)

```python
import itertools

a = itertools.chain([1,2,3], ['AB'], 'hello@world!')

for i in a:
    print(i, end=' ')
# 1 2 3 AB h e l l o @ w o r l d !

print()
aa = itertools.chain([1,2,[10,20,30]],"ABC",(10.2, 22.2))
# 1단계 iterable 까지만 그대로 출력함
for i in aa:
    print(i, end=' ')

# 1 2 [10, 20, 30] A B C 10.2 22.2

```

## itertools의 permutations

- 입력한 자료형으로부터 **순열(Permutation)**을 생성하여 tuple이 요소인 iter를 반환한다.

> from itertools import permutations
> permutations(iterable, r=None)

- 첫번째 인자로 iterable객체가 들어가 각 요소가 뽑기의 요소가 됩니다.
- r는 몇개를 한 묶음으로 뽑을 것인지 결정합니다. r길이의 tuple 요소를 가진 iter를 반환됩니다.
- 지정하지 않으면 iterabler객체의 길이가 r 값인 것처럼 계산됩니다.

```python
from itertools import permutations

a = ['a', 'b', 'c']
nono = list(permutations(a))
one = [''.join(i) for i in permutations(a,1)]
two = [''.join(i) for i in permutations(a,2)]
three = [''.join(i) for i in permutations(a,3)]

print(nono)   # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
print(one)    # ['a', 'b', 'c']
print(two)    # ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
print(three)  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

## itertools의 product

- permutation은 중복을 허용하지 않는 순열이었다면, `product`는 **중복을 허용하는 순열** 입니다.

> from itertools import product
> product(\*iterables, repeat=1)

- iterable객체들을 여러개를 넣어 벡터 곱 연산을 수행할 수 있습니다.
- 반환은 repeat의 수 혹은 입력한 iterable의 개수와 동일한 길이의 tuple 요소를 가진 iter를 반환합니다.

```python
from itertools import product

## 편의상 모든 원소를 str로 했습니다.
# list, string 등 iterable한객체 가능합니다.
a = ['a', 'b', 'c']
b = ['1', '2', '3']
s = 'ABC'

nono = list(product(a))
print(nono) # [('a',), ('b',), ('c',)]

pd = [''.join(i) for i in product(a, repeat=2)]
print(pd)   # ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

pd2 = list(product(a, b))
print(pd2)
# [('a', '1'), ('a', '2'), ('a', '3'), ('b', '1'), ('b', '2'), ('b', '3'), ('c', '1'), ('c', '2'), ('c', '3')]

pd2 = [''.join(i) for i in product(a, b)]  ## 벡터의 곱연산과 같다!
print(pd2) # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']


pd3 = [''.join(i) for i in product(s, repeat =3)]
print(pd3)
# ['AAA', 'AAB', 'AAC', 'ABA', 'ABB', 'ABC', 'ACA', 'ACB', 'ACC',
# 'BAA', 'BAB', 'BAC', 'BBA', 'BBB', 'BBC', 'BCA', 'BCB', 'BCC',
# 'CAA', 'CAB', 'CAC', 'CBA', 'CBB', 'CBC', 'CCA', 'CCB', 'CCC']
```

# functools 모듈

# json 모듈

- JSON(JavaScript object Notation)은 텍스트를 사용하여 데이터를 저장하고 전송할 데이터 공유를 위한 개방형 표준 파일 형식입니다.
- JSON 데이터는 **키/값 쌍**으로 작성됩니다. 키와 값은 중간에 콜론(:)으로 구분되며 왼쪽에는 키, 오른쪽에는 값이 있습니다.
- XMl에 비해 **명확하고 읽기 쉽고**, 데이터 셋을 정의하는 문자 수가 적어 인터넷을 통한 전송 **오버헤드**가 적습니다.

- `{ }` 를 하나의 오브젝트로 인식해서 다룹니다.
- json 모듈은 JSON 파일을 읽고 쓰기 편리하게 지원하는 모듈입니다.

- 인코더(json.JSONEncoder)와 디코더(json.JSONDecoder)

  - NaN, Infinity 및 -Infinity를 해당 float 값으로 이해합니다.
    |JSON|파이썬|
    |------|----|
    |오브젝트(object)|dict|
    |배열(array)|list|
    |문자열(string)|str|
    |숫자(정수)|int|
    |숫자(실수)|float|
    |true|True|
    |flase|False|
    |null|None|

- https://docs.python.org/ko/3/library/json.html

## json.dump()

- 인자로 file object가 있어서 `str`로 변환해 파일에 쓰는 기능까지 포함
- json 파일에 입력할 데이터는 `dictionary` 타입으로 되어있어야 한다.

```python
# list형식, dict형식 모두 입력이 된다.
# 왜냐하면 JSON 데이터와 Python 자료형이 1:1 매칭되고 그걸 josn 모듈에서 처리해주기 떄문

import json

li = [
    {
        "_id": "645f63cdbfa868f6ba47ccd7",
        "age": 40,
        "eyeColor": "brown",
        "name": "Frederick Pate",
        "gender": "male"
    },
    {
        "_id": "645f63cd9e3df96110aeec47",
        "age": 31,
        "eyeColor": "green",
        "name": "Janis Guthrie",
        "gender": "female"
    },
    {
        "_id": "645f63cd033fb24f4534d349",
        "age": 32,
        "eyeColor": "brown",
        "name": "Marla West",
        "gender": "female"
    }
]

d = {
        "_id": "645f63cd033fb24f4534d349",
        "age": 32,
        "eyeColor": "brown",
        "name": "Marla West",
        "gender": "female"
    }


with open('dump_li.json', 'w', encoding='utf-8') as f:
    # indent key argument에 int 혹은 문자로 들여쓰기 문자를 어떤 것으로 넣을지 설정할 수 있음
    json.dump(li, f, indent='\t') # JSON 문자열로 변환과 동시에 파일에 입력이 됨


with open('dump_d.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

```

### JSON에서 한글 출력하기

- key argument : `ensure_ascii` 활용
- 키 아규먼트 값을 `False`로 주면 아스키코드 값으로 문자를 표현하는 것을 보장하지 않으므로 문자 그대로 표현됨
- 키 아규먼트 값을 `True`로 주면 모든 문자를 아스키코드 값표현하기 때문에 아스키 코드가 아닌 문자는 이스케이프 문자로 표현된다(디폴트)

```python
import json
d = {'one': '하나', 'two': '둘', 'three': '셋'}

with open('ensure_false.json', 'w', encoding='utf-8') as f:
    json.dump(d,f,indent='\t', ensure_ascii=False)

## ensure_false.json
# {
# 	"one": "하나",
# 	"two": "둘",
# 	"three": "셋"
# }

with open('ensure_true.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent='\t', ensure_ascii=True)

## ensure_true.json
# {
# 	"one": "\ud558\ub098",
# 	"two": "\ub458",
# 	"three": "\uc14b"
# }

```

## json.load()

- JSON 파일을 열어 Python의 객체로 변환하는 함수

```python
# 위에 있는 dump_d.json 파일을 오픈하는 예제
import json

with open('dump_d.json') as f:
    json_obj = json.load(f)

print(json_obj)
#  {'_id': '645f63cd033fb24f4534d349', 'age': 32, 'eyeColor': 'brown', 'name': 'Marla West', 'gender': 'female'}
```

## json.dumps()

> json.dumps(py_object, name)

- Python 객체를 JSON 문자열로 변환하는 함수
- 반환 값은 `str` 타입 문자열을 반환해줌
- 파일에 쓰는 기능은 없음

- json.dumps()는 JSON 문자열로 변환만 해주기 때문에 f.write로 직접 파일에 써 줘야 한다.

```python
import json
d = {
        "_id": "645f63cd033fb24f4534d349",
        "age": 32,
        "eyeColor": "brown",
        "name": "Marla West",
        "gender": "female"
    }

with open('dumps.json', 'w', encoding='utf-8') as f:
    json_str = json.dumps(li, indent='\t')
    print(json_str)
    f.write(json_str) # dumps는 JSON문자열로 변환만 하기 때문에 파일에 직접 써줘야 한다.

```

## json.loads()

- JSON 문자열을 Python 객체로 변환하는 함수

```python
import json
d = {
        "age": 32,
        "Region": {
          "Contry" : "Korea,
          "City" : "Seoul,
          "Code" : 18490
        },
        "name": "Marla West",
    }


json_str = json.dumps(d, intdent = 4)
print(json_str)
print(type(json_str)) # <class 'str'>

py_obj = json.loads(json_str)
print(type(py_obj)) # <class 'dict'> # python 객체 dict로 변환됨

## 출력
# {
#     "age": 32,
#     "Region": {
#         "Country": "Korea",
#         "City": "Seoul",
#         "Code": 18490
#     },
#     "name": "Marla West"
# }

```

# random 모듈

- 임의로 난수를 생성하는 모듈입니다.
- 실제로 완벽한 난수는 아니지만 난수에 매우 가깝게 숫자를 생성해줍니다.
- 난수를 생성하는 알고리즘은 여러 가지 방식이 있습니다

# pprint 모듈

# os 모듈

- 파이썬 내장 모듈로 별도의 설치 없이 `import os`로 임포트 할 수 있습니다.
- 파이썬을 이용해 파일을 복사하거나 디렉터리를 생성하고 특정 디렉터리 내의 파일 목록을 구하고자 할 때 `os 모듈`을 사용하면 됩니다.

## os.getcwd()

- 현재 경로를 str 문자열로 반환

```python
import os

s = os.getcwd()

print(type(s))  # <class 'str'>
print(s)        # C:\Users\ABO\Desktop\Study_Python
```

## os.listdir()

- 현재 경로에 있는 모든 파일 및 폴더를 str 문자열 요소를 가진 list로 반환
- 파일은 확장자가 있고 폴더는 확장자가 없는 것으로 구분할 수 있음

```python
import os

l = os.listdir()

print(type(l)) # <class 'list'>
print(l)  # ['.git', 'CodingTest', 'python_grammer', 'README.md']

```

## os.system()

> os.system(커맨드명령어)

- 커맨드명령어 (string) 를 수행하는 함수

```python
import os

os.system('dir')

#  C 드라이브의 볼륨에는 이름이 없습니다.
#  볼륨 일련 번호: F28A-138E

#  C:\Users\ABO\Desktop\Study_Python 디렉터리

# 2023-05-11  오후 04:40    <DIR>          .
# 2023-05-11  오후 04:40    <DIR>          ..
# 2023-05-09  오후 05:06    <DIR>          CodingTest
# 2023-05-11  오후 04:40    <DIR>          python_grammer
# 2023-05-09  오후 04:42                58 README.md
#                1개 파일                  58 바이트
#                4개 디렉터리  104,515,416,064 바이트 남음
# 0
```

## os.mkdir(), os.makedirs()

- `os.mkdir()`, `os.makedirs()`함수는 입력한 경로의 폴더를 생성해주는 함수입니다.

> os.mkdir(경로)

- 입력한 경로의 폴더만 생성하는 함수.
- 중간에 없는 경로가 입력되면 지정된 경로를 찾을 수 없다는 에러가 나오면서 실패한다.

```python
import os

os.mkdir('test') # test 폴더를 생성
os.mkdir('test2/test3') # 현재 경로에 test2 폴더가 없다면 에러 발생

```

> os.makedirs(경로, exist_ok=True/False)

- 최하위 경로까지 가는 경로에 폴더가 없다면 모든 폴더를 생성해줌

```python
import os

os.makedirs('test2/test3/testtest') # test2, test3 폴더가 없어도 모두 생성
os.makedirs('test2/test3/testtest') # 파일이 이미 있으므로 만들 수 없습니다: 'test2/test3/testtest' 라는 에러 발생
os.makedirs('test2/test3/testtest', exist_ok=True) # 경로상에 파일이 이미 존재하고 있어도 에러를 뱉지 않는 옵션

```

## os.path 모듈

- `os` 모듈에 포함된 모듈로 파일 경로를 생성 및 수정하고 파일 정보를 쉽게 다룰 수 있게 하는 모듈입니다.
- `import os.path`로 임포트 할 수 있습니다.

- os.path.abspath() 함수

  > os.path.abspath(파일및폴더이름)

  - 문자열로 입력한 `파일및폴더이름`를 절대경로 문자열로 반환합니다.

  ```python
  import os.path

  s = os.path.abspath('Test.md')

  print(type(s))  # <class 'str'>
  print(s)        # C:\Users\ABO\Desktop\Study_Python\Test.md
  ```

- os.path.basename() 함수

  > os.path.basename(절대경로)

  - 입력한 절대 경로에서 가장 마지막 폴더 혹은 파일명만 문자열로 반환합니다.
  - 절대경로를 입력할 때 백슬래시 개수에 유의해한다. (백슬래스 2개 혹은 raw-string 문자)

```python
import os.path

s = os.path.basename(r'C:\Users\ABO\Desktop\Study_Python\Test.md')

print(type(s))  # <class 'str'>
print(s)        # Test.md

```

- os.path.dirname() 함수

  > os.path.dirname(경로)

  - path의 파일/디렉토리 경로를 반환한다.

  ```python
  import os.path

  s = os.path.dirname(r'C:\Users\ABO\Desktop\Study_Python\Test.md')

  print(type(s))  # <class 'str'>
  print(s)        # C:\Users\ABO\Desktop\Study_Python

  ```

  - 폴더로 했을 때

  ```python
  import os.path

  s = os.path.dirname(r'C:\Users\ABO\Desktop\Study_Python')

  print(type(s))  # <class 'str'>
  print(s)        # C:\Users\ABO\Desktop

  ```

- os.path.exists() 함수

  > os.path.dirname(경로)

  - 입력한 경로가 존새하면 `True`, 존재하지 않으면 `False`를 리턴한다

```python
import os.path

print(os.path.exists(r'C:\Users\ABO\Desktop\Study_Python\Test.md')) ## 파일명은 입력해도 False
print(os.path.exists(r'C:\Users\ABO\Desktop\Study_Python'))         ## 실제 있는 경로이면 True
```

# glob 모듈

- 파일 검색이 아주 용이한 모듈로 `*` 이나 `?` 문자로 파일명을 쉽게 필터링할 수 있다.
- 정규표현식과 같이 사용이 안됩니다.

# sys 모듈

- 인터프리터? 디버깅하는거 있던데...

# pytz 모듈

- 세계 시간 기준으로 관리해주는 패키지

# 엑셀모듈 : xlsxwriter

- openpyxl 등등이 있었음

# 크롤링 모듈 : beautifulsoup

> 임포트 형식 : `from bs4 import BeautifulSoup`

- `BeautifulSoup`은 HTML과 XML 문서를 파싱하는 라이브러리입니다.
- 웹 크롤링을 할 때, HTML 문서에서 원하는 데이터를 추출하는 데 자주 사용됩니다.
- str 타입의 html 데이터를 html 구조를 가진 데이터로 가공하는 것도 가능합니다.

- `reausts` 모듈로 가져온 응답을 파싱해서 원하는 정보를 보여줄 수 있음
- 일반적으로 아래와 같이 원하는 url의 html파일을 요청받은 후 BeautifulSoup객체를 생성해 사용함

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```

- 교육 크롤링 페이지의 거래량 총합을 구하는 코드

```python

# advanced 과제 :
# 제주코딩베이스캠프 연구원에 2019.09.24일 부터 2019.10.23일까지 거래된 거래총량을 구해주세요.

# https://paullab.co.kr/stock.html

### 제출답안### >> 주석제거후 제출했음
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# print(type(soup)) # <class 'bs4.BeautifulSoup'>

# 테이블 이름을 미리 저장
table_title = soup.select_one('.main>#제주코딩베이스캠프연구원').text

# 연구원 이 들어간 객체만 골라서 가져오기
data = soup.select('.main')

lab_table = list(filter(lambda x: '연구원' in x.text, data))
# print(lab_table)
# print(len(lab_table))

data_list = lab_table[0].select('table>tbody>tr>td')
# print(type(data_list[0]))   #<class 'bs4.element.Tag'>
# print(dir(data_list[0]))

# len(data_list) # 140
total_trading_volume = 0

# 7번째 데이터마다 거래량
for i in range(6,len(data_list),7):
    # print(data_list[i].text)
    total_trading_volume += int(data_list[i].text.replace(',', ''))

print(f'{table_title}의 기간동안 거래총량은 {total_trading_volume:,} 회 입니다.')

```

- 더 간단하게 풀이한 방법. 상태클래스를 사용하면 더 쉽게 활용할 수 있다.

```python
# advanced 과제 : 더 쉽게 풀기. td에 :nth-child(7) 으로 검색하면 7번째 데이터를 바로 읽어온다.
# 제주코딩베이스캠프 연구원에 2019.09.24일 부터 2019.10.23일까지 거래된 거래총량을 구해주세요.

# https://paullab.co.kr/stock.html

### 제출답안### >> 주석제거후 제출했음
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 테이블 이름을 미리 저장
table_title = soup.select_one('.main>#제주코딩베이스캠프연구원').text

# 연구원 이 들어간 객체만 골라서 가져오기
data = soup.select('.main')
lab_table = list(filter(lambda x: '연구원' in x.text, data))

data_list = lab_table[0].select('table > tbody > tr > td:nth-child(7)') # > span은 있어도 되고 없어도 되네..
data_list2 = [i.text.replace(',','') for i in data_list]

total_trading_volume = sum(map(int, data_list2))

print(f'{table_title}의 기간동안 거래총량은 {total_trading_volume:,} 회 입니다.')
```

# gc 모듈 : Garbage Collector 사용하기

- https://wikidocs.net/13969

# psutil 모듈 : CPU및 메모리 성능 확인 모듈
