# [Silver IV] Polynomial Remains - 1716 

[문제 링크](https://www.acmicpc.net/problem/1716) 

### 성능 요약

메모리: 133924 KB, 시간: 240 ms

### 분류

수학

### 제출 일자

2024년 12월 11일 10:07:02

### 문제 설명

<p style="user-select: auto !important;">Given the polynomial</p>

<p style="text-align: center; user-select: auto !important;">a(x) = a<sub style="user-select: auto !important;">n</sub> x<sup style="user-select: auto !important;">n</sup> + ... + a<sub style="user-select: auto !important;">1</sub> x + a<sub style="user-select: auto !important;">0</sub>,</p>

<p style="user-select: auto !important;">compute the remainder r(x) when a(x) is divided by x<sup style="user-select: auto !important;">k</sup>+1.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of a number of cases. The first line of each case specifies the two integers n and k (0 ≤ n, k ≤ 10000). The next n+1 integers give the coefficients of a(x), starting from a<sub style="user-select: auto !important;">0</sub> and ending with a<sub style="user-select: auto !important;">n</sub>. The input is terminated if n = k = -1.</p>

### 출력 

 <p style="user-select: auto !important;">For each case, output the coefficients of the remainder on one line, starting from the constant coefficient r<sub style="user-select: auto !important;">0</sub>. If the remainder is 0, print only the constant coefficient. Otherwise, print only the first d+1 coefficients for a remainder of degree d. Separate the coefficients by a single space.</p>

<p style="user-select: auto !important;">You may assume that the coefficients of the remainder can be represented by 32-bit integers.</p>

