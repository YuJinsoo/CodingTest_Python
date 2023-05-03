# python 함수 관련 정리

## 데코레이터 (decorator)

- 함수는 아니지만...

---

## 람다함수 (lambda)

- 람다는 식 형대로 되어있어 람다 표현식(lambda expression)이라고 부릅니다. <br> 함수 이름이 없어 익명 함수라고도 부릅니다.
- 간단하게 작성할 수 있어 다른 함수의 인자로 넣어 줄 때 주로 사용합니다.
- 람다식으로 표현한 object는 함수(function) 객체입니다.
- 대표적으로 map, filter 등의 함수의 function 인자로 자주 사용합니다.

> 기본 표현식 <br> `lambda` 인자1, 인자2, ... : 표현식(expression)

```python
# lambda로 생성한 object는 function 타입
lambda x: x+10
# <function <lambda> at 0x0000023EDDAEFAF0>

#식 자체로 함수를 사용할 수 있습니다.
(lambda x: x+10)(3)  #13

# 람다 함수 객체를 사용해봅시다
func = lambda x : x + 10
print(func(4)) #14

func2 = lambda x , y : x +y
func2(1,2) #3

func3 = lambda x, y, z : 100*x + 10*y + z
func3(1,2,3) # 123
```

---

## 클로저 (Closuer)

- 클로저(Closure)는 자신이 생성(선언)된 외부 환경을 기억(Capture)하는 함수 객체이다
- 대표적으로 Python, Javascript, Go lang 에서 지원한다
- 클로저를 지원하려면 언어 차원에서 함수를 일급 객체(First-class object)로 취급해야 한다

### Python 에서 클로저

- 파이썬에서는 함수도 객체(Object)이다
- 클로저에 저장되는 외부 변수는 함수 객체 내의 `__closure__`라는 특별한 변수에 저장된다
- 함수 객체에서 `__closure__` 를 통해 저장된 값을 확인할 수 있다
- `__closure__`의 타입은 `cell` 타입으로 인덱싱과 `cell_contents()` 메서드로 값을 확인할 수 있다

```python
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure_x10 = outer_func(10)
print(closure_x10(30))                  #40
dir(closure_x10)                        # attribute __closure__ 있음을 확인
print(closure_x10.__closure__)          # cell 속성. cell 객체에 int 값 1개 가지고있음
print(closure_x10.__closure__[0])       # 셀 객체에 접근 1개있으니까 index 0
print(type(closure_x10.__closure__[0])) # class cell
dir(closure_x10.__closure__[0])         # cell_contests라는 메서드가 있음
closure_x10.__closure__[0].cell_contents # 10
```

### 실무에서 클로저는 어떻게 활용될까?

- 일반적으로 클로저 패턴보다는 **데코레이터 패턴**으로 사용
- Python은 클로저 패턴이 활발하게 사용되는 언어는 아님
- 정보은닉의 이유로 사용

---

## 순수함수

- 순수함수는 함수는 외부 환경을 변화시키지 않는 함수를 의미한다
- 순수함수는 주변 환경을 변화시키지 않기 때문에, 순수함수로 함수형 프로그래밍을 할 경우 오류를 줄이고 안정성을 높인다
- 단순 더하는 함수로 예제를 보자

  ```python
  # 순수함수
  def add_pure(a, b):
      return a + b
  # 함수 외부 환경에 영향이 전혀 없는 함수 구조. 순수함수이다

  # 비 순수함수
  c = 100
  def add1(a,b):
      return a + b + c
  # c 값이 변경됨에 따라 에러가 발생할 수도 있고, 리턴이 달라짐. 순수함수가 아님

  c = 100
  def add2(a,b):
      c = b
      return a + b
  # 함수 외부의 값을 변경하므로 순수함수가 아니다.
  ```
