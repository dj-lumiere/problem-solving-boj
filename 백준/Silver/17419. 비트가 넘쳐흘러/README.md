# [Silver IV] 비트가 넘쳐흘러 - 17419 

[문제 링크](https://www.acmicpc.net/problem/17419) 

### 성능 요약

메모리: 112980 KB, 시간: 96 ms

### 분류

비트마스킹, 수학, 문자열

### 제출 일자

2024년 12월 3일 13:25:50

### 문제 설명

<p style="text-align: center; user-select: auto !important;"><em style="user-select: auto !important;">🎶 DJ욱제는 <strong style="user-select: auto !important;">비트</strong>에 몸을 맡기는 중이다. 🎶</em></p>

<p style="user-select: auto !important;"><em style="user-select: auto !important;">DJ욱제</em>는 비트에 심취한 나머지, <em style="user-select: auto !important;">비트를 비틀어 제껴버리는</em> 문제를 내 버렸다!</p>

<p style="user-select: auto !important;"><em style="user-select: auto !important;">N</em>자리 이진수 <em style="user-select: auto !important;">K</em>가 주어진다. <em style="user-select: auto !important;">K</em>가 0이 아닐 때까지 아래의 연산을 적용했을 때, 연산이 일어나는 횟수를 구하시오.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><em style="user-select: auto !important;">K</em> = <em style="user-select: auto !important;">K</em>-(<em style="user-select: auto !important;">K</em>&((~<em style="user-select: auto !important;">K</em>)+1))</li>
</ul>

<p style="user-select: auto !important;">아래는 위의 연산에 사용된 연산자에 대한 설명이다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">'+'는 산술 더하기 연산이다. (5 + 2 = 7)</li>
	<li style="user-select: auto !important;">'-'는 산술 빼기 연산이다. (5 - 2 = 3)</li>
	<li style="user-select: auto !important;">'&'는 비트 AND 연산이다. (1101 & 0111 = 0101)</li>
	<li style="user-select: auto !important;">'~'는 비트 NOT 연산이다. 켜진 비트를 끄고, 꺼진 비트를 켜는 연산이다. (~1101 = 0010)</li>
</ul>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 <em style="user-select: auto !important;">N</em>이 주어진다.</p>

<p style="user-select: auto !important;">둘째 줄에 <em style="user-select: auto !important;">N</em>자리 이진수 <em style="user-select: auto !important;">K</em>가 주어진다. <em style="user-select: auto !important;">K</em>는 0으로 시작하지 않는다. 즉, leading zero는 없다.</p>

### 출력 

 <p style="user-select: auto !important;">연산이 일어나는 횟수를 출력한다.</p>

