# [Bronze IV] Tournament Selection - 14038 

[문제 링크](https://www.acmicpc.net/problem/14038) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

구현

### 제출 일자

2024년 12월 26일 12:02:13

### 문제 설명

<p style="user-select: auto !important;">Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">if a player wins 5 or 6 games, they are placed in Group 1;</li>
	<li style="user-select: auto !important;">if a player wins 3 or 4 games, they are placed in Group 2;</li>
	<li style="user-select: auto !important;">if a player wins 1 or 2 games, they are placed in Group 3;</li>
	<li style="user-select: auto !important;">if a player does not win any games, they are eliminated from the tournament.</li>
</ul>

<p style="user-select: auto !important;">Write a program to determine which group a player is placed in</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of six lines, each with one of two possible letters: W (to indicate a win) or L (to indicate a loss).</p>

### 출력 

 <p style="user-select: auto !important;">The output will be either 1, 2, 3 (to indicate which Group the player should be placed in) or -1 (to indicate the player has been eliminated).</p>

