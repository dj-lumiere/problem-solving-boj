# [Bronze I] Best Matched Pair - 15529 

[문제 링크](https://www.acmicpc.net/problem/15529) 

### 성능 요약

메모리: 129496 KB, 시간: 276 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 12월 21일 15:22:15

### 문제 설명

<p style="user-select: auto !important;">You are working for a worldwide game company as an engineer in Tokyo. This company holds an annual event for all the staff members of the company every summer. This year’s event will take place in Tokyo. You will participate in the event on the side of the organizing staff. And you have been assigned to plan a recreation game which all the participants will play at the same time.</p>

<p style="user-select: auto !important;">After you had thought out various ideas, you designed the rules of the game as below.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Each player is given a positive integer before the start of the game.</li>
	<li style="user-select: auto !important;">Each player attempts to make a pair with another player in this game, and formed pairs compete with each other by comparing the products of two integers.</li>
	<li style="user-select: auto !important;">Each player can change the partner any number of times before the end of the game, but cannot have two or more partners at the same time.</li>
	<li style="user-select: auto !important;">At the end of the game, the pair with the largest product wins the game.</li>
</ul>

<p style="user-select: auto !important;">In addition, regarding the given integers, the next condition must be satisfied for making a pair.</p>

<p style="user-select: auto !important;">The sequence of digits obtained by considering the product of the two integers of a pair as a string must be increasing and consecutive from left to right. For example, 2, 23, and 56789 meet this condition, but 21, 334, 135 or 89012 do not.</p>

<p style="user-select: auto !important;">Setting the rules as above, you noticed that multiple pairs may be the winners who have the same product depending on the situation. However, you can find out what is the largest product of two integers when a set of integers is given.</p>

<p style="user-select: auto !important;">Your task is, given a set of distinct integers which will be assigned to the players, to compute the largest possible product of two integers, satisfying the rules of the game mentioned above.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of a single test case formatted as follows.</p>

<pre style="user-select: auto !important;">N
a<sub style="user-select: auto !important;">1</sub> a<sub style="user-select: auto !important;">2</sub> ... a<sub style="user-select: auto !important;">N</sub></pre>

<p style="user-select: auto !important;">The first line contains a positive integer N which indicates the number of the players of the game. N is an integer between 1 and 1, 000. The second line has N positive integers that indicate the numbers given to the players. For i = 1, 2, . . . , N − 1, there is a space between a<sub style="user-select: auto !important;">i</sub> and a<sub style="user-select: auto !important;">i+1</sub>. a<sub style="user-select: auto !important;">i</sub> is between 1 and 10, 000 for i = 1, 2, . . . , N, and if i ≠ j, then a<sub style="user-select: auto !important;">i</sub> ≠ a<sub style="user-select: auto !important;">j</sub>.</p>

### 출력 

 <p style="user-select: auto !important;">Print the largest possible product of the two integers satisfying the conditions for making a pair. If any two players cannot make a pair, print −1.</p>

