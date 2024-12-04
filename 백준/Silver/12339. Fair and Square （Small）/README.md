# [Silver V] Fair and Square (Small) - 12339 

[문제 링크](https://www.acmicpc.net/problem/12339) 

### 성능 요약

메모리: 110272 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 수학, 런타임 전의 전처리, 문자열

### 제출 일자

2024년 12월 4일 22:47:18

### 문제 설명

<p style="user-select: auto !important;">Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A <em style="user-select: auto !important;">palindrome</em> is just an integer that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10, we don't consider leading zeroes when determining whether a number is a palindrome).</p>

<p style="user-select: auto !important;">He recently became interested in squares as well, and formed the definition of a <em style="user-select: auto !important;">fair and square</em> number - it is a number that is a palindrome <strong style="user-select: auto !important;">and</strong> the <em style="user-select: auto !important;">square of a palindrome</em> at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are <strong style="user-select: auto !important;">not</strong> fair and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.</p>

<p style="user-select: auto !important;">Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.</p>

<p style="user-select: auto !important;">Solving this problem</p>

<p style="user-select: auto !important;">Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>. <strong style="user-select: auto !important;">T</strong> lines follow. Each line contains two integers, <strong style="user-select: auto !important;">A</strong> and <strong style="user-select: auto !important;">B</strong> - the endpoints of the interval Little John is looking at.</p>

<p style="user-select: auto !important;">Limits</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 100.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">A</strong> ≤ <strong style="user-select: auto !important;">B</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to <strong style="user-select: auto !important;">A</strong> and smaller than or equal to <strong style="user-select: auto !important;">B</strong>.</p>

