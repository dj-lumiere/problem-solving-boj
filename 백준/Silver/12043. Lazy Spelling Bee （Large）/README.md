# [Silver IV] Lazy Spelling Bee (Large) - 12043 

[문제 링크](https://www.acmicpc.net/problem/12043) 

### 성능 요약

메모리: 128140 KB, 시간: 252 ms

### 분류

조합론, 수학, 문자열

### 제출 일자

2024년 12월 27일 13:58:51

### 문제 설명

<p style="user-select: auto !important;">In the Lazy Spelling Bee, a contestant is given a target word W to spell. The contestant's answer word A is acceptable if it is the same length as the target word, and the i-th letter of A is either the i-th, (i-1)th, or (i+1)th letter of W, for all i in the range of the length of A. (The first letter of A must match either the first or second letter of W, since the 0th letter of W doesn't exist. Similarly, the last letter of A must match either the last or next-to-last letter of W.) Note that the target word itself is always an acceptable answer word.</p>

<p style="user-select: auto !important;">You are preparing a Lazy Spelling Bee, and you have been asked to determine, for each target word, how many distinct acceptable answer words there are. Since this number may be very large, please output it modulo 1000000007 (10<sup style="user-select: auto !important;">9</sup> + 7).</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>. <strong style="user-select: auto !important;">T</strong> test cases follow; each consists of one line with a string consisting only of lowercase English letters (<code style="user-select: auto !important;">a</code> through <code style="user-select: auto !important;">z</code>).</p>

<h3 style="user-select: auto !important;">Limits</h3>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 100.</li>
	<li style="user-select: auto !important;">1 ≤ length of each string ≤ 1000.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of distinct acceptable answer words, modulo 10<sup style="user-select: auto !important;">9</sup> + 7.</p>

