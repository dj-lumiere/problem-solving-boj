# [Platinum V] (재밌고 웃기고 센스있고 깔끔한 제목) - 27452 

[문제 링크](https://www.acmicpc.net/problem/27452) 

### 성능 요약

메모리: 31256 KB, 시간: 144 ms

### 분류

수학, 다이나믹 프로그래밍, 재귀

### 문제 설명

<p>다음과 같은 문자열의 수열 $S$를 정의한다.</p>

<p style="text-align: center;">$S_1 =$ <code>()</code></p>

<p style="text-align: center;">$S_2 =$ <code>()</code></p>

<p style="text-align: center;">$S_n =$ <code>(</code>$S_{n-2} S_{n-1}$<code>)</code> where $n \geq 3$</p>

<p>$S_n$의 $k$ 번째 문자를 구하여라. 단, $S_n$의 맨 처음 문자의 인덱스는 $1$이다.</p>

### 입력 

 <p>첫 번째 줄에 테스트 케이스의 수 $T$가 주어진다. ($1 \leq T \leq 1\,000$)</p>

<p>두 번째 줄부터 $T$ 개의 줄에 정수 $n$, $k$가 주어진다. ($1 \leq n, k \leq 10^{18}$)</p>

### 출력 

 <p>각 테스트 케이스마다 $S_n$의 $k$ 번째 문자를 출력한다. 만약, $k$가 $S_n$의 길이보다 클 경우, <code>0</code>을 대신 출력한다.</p>

