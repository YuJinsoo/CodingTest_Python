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
    - 튜플을 사용해보자
        - 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사하여 비추

``` python
# 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사
grades =[]
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
```

> `namedtuple`의 한계
- 

### 기억해야 할 Point

> - 딕셔너리, 긴 튜플, 다른 내장 타입이 복잡하게 내표된 데이터를 값으로 사용하는 딕셔너리를 만들지 말자. <br> 
> - 완전한 클래스가 제공하는 유연성이 필요하지 않고 가벼운 불변 데이터 컨테이너가 필요하다면 `namedtuple`을 사용하라 <br>
> - 내부 상태르 ㄹ표현하는 딕셔너리가 복잡해지면 이 데이터를 관리하는 코드를 여러 클래스로 나눠서 재작성해라 <br>

<br>




## BetterWay38. 간단한 인터페이스의 경우 클래스 대신 함수를 받아라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay39. 객체를 제너릭하게 구성하려면 @classmethod를 통한 다형성을 활용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>


## BetterWay40. supser로 부모 클래스를 초기화하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

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

