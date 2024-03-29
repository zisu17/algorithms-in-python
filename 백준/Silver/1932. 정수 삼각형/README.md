# [Silver I] 정수 삼각형 - 1932 

[문제 링크](https://www.acmicpc.net/problem/1932) 

### 성능 요약

메모리: 39612 KB, 시간: 160 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<pre>        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5</pre>

<p>위 그림은 크기가 5인 정수 삼각형의 한 모습이다.</p>

<p>맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.</p>

<p>삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.</p>

### 입력 

 <p>첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.</p>

### 출력 

 <p>첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.</p>


### 해설

DP(Dinamic Programming)

메모리를 사용해서 중복 연산을 줄이고 수행속도를 개선한다.

메모리를 사용한다는 것은 DP 삼각형과 같이 또다른 배열, 정수 삼각형을 만든다는 것을 의미함

한 번 연산한 결과를 배열에 담아서 다시는 중복된 연산을 하지 않도록 만들어야함

<img width="834" alt="image" src="https://github.com/zisu17/algorithms-in-python/assets/108858121/01641395-7941-4f2d-9880-c0f26239d0c7">



