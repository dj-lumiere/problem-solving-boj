# [Silver III] Classical A+B Problem - 28202 

[문제 링크](https://www.acmicpc.net/problem/28202) 

### 성능 요약

메모리: 2180 KB, 시간: 40 ms

### 분류

임의 정밀도 / 큰 수 연산, 브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 수학

### 문제 설명

<p>An integer is called a <em>repdigit</em> if it is positive and its decimal representation consists of repeated instances of the same digit. For example, $1$, $666$, $4444$, and $999999$ are repdigits, while $0$, $44244$, $50216$, and $787788$ are not.</p>

<p>You are given a positive integer $n$. It is known that $n$ can be represented as $n = a + b$, where $a$ and $b$ are repdigits. Find any such representation.</p>

### 입력 

 <p>Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). The description of the test cases follows.</p>

<p>The only line of each test case contains a single integer $n$ without leading zeros ($2 \le n < 10^{4000}$). It is guaranteed that $n$ can be represented as $n = a + b$, where $a$ and $b$ are repdigits.</p>

<p>It is guaranteed that the total number of digits in $n$ over all test cases does not exceed $10^5$.</p>

### 출력 

 <p>For each test case, print two integers $a$ and $b$ such that $n = a + b$ and both $a$ and $b$ are repdigits.</p>

<p>If there are multiple solutions, print any of them.</p>

