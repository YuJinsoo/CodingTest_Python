# 목록
1. [BetterWay37. 내장 타입을 여러 단계로 내포시키기 보다는 클래스를 합성해라](#betterway37-내장-타입을-여러-단계로-내포시키기-보다는-클래스를-합성해라)
2. [BetterWay38. 간단한 인터페이스의 경우 클래스 대신 함수를 받아라](#betterway38-간단한-인터페이스의-경우-클래스-대신-함수를-받아라)
3. [BetterWay39. 객체를 제너릭하게 구성하려면 @classmethod를 통한 다형성을 활용하라](#betterway39-객체를-제너릭하게-구성하려면-classmethod를-통한-다형성을-활용하라)
4. [BetterWay40. supser로 부모 클래스를 초기화하라](#betterway40-supser로-부모-클래스를-초기화하라)
5. [BetterWay41. 기능을 합성할 때는 믹스인 클래스를 사용하라](#betterway41-기능을-합성할-때는-믹스인-클래스를-사용하라)
6. [BetterWay42. 비공개 애트리뷰트보다는 공개 애트리뷰트를 사용하라](#betterway42-비공개-애트리뷰트보다는-공개-애트리뷰트를-사용하라)
7. [BetterWay43. 커스텀 컨테이너 타입은 collections.abc를 상속하라](#betterway43-커스텀-컨테이너-타입은-collectionsabc를-상속하라)

# Chapter5 : 클래스와 인터페이스

- python은 객체지향 언어!
- 상속, 다형성, 캡슐화, 추상화


## BetterWay37. 내장 타입을 여러 단계로 내포시키기 보다는 클래스를 합성해라

- 여러 복합데이터 혹은 `dict`로 관리하는 데이터의 계층이 깊어지면 클래스를 사용하는 것을 권장합니다.
    - 왜냐하면 구조를 기억하기 힘들기 때문입니다.

- 파이썬의 내장 딕셔너리, 튜플, 리스트는 사용하기 편해 내부에 딕셔너리 튜플을 추가해 코드를 사용하기 쉽다.
    - 계층이 두단계 이상이 되면, 코드를 읽기 어려워지고 유지보수도 어려워집니다.
    - 값을 관리하는 것이 복잡하다고 느껴지면 즉시 클래스로 기능을 분리합니다.
        - 잘 캡슐화해주는 인터페이스를 제공할 수 있음.

```python
# 기본 딕셔너리로 모든 데이터를 관리하면서 복잡해지는 예제
# dictionary로 성적표 관리
class SimpleGaradeBook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGaradeBook()
book.add_student('아이유')
book.report_grade('아이유', 90)
book.report_grade('아이유', 95)
book.report_grade('아이유', 85)
print(book.average_grade('아이유')) # 90.0


# 위 확장기능 과목별 성적관리
## dict가 2개라 복잡해짐.
from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list) # 내부에 dict하나 더
    
    def report_grade(self, name, subject, score):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(score)
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('아인슈타인')
book.report_grade('아인슈타인', '수학', 75)
book.report_grade('아인슈타인', '수학', 65)
book.report_grade('아인슈타인', '체육', 95)
book.report_grade('아인슈타인', '체육', 90)
print(book.average_grade('아인슈타인')) # 81.25


# 시험 별 가중치 까지 관리
# 평균 계산이 매우 복잡해졌음...
# 심지어 생성할때도 인자가 너무 많아서 힘듦
class WeightedGradeBook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0,0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0,0
            
            for score, weight in scores:
                subject_avg += score* weight
                total_weight += weight
            
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum/score_count

book = WeightedGradeBook()
book.add_student('아인슈타인')
book.report_grade('아인슈타인', '수학', 75, 0.05)
book.report_grade('아인슈타인', '수학', 65, 0.15)
book.report_grade('아인슈타인', '수학', 70, 0.80)
book.report_grade('아인슈타인', '체육', 100, 0.40)
book.report_grade('아인슈타인', '체육', 85, 0.60)
print(book.average_grade('아인슈타인')) # 80.25
```
<br>

#### 클래스를 활용해 리팩토링하기

- 의존 관계 트리의 맨 밑바닥(가장 깊은 레벨)을 점수로 표현하는 클래스로 변환할 수 있음
    - 단순 데이터를 리팩토링 하기 위해 클래스를 도입하는 것은 비효율적입니다.
    - 점수는 불변이므로 마침 `튜플`을 사용해보자
        - 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사하여 비추
        - 내부 원소의 위치를 사용해 접근해야함. 즉 외부에서 구조를 알고 있어야함.

``` python
# 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사
# 내부 원소의 위치를 사용해 접근해야함. 즉 외부에서 구조를 알고 있어야함.
grades =[]
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
```

- `튜플`사용시 길이가 길어질 것이 예상된다면 `namedtuple`타입을 사용해보자
    - 작은 크기의 불변 데이터 클래스를 쉽게 정의할 수 있음
    - 위치인자, 키워드 인자 모두 사용 가능
    - 요구사항이 바뀌는 경우에 `namedtuple`을 클래스로 바꾸기 쉽다.
        (어트리뷰트처럼 사용할 수 있기 때문에 정의만 클래스로 바꾸면 호환이 됨)

```python
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))

test = Grade(10, 0.5)
print(test)         #Grade(score=10, weight=0.5)
print(test.score)   #10
print(test.weight)  #0.5
print(test[0])      #10
print(test[1])      #0.5
```


> #### `namedtuple`의 한계
> - 디폴트 인자 값을 지정할 수 없다. <br>
> - 속정이 4~5개 이상이면 `dataclasses`내장 모듈을 사용하는 편이 낫다.<br>
> - 여전히 숫자 이터레이션이 가능하기 때문에 외부에 제공하는 API의 겨웅 클래스로 변경이 어려울 수 있다. <br>
> - 모든 부분을 제어할 수 있지 않다면 클래스로 정의하는 편이 더 낫다.<br>

- 클래스로 구현
    - 코드는 길어지지만 읽기 쉬워진다.
    - 사용 코드도 읽기 쉽고 확정성이 좋다.

```python
from collections import namedtuple, defaultdict
Grade = namedtuple('Grade', ('score', 'weight'))

class Subject:
    def __init__(self):
        self._grades = []
    
    def report_grades(self, score, weight):
        self._grades.append(Grade(score, weight))
    
    def average_grades(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        
        return total/total_weight

class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0,0
        for subject in self._subjects.values():
            total += subject.average_grades()
            count += 1
        return total / count

class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
    
    def get_student(self, name):
        return self._students[name]
    
book = Gradebook()
albert = book.get_student('아인슈타인')
math = albert.get_subject('수학')
math.report_grades(70, 0.05)
math.report_grades(65, 0.15)
math.report_grades(70, 0.80)
gym = albert.get_subject('체육')
gym.report_grades(100, 0.40)
gym.report_grades(100, 0.60)
print(albert.average_grade()) # 84.625
```

<br>
### 기억해야 할 Point

> - 딕셔너리, 긴 튜플, 다른 내장 타입이 복잡하게 내표된 데이터를 값으로 사용하는 딕셔너리를 만들지 말자. <br> 
> - 완전한 클래스가 제공하는 유연성이 필요하지 않고 가벼운 불변 데이터 컨테이너가 필요하다면 `namedtuple`을 사용하라 <br>
> - 내부 상태를 표현하는 딕셔너리가 복잡해지면 이 데이터를 관리하는 코드를 여러 클래스로 나눠서 재작성해라 <br>

<br>


## BetterWay38. 간단한 인터페이스의 경우 클래스 대신 함수를 받아라

- 파이썬 내장 API중 상당수는 인자로 함수를 전달해 도작을 바꿀 수 있다.
    - 이런 함수를 훅(hook)이라고 부름
    - `sort`메서드에 `len`함수를 넘겨주는 예제
        ``` python
            ## 이름 길이에 따라 정렬합니다.
            names = ['소크라테스','아르키메데스','플라톤','아리스토텔레스']
            names.sort(key=len)
            print(names) 
            # ['플라톤', '소크라테스', '아르키메데스', '아리스토텔레스']
        ``` 

- `훅`을 추상 클래스를 통해 정의해아 하는 언어도 있음
- python에서는 **인자와 반환 값이 잘 정의되고 상태가 없는 함수**를 훅으로 사용하는 경우가 많음
- python은 함수를 `일급 시민 객체`로 취급하기 때문에 가능
    - 일급 시민 객체
        - 언어 안에서 제약 없이 사용할 수 있는 데이터값
        - 변수 할당, 함수 리턴, 함수 인자, 동등성을 검사할 수 있는 값

- defaultdict 클래스의 동작을 커스터마이즈 하는 예제
    - `log_missing`과 같이 커스텀 함수를 사용할 수 있으면 정해진 동작과 부수효과를 분리할 수 있기 때문에 API를 더 쉽게 만들 수 있다.
```python
# defaultdict 클래스의 동작을 커스터마이즈 하는 예제
def log_missing():
    print('키 추가됨')
    return 0

from collections import defaultdict

current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9)
]

## 없는 key에 접근할 때 실행할 함수를 1번 인자로 넘겨줄 수 있다.
result = defaultdict(log_missing, current)
print('이전: ', dict(result))
for key, amount in increments:
    result[key] += amount

print('이후: ', dict(result)) 
# 이후:  {'초록': 12, '파랑': 20, '빨강': 5, '주황': 9}
```

- defaultdict에 없는 key에 접근한 횟수를 세고 싶은 예제
    - 상태가 있는 클로저를 사용하면 된다. (Better way 21)
    - 내부 함수 `missing`이 상태를 관리함
    - 하지만 상태있는 클로저를 활용한 것은 그렇지 않은 코드보다 이해하기 어렵다.
        - 추적하고 싶은 상태를 저장하는 클래스를 구현하는 방법도 있음.
```python
def log_missing():
    print('키 추가됨')
    return 0

from collections import defaultdict

def increment_with_report(current, increments):
    added_count = 0
    
    def missing():
        nonlocal added_count # 상태가 있는 클로저
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    
    return result, added_count

current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9)
]

res, cnt = increment_with_report(current, increments)
print(res, cnt)
# {'초록': 12, '파랑': 20, '빨강': 5, '주황': 9}) 2
```

- 상태를 저장하는 클래스를 정의하여 구현 (위 예제 다른 접근방법)
    - 하지만 이 방법은 클래스 인스턴스를 어디에 만드는지에 대한 논란이 생길 수 있음.
    - 클래스 매직메서드 `__call__`을 정의해 인스턴스 생성을 생략할 수 있음
```python
# 상태를 저장하는 클래스 (위 예제 다른 접근방법)
class CountMissing:
    def __init__(self):
        self.added = 0
    
    def missing(self):
        self.added += 1
        return 0

from collections import defaultdict

current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9)
]

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount

assert counter.added == 2 
```

- 상태를 저장하는 클래스에 __call__정의하여 구현
    - 위 인스턴스를 생성하는 방법보다 훨씬 깔끔하다.
    - 
```python
class BetterCountMissing:
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return 0

from collections import defaultdict

current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9)
]

counter2 = BetterCountMissing()
result = defaultdict(counter2, current)
for key, amount in increments:
    result[key] += amount

assert counter2.added == 2 
```

### 기억해야 할 Point
> - python의 여러 컴포넌트 사이에 간단한 인터페이스가 필요할 때는 클래스를 정의하고 인스턴스를 생성하는 대신 간단히 함수를 사용할 수 있다.<br>
> - python 함수나 메서드는 일급 시민이다. 따라서 함수나 함수 참조를 식에 사용할 수 있다.<br>
> - __call__매직 메서드를 사용하면 클래스의 인스턴스인 객체를 일반 파이썬 함수처럼 호출할 수 있다.<br>
> - 상태를 유지하기 위한 함수가 필요한 경우에는 상태가 있는 클로저를 정의하는 대신 __call__메서드가 있는 클래스를 정의할 지 고려해보자<br>

<br>

## BetterWay39. 객체를 제너릭하게 구성하려면 @classmethod를 통한 다형성을 활용하라
- 객체 뿐 아니라 클래스도 다형성을 지원함
- 다형성을 사용하면..
    - 계층을 이루는 여러 클래스가 자신에게 맞는 유일한 메서드 버전을 구현할 수 있다.
    - 같은 인터페이스를 만족하거나 같은 추상 기반 클래스를 공유하는 많은 클래스가 서로 다른 기능을 제공할 수 있다는 뜻입니다. (BetterWay43)

- 맵리듀스(Map Reduce) 구현 예제
    - 이 예제는 잘 동작할 것 처럼 보이지만, 객체를 생성해 활용해야만 이 모든 클래스가 쓸모있음
    - 각 객체를 만들고 맵리듀스를 조화롭게 실행하는 책임은 누가 져야 할까??
```python
# 입력 데이터를 표현할 수 있는 공통 클래스가 필요해 구현
class InputData:
    def read(self):
        raise NotImplementedError

# 하위클래스
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()
        

# 위 입력 데이터를 소비하는 공통 방법을 제공하는 맵리듀스 작업자로 쓸 수 있는 추상 인터페이스를 정의
class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError

# worker의 하위 클래스
# 새줄 문자의 개수를 세는 맵리듀스 기능 클래스
class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
        
    def reduce(self, other):
        self.result += other.result
```

- 이런 클래스를 인스턴스화 하고 실행을 책임지는 방법
1. 도우미 함수를 활요해 객체를 직접 만들고 연결
    - 이 방법의 문제가 뭘까?
    - 함수가 전혀 제너릭 하지 않다.
        - 다른 `InputData`나 `Worker` 하위 클래스를 사용하고 싶다면 그에 맞는 `generate_inputs`, `create_workers`, `mapreduce를` 작성해야 함
        - 객체를 구성할 수 있는 제너릭한 방법이 필요함.
        - 다른 언어에서는 다형성을 사용해 해결할 수 있는데, `InputData`의 모든 하위클래스는 맵리듀스를 처리하는 도우미 메서드들이 제너릭하게 사용할 수 있는 특별한 생성자(팩토리 메서드 같은)를 제공합니다.
        - But, python에서는 생성자가 `__init__` 뿐...
        - 이 문제를 해결하는 가장 좋은 방법은 `클래스 메서드`다형성을 이용하는 것!

```python
import os

# 디렉터리 목록을 얻어 안에 들어있는 파일마다 pathInputData 인스턴스를 만듦
def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

# generate_inputs를 통해 만든 PathInputData 인스턴스들을 사용하는 LineCounterWorker인스턴스를 생성
def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

# 이 Worker 인스턴스의 map 단계를 여러 스레드에 공급해서 실행할 수 있다.(better way 53)
# 그후 reduce를 반복적으로 호출해서 견과를 최종 값으로 합칠 수 있다.

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

# 마지막으로 지금까지 만든 모든 조각을 한 함수에 합쳐서 각 단계를 실행
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)
```

2. `클래스 메서드`사용
    - `GenericWorker`의 `create_workers`에서 `generate_inputs`를 호출하는 것이 이 예제에서 보여주고 싶은 다형성입니다.
    - `create_worker`가 `__init__`을 통하지 않고 `cls()`를 호출함으로써 다른 방법으로 객체를 만들 수 있다.

```python
## 클래스메서드 사용

class GenericInputData:
    def read(self):
        raise NotImplementedError
    
    # 객체를 생성하는 설정 정보가 들어 있는 딕셔너리르 파라미터로 받는다.
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    ...
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

# 비슷한 방식으로 GenericWorker에 create_workes를 넣을 수 있따.

class GenericWorker():
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError
    
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        ## 이 부분이 다형성의 예.
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers
```

- 마지막으로는 mapreduce 함수가 create_worker를 호출하게 변경하면 mapreduec를 완전하게 제너릭 함수로 만들 수 있습니다.

```python
def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)
```

- 각 하위 클래스의 인스턴스 객체를 결합하는 코드를 변경하지 않아도, `GenericInput`과 `GenericWorker`의 하위 클래스를 내가 원하는 대로 작성할 수 있다.


### 기억해야 할 Point
> - python 클래스의 생성자는 `__init__`메서드 뿐이다.<br>
> - `@classmethod`를 사용하면 클래스에 다른 생성자를 정의할 수 있다.<br>
> - 클래스를 메서드 다형성을 활용하면 여러 구체적인 하위 클래스의 객체를 만들고 연결하는 제너릭한 방법을 제공할 수 있다.<br>

<br>


## BetterWay40. supser로 부모 클래스를 초기화하라
- 자식 클래스에서 부모 클래스를 초기화하는 오래된 방법은 자식 인스턴스에서 부모 클래스의 `__init__`메서드를 직접 호출하는 것이다.
    - 이 방법은 기본적인 클래스 계층의 경우 잘 동작
    - 다른 경우에는 잘못 동작할 수 있음

```python
## 기본적인 형상에서는 문제 없이 동작한다.
class Base:
    def __init__(self, value):
        self.value = value

class Child(Base):
    def __init__(self):
        Base.__init__(self, 5)
```

- 다중 상속의 경우 위 방법은 문제가 발생할 수 있다. (사실 다중 상속은 피해야 하는 case)
    - 모든 하위 클래스에서 `__init__` 호출의 순서가 정해져 있지 않는 것이 문제

```python
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class Child(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)
        
class TimesTwo:
    def __init__(self):
        self.value *= 2
        
class PlusFive:
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print(foo.value) # 15

## 하지만 상속 순서와 초기화 순서가 다른 경우..
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

afoo = AnotherWay(5)
print(afoo.value) # 15
## 이때도 문제는 발생하지 않는다. __init__메서드 순서가 동일하기 때문.
```

- 다중 상속 중 다이아몬드 상속인 경우
    - 예상했던 결과랑 다른 결과가 나옴(44가 나와야 하지만 14가 나옴)
    - 왜냐하면 ThisWay의 `__init__`에서 PlusNine의 `__init__`이 호출되면서 value가 다시 5로 초기화 된 다음 9를 더하기 때문.
    - 이런 경우 디버깅 하기 매우 어려워짐
```python
## 기본 클래스를 상속하는 두 클래스
class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9

## 기본 클래스의 두 자식 클래스를 상속하는 클래스(다이아몬드 상속)
class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = ThisWay(5)
print(foo.value) ## 14
## 예상한 동작은 5 * 7 + 9 이기 때문에 44 이지만, 14가 출력됨
```

- 위와 같은 문제를 해결하기 위해 `super`라는 매장 함수와 표준 메서드 결정 순서(Method Resolution Order, MRO)가 있다.
    - `super`를 사용하면 다이아몬드 계층의 공통 상위 클래스를 단 한 번만 호출하도록 보장합니다. (Betterway 48)
    - MRO는 상위 클래스를 초기화하는 순서를 정의합니다.
        - 이때 C3 선형화 라는 알고리즘을 사용한다.
    
   

- 다이아몬드 상속 구조이지만 super를 활용한 예제
    - `mro()` 메서드 로 출력한 순서에서 위에서 아래로 호출됨
    - 하지만 스택구조이므로, 역순으로 연산이 진행되어서 리턴됨(5+9 먼저인 이유)
```python
## 기본 클래스를 상속하는 두 클래스
class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

## 기본 클래스의 두 자식 클래스를 상속하는 클래스(다이아몬드 상속)
class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

foo = GoodWay(5)
print(foo.value) ## 98
# 7 * ( 5 + 9 ) 라서 98이 나옴

mro_str = '\n'.join(repr(cls) for cls in GoodWay.mro())
print(mro_str)
# <class '__main__.GoodWay'>
# <class '__main__.TimesSevenCorrect'>
# <class '__main__.PlusNineCorrect'>
# <class '__main__.MyBaseClass'>
# <class 'object'>

```
- `super().__init__` 호출은 다중 상속을 튼튼하게 해주며, 하위 클래스에서 상위 클래스의 `__init__`을 직접 호출하는 것 보다 유지보수를 더 편하게 해준다.
- super()함수에 두 파라미터를 넘길 수 있다.
    1. 접근하고 싶은 MRO 뷰를 제공할 부모 타입
    2. 첫 파라미터로 지정한 타입의 MRO 뷰에 접근할 때 사용할 인스턴스

> super에 파라미터를 넘겨야 하는 유일한 경우는 자식 클래스에서 상위 클래스의 특정 기능에 접근해야 하는 경우 뿐이다. (특정 기능을 감싸거나 재사용해야 하는 경우)

```python
## super에 전달하는 인자
class ExplictTrisect(MyBaseClass):
    def __init__(self, value):
        super(ExplictTrisect, self).__init__(value)
        self.value /= 3
        
## 하지만 object 인스턴스를 초기화 할 때는 두 파라미터를 지정할 필요가 없음
## 지정하지 않으면 컴파일러가 자동으로 올바른 파라미터르 ㄹ넣어준다.

##동일한 결과
class AutoTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3
        

class ImplictTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3

assert ExplictTrisect(9).value == 3
assert AutoTrisect(9).value == 3
assert ImplictTrisect(9).value == 3
```

### 기억해야 할 Point
> - 파이선은 표준 메서드 결정 순서(MRO)를 활용해 상위 클래스 초기화 순서와 다이아몬드 상속 문제를 해결한다.<br>
> - 부모 클래스를 초기화할 때는 super 내장 함수를 아무 인자 없이 호출한다. (파이썬 컴파일러가 자동으로 올바른 파라미터를 전달한다.)<br>

<br>

## BetterWay41. 기능을 합성할 때는 믹스인 클래스를 사용하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay42. 비공개 애트리뷰트보다는 공개 애트리뷰트를 사용하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay43. 커스텀 컨테이너 타입은 collections.abc를 상속하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

