# [Silver III] Cow Line - 6119 

[문제 링크](https://www.acmicpc.net/problem/6119) 

### 성능 요약

메모리: 148380 KB, 시간: 276 ms

### 분류

자료 구조, 덱

### 제출 일자

2024년 12월 12일 14:50:35

### 문제 설명

<p style="user-select: auto !important;">Farmer John's N cows (conveniently numbered 1..N) are forming a line. The line begins with no cows and then, as time progresses, one by one, the cows join the line on the left or right side. Every once in a while, some number of cows on the left or right side of the line all leave the line to go graze in their favorite pasture.</p>

<p style="user-select: auto !important;">FJ has trouble keeping track of all the cows in the line. Please help him.</p>

<p style="user-select: auto !important;">The cows enter the line in numerical order 1..N, and once a cow leaves the line she never re-enters it. Your program will be given S (1 <= S <= 100,000) input specifications; each appears on a single line and is one of two types:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">A cow enters the line (a parameter indicates whether on the left or right).</li>
	<li style="user-select: auto !important;">K cows leave the line from the left or right side (supplied parameters define both the number of cows and which side).</li>
</ul>

<p style="user-select: auto !important;">Input lines never request an operation that can not be performed.</p>

<p style="user-select: auto !important;">After all the input lines have been processed, your program should print the cows in the line in order from left to right. The final line is guaranteed to be non-empty at the end of the input specifications.</p>

### 입력 

 <ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Line 1: A single integer: S</li>
	<li style="user-select: auto !important;">Lines 2..S+1: Line i+1 contains specification i in one of four formats:
	<ul style="user-select: auto !important;">
		<li style="user-select: auto !important;">A L -- a cow arrives on the Left of the line</li>
		<li style="user-select: auto !important;">A R -- a cow arrives on the Right of the line</li>
		<li style="user-select: auto !important;">D L K -- K cows depart the Left side of the line</li>
		<li style="user-select: auto !important;">D R K -- K cows depart the Right side of the line</li>
	</ul>
	</li>
</ul>

<p style="user-select: auto !important;"> </p>

### 출력 

 <ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Lines 1..??: Print the numbers of the cows in the line in order from left to right, one number per line.</li>
</ul>

<p style="user-select: auto !important;"> </p>

