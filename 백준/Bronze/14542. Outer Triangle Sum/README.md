# [Bronze II] Outer Triangle Sum - 14542 

[문제 링크](https://www.acmicpc.net/problem/14542) 

### 성능 요약

메모리: 128140 KB, 시간: 224 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 12월 21일 15:26:21

### 문제 설명

<p style="user-select: auto !important;">You are to find the sum of the outer number of an isosceles right triangle.</p>

<p style="user-select: auto !important;">For example, for n = 5 the isosceles right triangle grid are filled with non-negative integers that are less than 100:</p>

<pre style="user-select: auto !important;"><strong style="user-select: auto !important;">5   </strong>
<strong style="user-select: auto !important;">1</strong>   <strong style="user-select: auto !important;">8</strong> 
<strong style="user-select: auto !important;">9</strong>   6  <strong style="user-select: auto !important;">1</strong> 
<strong style="user-select: auto !important;">2</strong>   7  2  <strong style="user-select: auto !important;">6</strong> 
<strong style="user-select: auto !important;">3   5  7  8  9</strong></pre>

<p style="user-select: auto !important;">The sums of the outer integers are calculated as below:</p>

<p style="user-select: auto !important;">sum = 5 + 1 + 9 + 2 + 3 + 5 + 7 + 8 + 9 + 6 + 1 + 8 = 64</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of a few test cases. For each test case, the first line of input is a positive integer <strong style="user-select: auto !important;">n (n <= 10) </strong>that determines the dimension of the triangle. Each of the next <strong style="user-select: auto !important;">n </strong>lines contains 1 to <strong style="user-select: auto !important;">n </strong>integers respectively that will fill the isosceles right triangle. Input is terminated by a case where <strong style="user-select: auto !important;">n </strong>is 0.</p>

### 출력 

 <p style="user-select: auto !important;">Each line of output will start with “Case #:” where # is replaced by the case number. Then you have to output the sum of the outer numbers of the triangle.</p>

