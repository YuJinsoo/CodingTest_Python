# 37

# # dictionary로 성적표 관리
# class SimpleGaradeBook:
#     def __init__(self):
#         self._grades = {}
    
#     def add_student(self, name):
#         self._grades[name] = []
    
#     def report_grade(self, name, score):
#         self._grades[name].append(score)
    
#     def average_grade(self, name):
#         grades = self._grades[name]
#         return sum(grades) / len(grades)

# book = SimpleGaradeBook()
# book.add_student('아이유')
# book.report_grade('아이유', 90)
# book.report_grade('아이유', 95)
# book.report_grade('아이유', 85)
# print(book.average_grade('아이유')) # 90.0


# # 위 확장기능 과목별 성적관리
# ## dict가 2개라 복잡해짐.
# from collections import defaultdict

# class BySubjectGradebook:
#     def __init__(self):
#         self._grades = {}
    
#     def add_student(self, name):
#         self._grades[name] = defaultdict(list) # 내부에 dict하나 더
    
#     def report_grade(self, name, subject, score):
#         by_subject = self._grades[name]
#         grade_list = by_subject[subject]
#         grade_list.append(score)
    
#     def average_grade(self, name):
#         by_subject = self._grades[name]
#         total, count = 0, 0
#         for grades in by_subject.values():
#             total += sum(grades)
#             count += len(grades)
#         return total / count

# book = BySubjectGradebook()
# book.add_student('아인슈타인')
# book.report_grade('아인슈타인', '수학', 75)
# book.report_grade('아인슈타인', '수학', 65)
# book.report_grade('아인슈타인', '체육', 95)
# book.report_grade('아인슈타인', '체육', 90)
# print(book.average_grade('아인슈타인')) # 81.25


# # 시험 별 가중치 까지 관리
# # 평균 계산이 매우 복잡해졌음...
# # 심지어 생성할때도 인자가 너무 많아서 힘듦
# class WeightedGradeBook:
#     def __init__(self):
#         self._grades = {}
    
#     def add_student(self, name):
#         self._grades[name] = defaultdict(list)
    
#     def report_grade(self, name, subject, score, weight):
#         by_subject = self._grades[name]
#         grade_list = by_subject[subject]
#         grade_list.append((score, weight))
    
#     def average_grade(self, name):
#         by_subject = self._grades[name]
#         score_sum, score_count = 0,0
#         for subject, scores in by_subject.items():
#             subject_avg, total_weight = 0,0
            
#             for score, weight in scores:
#                 subject_avg += score* weight
#                 total_weight += weight
            
#             score_sum += subject_avg / total_weight
#             score_count += 1
#         return score_sum/score_count

# book = WeightedGradeBook()
# book.add_student('아인슈타인')
# book.report_grade('아인슈타인', '수학', 75, 0.05)
# book.report_grade('아인슈타인', '수학', 65, 0.15)
# book.report_grade('아인슈타인', '수학', 70, 0.80)
# book.report_grade('아인슈타인', '체육', 100, 0.40)
# book.report_grade('아인슈타인', '체육', 85, 0.60)
# print(book.average_grade('아인슈타인')) # 80.25


# # 37-1

# # 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사
# grades =[]
# grades.append((95, 0.45))
# grades.append((85, 0.55))
# total = sum(score * weight for score, weight in grades)
# total_weight = sum(weight for _, weight in grades)
# average_grade = total / total_weight

# # collection 모듈의 namedtuple 활용
# # 작은 불변 데이터 클래스를 쉽게 정의할 수 있습니다.
# from collections import namedtuple

# Grade = namedtuple('Grade', ('score', 'weight'))

# test = Grade(10, 0.5)
# print(test)         #Grade(score=10, weight=0.5)
# print(test.score)   #10
# print(test.weight)  #0.5
# print(test[0])      #10
# print(test[1])      #0.5

# # 위치기반, 키워드 기반 다 가능합니다.
# # 

# # 클래스로 구현
# from collections import namedtuple, defaultdict
# Grade = namedtuple('Grade', ('score', 'weight'))

# class Subject:
#     def __init__(self):
#         self._grades = []
    
#     def report_grades(self, score, weight):
#         self._grades.append(Grade(score, weight))
    
#     def average_grades(self):
#         total, total_weight = 0, 0
#         for grade in self._grades:
#             total += grade.score * grade.weight
#             total_weight += grade.weight
        
#         return total/total_weight

# class Student:
#     def __init__(self):
#         self._subjects = defaultdict(Subject)
    
#     def get_subject(self, name):
#         return self._subjects[name]
    
#     def average_grade(self):
#         total, count = 0,0
#         for subject in self._subjects.values():
#             total += subject.average_grades()
#             count += 1
#         return total / count

# class Gradebook:
#     def __init__(self):
#         self._students = defaultdict(Student)
    
#     def get_student(self, name):
#         return self._students[name]
    
# book = Gradebook()
# albert = book.get_student('아인슈타인')
# math = albert.get_subject('수학')
# math.report_grades(70, 0.05)
# math.report_grades(65, 0.15)
# math.report_grades(70, 0.80)
# gym = albert.get_subject('체육')
# gym.report_grades(100, 0.40)
# gym.report_grades(100, 0.60)
# print(albert.average_grade()) # 84.625



# 38

# names = ['소크라테스','아르키메데스','플라톤','아리스토텔레스']
# names.sort(key=len)
# print(names) # ['플라톤', '소크라테스', '아르키메데스', '아리스토텔레스']

# # defaultdict 클래스의 동작을 커스터마이즈 하는 예제
# def log_missing():
#     print('키 추가됨')
#     return 0

# from collections import defaultdict

# current = {'초록': 12, '파랑': 3}
# increments = [
#     ('빨강', 5),
#     ('파랑', 17),
#     ('주황', 9)
# ]

# ## 없는 key에 접근할 때 실행할 함수를 1번 인자로 넘겨줄 수 있다.
# result = defaultdict(log_missing, current)
# print('이전: ', dict(result))
# for key, amount in increments:
#     result[key] += amount

# print('이후: ', dict(result)) # 이후:  {'초록': 12, '파랑': 20, '빨강': 5, '주황': 9}



# def log_missing():
#     print('키 추가됨')
#     return 0

# from collections import defaultdict

# def increment_with_report(current, increments):
#     added_count = 0
    
#     def missing():
#         nonlocal added_count # 상태가 있는 클로저
#         added_count += 1
#         return 0

#     result = defaultdict(missing, current)
#     for key, amount in increments:
#         result[key] += amount
    
#     return result, added_count

# current = {'초록': 12, '파랑': 3}
# increments = [
#     ('빨강', 5),
#     ('파랑', 17),
#     ('주황', 9)
# ]

# res, cnt = increment_with_report(current, increments)
# print(res, cnt)
# # {'초록': 12, '파랑': 20, '빨강': 5, '주황': 9}) 2


# class CountMissing:
#     def __init__(self):
#         self.added = 0
    
#     def missing(self):
#         self.added += 1
#         return 0

# from collections import defaultdict

# current = {'초록': 12, '파랑': 3}
# increments = [
#     ('빨강', 5),
#     ('파랑', 17),
#     ('주황', 9)
# ]

# counter = CountMissing()
# result = defaultdict(counter.missing, current)
# for key, amount in increments:
#     result[key] += amount

# assert counter.added == 2 



# class BetterCountMissing:
#     def __init__(self):
#         self.added = 0
    
#     def __call__(self):
#         self.added += 1
#         return 0

# from collections import defaultdict

# current = {'초록': 12, '파랑': 3}
# increments = [
#     ('빨강', 5),
#     ('파랑', 17),
#     ('주황', 9)
# ]

# counter2 = BetterCountMissing()
# result = defaultdict(counter2, current)
# for key, amount in increments:
#     result[key] += amount

# assert counter2.added == 2 


# 39

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
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

