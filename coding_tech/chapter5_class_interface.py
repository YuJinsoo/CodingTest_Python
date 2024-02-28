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


# 37-1

# 튜플을 길게 확장하는 패턴은 딕셔너리를 중첩하는 것과 유사
grades =[]
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight

# collection 모듈의 namedtuple 활용
# 작은 불변 데이터 클래스를 쉽게 정의할 수 있습니다.
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))

# 위치기반, 키워드 기반 다 가능합니다.
# 