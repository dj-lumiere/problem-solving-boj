# [Bronze III] Missing Numbers - 17588 

[문제 링크](https://www.acmicpc.net/problem/17588) 

### 성능 요약

메모리: 127496 KB, 시간: 228 ms

### 분류

구현

### 제출 일자

2024년 12월 29일 11:41:18

### 문제 설명

<p style="user-select: auto !important;">You enjoy your new job as a teacher of young children. It’s fun to see them learning to count, recognize letters, draw, and interact with the world.</p>

<p style="user-select: auto !important;">One common problem you’ve noticed is that children often forget numbers when counting. For example, early on they might count “one, two, three, five, six.” You have to remind them about that “four” that they didn’t say. And as they get more proficient and clever, they may use the “quick” way of counting: “one, two, skip a few, ninety-nine, one hundred!”</p>

<p style="user-select: auto !important;">Please write a program that can help you (and your students) identify the missing numbers when they are counting.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of input contains a single integer <em style="user-select: auto !important;">n</em>, where 1 ≤ <em style="user-select: auto !important;">n</em> ≤ 100. Each of the next <em style="user-select: auto !important;">n</em> lines contains one number that the child recited. Each recited number is an integer between 1 and 200 (inclusive). They are listed in increasing order, and there are no duplicates.</p>

### 출력 

 <p style="user-select: auto !important;">If the child recited all the numbers between 1 and the last number they recited, then print <code style="user-select: auto !important;">good job</code>.</p>

<p style="user-select: auto !important;">If the child missed any numbers between 1 and the last number they recited, then print those missing numbers in increasing numeric order, one per line.</p>

