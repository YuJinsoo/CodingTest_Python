# 목록
1. [BetterWay52. 자식프로세스를 관리하기 위해 subprocess를 사용하라](#betterway52-자식프로세스를-관리하기-위해-subprocess를-사용하라)
2. [BetterWay53. 블로킹 I/O의 경우 스레드를 사용하고 병렬성을 피하라](#betterway53-블로킹-io의-경우-스레드를-사용하고-병렬성을-피하라)
3. [BetterWay54. 스레드에서 데이터 경합을 피가히 위해 Lock을 사용하라](#betterway54-스레드에서-데이터-경합을-피가히-위해-lock을-사용하라)
4. [BetterWay55. Queue를 사용해 스레드 사이의 작업을 조율하라](#betterway55-queue를-사용해-스레드-사이의-작업을-조율하라)
5. [BetterWay56. 언제 동시성이 필요한지 인식하는 방법을 알아두라](#betterway56-언제-동시성이-필요한지-인식하는-방법을-알아두라)
6. [BetterWay57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라](#betterway57-요구에-따라-팬아웃을-진행하려면-새로운-스레드를-생성하지-말라)
7. [BetterWay58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라](#betterway58-동시성과-queue를-사용하기-위해-코드를-어떻게-리팩터링해야-하는지-이해하라)
8. [BetterWay59. 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용해라](#betterway59-동시성을-위해-스레드가-필요한-경우에는-threadpoolexecutor를-사용해라)
9. [BetterWay60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라](#betterway60-io를-할-때는-코루틴을-사용해-동시성을-높여라)
10. [BetterWay61. 스레드를 사용한 I/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라](#betterway61-스레드를-사용한-io를-어떻게-asyncio로-포팅할-수-있는지-알아두라)
11. [BetterWay62. asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라](#betterway62-asyncio로-쉽게-옮겨갈-수-있도록-스레드와-코루틴을-함께-사용하라)
12. [BetterWay63. 응답성을 최대로 높이려면 asyncio 이벤트 루프를 블록하지 말라](#betterway63-응답성을-최대로-높이려면-asyncio-이벤트-루프를-블록하지-말라)
13. [BetterWay64. 진정한 병렬성을 살리려면 concurrent.futures를 사용하라](#betterway64-진정한-병렬성을-살리려면-concurrentfutures를-사용하라)



# Chapter7 : 동시성과 병렬성

- 동시성 (Concurenncy)
    - 여러 작업을 코어 1개에서 번갈아가며 처리하여 동시에 처리하는 것처럼 보이는 것
    - CPU 코어 1 개에서 시간을 쪼개어 번갈아 가며 수행
    - CPU 바운드 작업 일 때, 속도 차이가 별로 없다.

- 병렬성 (Parallelism)
    - 여러 작업을 동시에 처리하는 것
    - 여러 코어에서 각각 다른 명령을 처리
    - CPU 바운드 작업 일 때, 속도가 현저히 빨라진다. 

- Python 동시성 프로그램
    - 스레드
    - 코루틴
    - 하위 프로세스(subprocess)
    - C 확장(C extension)
    - 시스템 콜(system call)

- 동시성 python 코드가 실제 병렬적으로 실행되게 만드는 것은 매우 어렵다.


## BetterWay52. 자식프로세스를 관리하기 위해 subprocess를 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay53. 블로킹 I/O의 경우 스레드를 사용하고 병렬성을 피하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay54. 스레드에서 데이터 경합을 피가히 위해 Lock을 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay55. Queue를 사용해 스레드 사이의 작업을 조율하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay56. 언제 동시성이 필요한지 인식하는 방법을 알아두라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay59. 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용해라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay61. 스레드를 사용한 I/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay62. asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay63. 응답성을 최대로 높이려면 asyncio 이벤트 루프를 블록하지 말라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay64. 진정한 병렬성을 살리려면 concurrent.futures를 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>
