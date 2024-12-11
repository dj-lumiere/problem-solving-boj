# [Bronze I] Frodo Sequence - 5346 

[문제 링크](https://www.acmicpc.net/problem/5346) 

### 성능 요약

메모리: 127552 KB, 시간: 228 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 12월 11일 09:48:39

### 문제 설명

<p style="user-select: auto !important;">The Fibonacci sequence is a famous integer sequence defined by Leonardo of Pisa in 1202. The sequence is defined as follows:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">1</sub> = 1</li>
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">2</sub> = 1</li>
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">3</sub> = 2</li>
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">4</sub> = 3</li>
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">5</sub> = 5</li>
	<li style="user-select: auto !important;">…</li>
	<li style="user-select: auto !important;">Fib<sub style="user-select: auto !important;">n</sub> = Fib<sub style="user-select: auto !important;">n-1</sub> + Fib<sub style="user-select: auto !important;">n-2</sub> for all n>2</li>
</ul>

<p style="user-select: auto !important;">What you may not know is that Frodo of Bag End also defined an integer sequence called the Frodo sequence. Frodo’s sequence is defined as follows:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">1</sub> = 1</li>
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">2</sub> = 1</li>
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">3</sub> = 2</li>
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">4</sub> = 2</li>
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">5</sub> = 3</li>
	<li style="user-select: auto !important;">…</li>
	<li style="user-select: auto !important;">Fro<sub style="user-select: auto !important;">n</sub> = Fro<sub style="user-select: auto !important;">n-1</sub> + Fro<sub style="user-select: auto !important;">n-2</sub> - Fro<sub style="user-select: auto !important;">n-3</sub> for all n>3</li>
</ul>

<p style="user-select: auto !important;">You need to write a program that given n finds Fro<sub style="user-select: auto !important;">n</sub>.</p>

### 입력 

 <p style="user-select: auto !important;">he input will be a sequence of integers, one per line. The end of input will be signaled by the integer 0. All integers, other than the last (zero), are positive and less than 2<sup style="user-select: auto !important;">31</sup>.</p>

### 출력 

 <p style="user-select: auto !important;">For each positive integer, n, print Fro<sub style="user-select: auto !important;">n</sub>.</p>

