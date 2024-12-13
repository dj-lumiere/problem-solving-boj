# [Silver IV] Selection Sum - 13229 

[문제 링크](https://www.acmicpc.net/problem/13229) 

### 성능 요약

메모리: 139584 KB, 시간: 272 ms

### 분류

누적 합

### 제출 일자

2024년 12월 13일 16:26:47

### 문제 설명

<p style="user-select: auto !important;">Suppose we have an array of integers such as 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. It is easy to compute the sum of all its elements. We only need a loop! For example:</p>

<pre style="user-select: auto !important;">int size = 10;
int total = 0;
for (int i = 0; i < size; i += 1) {
    total = total + v[i];
}
</pre>

<p style="user-select: auto !important;">If we want to count a different range of elements (for example, from position 5 to 7) we only need to change a few parts of the loop. In this problem you'll have to do this operation several times!</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input will contain an integer n (the array size). The next line will contain n integers separated by spaces.</p>

<p style="user-select: auto !important;">After the array, the next line will contain an integer m (the number of tests). The next m lines will contain a test each. A test is a pair of integers start, end. You'll have to compute the sum of the elements from the position start to end.</p>

<p style="user-select: auto !important;">Limits</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">n will be a number from 1 to 100000</li>
	<li style="user-select: auto !important;">start and end will be valid positions of the array</li>
	<li style="user-select: auto !important;">start <= end</li>
	<li style="user-select: auto !important;">the values of the array will be integers from 0 to 9</li>
	<li style="user-select: auto !important;">m will be at most 10000</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test, print the sum of the elements of the array from the position start to the position end inclusive.</p>

<p style="user-select: auto !important;">That is: array[start] + array[start+1] + ... + array[end-1] + array[end].</p>

