# [Diamond II] FFT Algorithm - 18491 

[문제 링크](https://www.acmicpc.net/problem/18491) 

### 성능 요약

메모리: 123832 KB, 시간: 196 ms

### 분류

중국인의 나머지 정리, 분할 정복을 이용한 거듭제곱, 수학, 정수론, 폴라드 로, 소수 판정, 무작위화

### 제출 일자

2023년 12월 23일 15:08:10

### 문제 설명

<p>When I want to apply FFT algorithm to polynomial of degree less than 2<sup>k</sup> in modular arithmetics, I have to find ω — a primitive 2<sup>k</sup>-th root of unity.</p>

<p>Formally, for two given integers m and k, I should find any integer ω such that:</p>

<ul>
	<li>0 ≤ ω < m,</li>
	<li>ω<sup>2<sup>k</sup></sup> ≡ 1 (mod m),</li>
	<li>ω<sup>p</sup> ≠ 1 (mod m) for all 0 < p < 2<sup>k</sup>.</li>
</ul>

<p>In this task, I ask you to find ω for me, or determine that it does not exist. Since we talk about application of FFT, I’ve set some reasonable <strong>limitations for</strong> k: for smaller k naive polynomial multiplication is fine, and for larger k FFT takes more than 1 second (we are competitive programmers after all).</p>

### 입력 

 <p>The only line of input contains two integers m and k (2 ≤ m ≤ 4 · 10<sup>18</sup>, 15 ≤ k ≤ 23).</p>

### 출력 

 <p>Print any ω satisfying the criteria, or print −1 if there is no such ω.</p>

