# [Bronze I] Alien Communicating Machines - 4144 

[문제 링크](https://www.acmicpc.net/problem/4144) 

### 성능 요약

메모리: 129004 KB, 시간: 240 ms

### 분류

구현, 수학

### 제출 일자

2024년 12월 25일 18:26:49

### 문제 설명

<p style="user-select: auto !important;">Aliens on the planet Hex have sixteen fingers. As a result, they have developed a system of writing numbers with sixteen digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, in ascending order). Like the decimal system that we use, a number is written as a sequence of digits, and the value of a number is determined by the following rules:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">The value of a single-digit number is just the value of that digit.</li>
	<li style="user-select: auto !important;">The value of number <em style="user-select: auto !important;">a</em> consisting of a number <em style="user-select: auto !important;">b</em> followed by a digit <em style="user-select: auto !important;">d</em> is the value of <em style="user-select: auto !important;">b</em> multiplied by a fixed base, plus the value of <em style="user-select: auto !important;">d</em>. In our decimal system, the base is ten, whereas in the system used by the Hex aliens, the base is sixteen.</li>
</ul>

<p style="user-select: auto !important;">Still other planets have other aliens with different numbers of fingers. These aliens use the same rules for writing numbers, but each uses a different base.</p>

<p style="user-select: auto !important;">You have the important job of promoting universal peace by improving communication among all of these aliens. Specifically, you are to write a program that translates numbers written by one alien into numbers that can be understood by a different alien.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of input contains a single integer, the number of test cases to follow. Each test case is a single line containing three numbers <em style="user-select: auto !important;">x</em>, <em style="user-select: auto !important;">y</em>, and <em style="user-select: auto !important;">z</em>. Both <em style="user-select: auto !important;">x</em> and <em style="user-select: auto !important;">y</em> are written in decimal, and are the bases used by the two aliens. Each is at least two and at most thirty-six. The number <em style="user-select: auto !important;">z</em> is written in base <em style="user-select: auto !important;">x</em>, using the letters A through Z as the digits with value 10 through 35. The number <em style="user-select: auto !important;">z</em> will be no greater than four billion.</p>

### 출력 

 <p style="user-select: auto !important;">For each line of input, output a line containing a single number, equal in value to <em style="user-select: auto !important;">z</em>, but written in base <em style="user-select: auto !important;">y</em>.</p>

