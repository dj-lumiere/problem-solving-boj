# [Platinum IV] RealPhobia - 5804 

[문제 링크](https://www.acmicpc.net/problem/5804) 

### 성능 요약

메모리: 128784 KB, 시간: 308 ms

### 분류

유클리드 호제법, 수학, 정수론

### 제출 일자

2024년 4월 18일 12:43:49

### 문제 설명

<p>Bert is a programmer with a real fear of floating point arithmetic. Bert has quite successfully used rational numbers to write his programs but he does not like it when the denominator grows large.</p>

<p>Your task is to help Bert by writing a program that decreases the denominator of a rational number, whilst introducing the smallest error possible. For a rational number A/B, where B > 2 and 0 < A < B, your program needs to identify a rational number C/D such that:</p>

<ol>
	<li>0 < C < D < B, and</li>
	<li>the error |A/B - C/D| is the minimum over all possible values of C and D, and</li>
	<li>D is the smallest such positive integer.</li>
</ol>

### 입력 

 <p>The input starts with an integer K (1 < K < 1000) that represents the number of cases on a line by itself. Each of the following K lines describes one of the cases and consists of a fraction formatted as two integers, A and B, separated by “/” such that:</p>

<ol>
	<li>B is a 32 bit integer strictly greater than 2, and</li>
	<li>0 < A < B</li>
</ol>

### 출력 

 <p>For each case, the output consists of a fraction on a line by itself. The fraction should be formatted as two integers separated by “/”.</p>

