# [Silver III] izbori - 3161 

[문제 링크](https://www.acmicpc.net/problem/3161) 

### 성능 요약

메모리: 111428 KB, 시간: 140 ms

### 분류

구현

### 제출 일자

2024년 11월 3일 20:28:26

### 문제 설명

<p>Presidential elections are underway in a small country. There are a total of M citizens choosing between N candidates labeled 1 to N. </p>

<p>Each voter fills his ballot by listing all the candidates in order of preference – they put their favorite candidate in the first place, the second one in the second place, …, the least favored candidate in the last place. </p>

<p>We say that candidate A defeated candidate B if the number of voters that put candidate A in front of candidate B is greater than the number of voters that put candidate B in front of candidate A. For a candidate A we define his score as the total number of candidates he defeated. We say that a candidate is a winner of the elections if his score is greater than or equal to the score of every other candidate. </p>

<p>Write a program that, given the votes of the citizens, finds the winner (or winners) of the elections. </p>

### 입력 

 <p>The first line of input contains two integers M and N, 1 ≤ M,N ≤ 50, M is odd. </p>

<p>Each of the next M lines contains sequence of N numbers, the contents of each citizen's ballot. </p>

### 출력 

 <p>If there is only one winner, output his label on the first and only line. </p>

<p>If there are more winners, output their labels in arbitrary order, each label in its own line. </p>

