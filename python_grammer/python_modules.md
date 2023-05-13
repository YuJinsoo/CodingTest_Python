# re 모듈 (정규표현식)

- python은 정규 표현식을 지원하기 위해 re(regular expression)모듈을 제공한다
- re 모듈은 Python을 설치할 때 자동으로 설치된다

> 기본 사용법<br>

```python
import re
pattern = re.compile('do*g')
## 같은 규칙으로 여러번 사용할땐 이 방법을 사용
```

```pyton
import re
m = re.match('[a-z]+', 'python') #패턴규칙, #검사할문자열
```

- re모듈의 compile 을 사용하여 정규표현식을 컴파일하고 반환된 객체(pattern)를 이용하여 그 이후 작업을 수행한다.
- 패턴이란 정규식을 컴파일한 결과를 의미한다

## 공식문서

- python 3.11.3 에서의 정규표현식 HOWTO
- https://docs.python.org/ko/3/howto/regex.html

## 정규표현식(Regular Expressions)

- 복잡한 문자열을 처리할 때 사용하는 기법
- 파이썬만의 고유 문법이 아니라 모든 곳에서 사용

## 정규표현식의 필요성

- 문자열 처리 방식으로 했을 때 처리가 어려운 경우에도 간편하고 직관적으로 코드를 작성할 수 있다
- 찾으려는 문자여 ㄹ또는 바꿔야 할 문자열의 규칙이 복잡할수록 정규표현식의 효용성이 더욱 커진다.
- 예제<br>

## 메타문자

- 정규표현식의 기초
- 정규 표현식에서는 메타문를 사용하면 의미를 갖게 된다

> 메타문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

```python
. ^ $ * ? { } [ ] \ | ( )
```

### 문자 클래스 [ ]

- `[ ] 사이의 문자들과 매치`라는 의미
  <br> 예) [abc] 라면 "apple", "broken", "drown" 중 drwon은 a, b, c 중 어느것도 포함하지 않음으로 매치되지 않음(apple과 broken은 매치!)

> `[` 과 `]` 사이에는 어떤 문자도 들어갈 수 있다

- []안의 두 문자 사이에 하이픈(`-`)을 사용하면 두 문자 사이의 범위를 의미한다
  <br> [abc] 와 [a-c] 는 동일. [012345] 는 [0-5] 와 동일

  - [a-zA-z] : 알파벳 모두
  - [0-9] : 숫자

- 문자클래스 안에 어떤 문자나 메타문자도 사용할 수 있지만, `^` 메타문자는 반대(not) 의미가 있으므로 주의해야 한다
  - [^0-9] : 숫자가 아닌 것에 매치

> 자주 사용하는 문자 클래스<br> > <br>- `\d` - 숫자와 매치, [0-9]와 동일한 표현식이다.
> <br>- `\D` - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
> <br>- `\s` - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
> <br>- `\S` - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
> <br>- `\w` - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
> <br>- `\W` - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

### Dot .

- 정규 표현식의 Dot(.)메타문자는 줄바꿈 문자(`\n`)을 제외한 모든 문자와 매치됨을 의미한다
- 옵션을 주어 줄바꿈 문자와도 매치되게 할 수 있다. `re.DOTALL`

- 아래 정규식의 의미를 알아보자

```python
a.b
```

    - "a + 모든문자 + b" : a와 b 사이에 어떤 문자가 들어가도 모두 매치
    - "abb" - 매치 , "a8b" - 매치 , "abc" - 매치X (a와 b 사이에 어떤 문자 하나라도 있어야 함)

- 다음 정규표현식의 의미를 알아보자

```python
a[.]
```

    - 문자클래스(`[ ]`)안에 사용될 경우 문자 . 그대로를 의미하므로 주의한다
    - "abb" -  매치 X, "a.b" - 매치

### 반복 \*

- `*` 바로앞에있는 문자가 0개부터 무한대로 반복될 수 있다
  > `*` 메타 문자의 반복 개수가 무한대라고 표현했는데, 메모리 제한으로 2억 개 정도만 가능하다고 한다.

```python
bo*g
```

    - "dg" - "o"가 0번 반복되어 매치
    - "dog" - "o"가 1번 반복되어 매치
    - "doooog" - "o"가 4번 반복되어 매치

### 반복 +

- `+`는 바로 앞의 문자가 최소 1번 이상 반복될 때 사용한다

```python
bo+g
```

    - "dg" - "o"가 0번 반복되어 매치X
    - "dog" - "o"가 1번 반복되어 매치
    - "doooog" - "o"가 4번 반복되어 매치

### 반복 {m,n},?

- 반복 횟수를 제한하고 싶을 때 사용하는 정규 표현식 메타문자
- `{m, n}`를 사용하면 반복 횟수를 m부터 n 가지 매치할 수 있다
- m 이나 n을 입력하지 않으면 0으로 간주한다
  > `{1, }`는 `+`와 동일하고 `{0, }`은 `*`과 동일하다

1. {m}

```python
do{2}g
```

    - "d + o(반드시 2번 반복)+ g"
    - "doog" - "o"가 2번 반복되어 매치
    - "doooog" - "o"가 4번 반복되어 매치 X

2. {m, n}

```python
do{2, 4}g
```

    - "doog" - "o"가 2번 반복되어 매치
    - "dooooog" - "o"가 5번 반복되어 매치
    - "doooooog" - "o"가 6번 반복되어 매치 X

3. ?

   - 반복은 아니지만 비슷한 개념으로 `?`가 의미하는 것은 `{0,1}` 이다
   - 즉 바로앞의 문자가 있어도 되고 없어도 되는 것을 의미한다

   ```python
   ab?c
   ```

   - "abc" - "b"가 1번 사용되어 매치
   - "ac" - "b"가 0번 사용되어 매치

## 정규식을 이용한 문자열 검색

- 컴파일된 파일 객체를 사용해 문자열 검색을 수행할 때 다음 4가지 메서드를 제공한다
  1. match() - 문자열의 처음부터 정규식과 매치되는지 조사한다.
  2. serach() - 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
  3. findall() - 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
  4. finditer() - 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

### match()

- 처음부터 정규식과 매치되는지 조사한다.
- 패턴과 매치되면 re.Match객체를 리턴하고 매치되지 않는다면 None를 리턴한다

```python
import re
p = re.compile('[a-z]+') ## 비어있지 않은 모든 문자열에 매치

m = p.match("python")
print(m)        # <re.Match object; span=(0, 6), match='python'>

m = p.match("python 3.0") # .match는 문자열의 처음부터 확인하기 때문에 일치함.
print(m)


m = p.match("3 python") # 처음 나오는 문자 3은 a-z에 포함되지 않기 때문에 매치되지 않음.
print(m)                # 매치되지 않으면 None을 리턴해준다

```

- 이런 반환값을 이용해서 정규 표현식 프로그램은 다음과 같은 흐름으로 작성한다

```python
p = re.compile(정규표현식)          # 패턴 생성
m = p.match('string goes here')    # 결과값
if m:
    print('Match found: ', m.group())   # match되는 패턴이 어떤 문자열인지 리턴해줌 re.Match의 match 를 리턴해주는듯?
else:
    print('No match')
```

### serach()

- 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색
- 그래서 match와 search 메서드는 문자열의 처음부터 검색할지 여부에 따라 다르게 사용해야 함
- 일치되면 re.Match 객체를 리턴하고, 일치하지 않으면 None을 리턴한다

```python
import re
p = re.compile('[a-z]+') ## 비어있지 않은 모든 문자열에 매치

s = p.search("python")
print(s)        # <re.Match object; span=(0, 6), match='python'>

s = p.search("python 3.0")
print(s)        # <re.Match object; span=(0, 6), match='python'>

s = p.search("3 python") # 문자열 내용 중 일치되는 문자가 있으므로 매치됨
print(s)        # <re.Match object; span=(2, 8), match='python'>

s = p.search("333.3.333.3.3")
print(s)    # None

```

### findall()

- 패턴과 매치되는 모든 값을 찾아 리스트로 반환한다.

```python
import re
p = re.compile('[a-z]+') ## 비어있지 않은 모든 알팞 문자열에 매치

result = p.findall("life is too short, use python.")
print(type(result))     # <class 'list'>
print(result)           # ['life', 'is', 'too', 'short', 'use', 'python']
# , 과 . 음 a-z에 포함되지 않으므로 제외됨
```

### finditer()

- findall과 동일하지만 리턴 값으로 list가 아니라 iterator object를 리턴한다.

```python
import re
p = re.compile('[a-z]+') ## 비어있지 않은 모든 알팞 문자열에 매치

result = p.finditer("life is too short, use python.")
print(type(result))     # <class 'callable_iterator'>
print(result)           # <callable_iterator object at 0x7ffaaa8af1c0>

for i in result :
    print(i, i.group(), sep=' match at: ')

# <re.Match object; span=(0, 4), match='life'> match at: life
# <re.Match object; span=(5, 7), match='is'> match at: is
# <re.Match object; span=(8, 11), match='too'> match at: too
# <re.Match object; span=(12, 17), match='short'> match at: short
# <re.Match object; span=(19, 22), match='use'> match at: use
# <re.Match object; span=(23, 29), match='python'> match at: python

# iterable object라서 한 번 조회하면 다시 생성해줘야함
result = p.finditer("life is too short, use python.")
print(next(result))            # <re.Match object; span=(0, 4), match='life'>
print(next(result).group())    # is
```

### re.Match object의 메서드

- re.Match object는 match()와 search() 메서드의 매치된 결과로 반환된 오브젝트
- re.Match object의 메서드를 사용하면 매치 정보를 얻을 수 있다.

  1. group() - 매치된 문자열을 리턴한다.
  2. start() - 매치된 문자열의 시작 위치를 리턴한다.
  3. end() - 매치된 문자열의 끝 위치를 리턴한다.
  4. span() - 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.

```python

import re
p = re.compile('[a-z]+')

m = p.match('python')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# <re.Match object; span=(0, 6), match='python'>
# python
# 0
# 6
# (0, 6)

s = p.search('2222 python')
print(s)
print(s.group())
print(s.start())
print(s.end())
print(s.span())

# <re.Match object; span=(5, 11), match='python'>
# python
# 5
# 11
# (5, 11)

```

## 컴파일 옵션

- 정규표현식을 컴파일 할 때 옵션을 사용할 수 있다

| 옵션       | 약어 | 설명                                                                          |
| ---------- | ---- | ----------------------------------------------------------------------------- |
| DOTALL     | S    | `.`이 줄바꿈 문자를 포함한 모든 문자와 매치할 수 있도록 함                    |
| IGNORECASE | I    | 대소문자에 관계없이 매치할 수 있도록 한다                                     |
| MULTILINE  | M    | 여러줄과 매치할수 있도록 함 ( 메타문자 `^`, `$`와 연관)                       |
| VERBOSE    | X    | verbose모드 사용(정규식을 보기 편하게 만들 수 있고, 주석을 사용할 수 있게 됨) |

- 옵션을 사용할 때에는 `re.DOTALL` 처럼 전체 옵션을 써도 되고 `re.S`처럼 약어를 써도 된다

### 옵션: DOTALL, S

- `.`메타문자는 줄바꿈 문자(`\n`)를 제외한 모든 문자와 매치되는 규칙이 있다
- `\n`문자를 포하하여 매치하고 싶다면 팯턴 생성 시 `re.DOTALL` 혹은 `re.S`옵션을 사용해 정규식을 컴파일한다

```python
import re
p = re.compile('a.b')

m = p.match('a\nb')
print(m)    # None

p = re.compile('a.b', re.DOTALL) ## 옵션 적용하여 컴파일
m = p.match('a\nb')
print(m)    # <re.Match object; span=(0, 3), match='a\nb'>
```

### 옵션: IGNORECASE, I

- `re.IGNORECASE` 또는 `re.I`옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션
- 아래 예제의 `[a-z]+`옵션은 소문자만 의미하지만 옵션을 주면 대소문자 구별 없이 매치된다

```python
import re
p = re.compile('[a-z]+', re.I)

m = p.match('python')
print(m)    # <re.Match object; span=(0, 6), match='python'>

m = p.match('Python')
print(m)    # <re.Match object; span=(0, 6), match='Python'>

m = p.match('PYTHON')
print(m)    # <re.Match object; span=(0, 6), match='PYTHON'>
```

### 옵션: MULTILINE, M

- 메타문자 `^`, `$`과 관련있는 옵션
- 메타문자 `^`는 문자열의 처음을 `$`는 마지막을 의미함

```python
import re
p = re.compile("^python\s\w+")
# python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # ['python one']
# 메타문자 ^ 에의해 python이라는 문자열을 사용한 첫 번째 줄만 매치된 것
# 각 line의 처음으로 찾고 싶을 때에 사용하는 옵션이 re.MULTILINE, re.M 이다

p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data)) # ['python one', 'python two', 'python three']
# 각 줄에서 "python 단어"로 시작하는 모든 문자 찾음!
```

### 옵션: VERBOSE, X

- 이해하기 어려운 정규식을 주석 또는 줄 단위로 구분할 수 있는 방법
- 예제의 charref1보다 charref2가 가독성이 더 좋다
- 해당 옵션을 주면 문자열에 사용된 whitespace는 컴파일할 때 제거된다.(단 [ ] 안에 사용한 whitespace는 제외)
- 줄 단위로 #기호를 사용하여 주석문을 작성할 수 있다.

- 예제

```python
import re
charref1 = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref2 = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

```

## 백슬래시 문제

- 정규 표현식을 파이썬에서 사용할 때 혼란을 주는 요소가 한 가지 있는데, 바로 백슬래시(`\`)이다.

- 백슬래시 문자를 정규식으로 표현하려면 `\\`두번을 입력해야 함
- 그런데 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 `\\`이 `\`로 변경된다.
- 백슬래시 두 번을 정규식 엔진에 전달하려면
  1.  `\\\\`로 입력해서 컴파일 혹은,
  2.  Raw String이라는 것을 알려주는 r 을 따옴표 앞에 입력해서 컴파일

```python
import re
p = re.compile('\\section') # \ 한번으로 바뀌어서 전달되어버림
# \s 의 경우 [ \t\n\r\f\v] 로 바뀌어버리기 때문에 [ \t\n\r\f\v]ection 이걸 컴파일 한 것과 같게 됨

p = re.compile('\\\\section') # \ 네 번 사용해서 전달
#or
p = re.compile(r'\\section') # Raw String이라고 알려주는 r 문자를 ''("")앞에 삽입
```

# Collections 모듈

## collections.defaultdict

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

---

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
