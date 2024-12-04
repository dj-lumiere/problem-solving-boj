# [Bronze I] Hand Detection - 6995 

[문제 링크](https://www.acmicpc.net/problem/6995) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 12월 4일 22:58:21

### 문제 설명

<p style="user-select: auto !important;">Hobbits like games of chance and skill. As such they play a game very much like our poker, though their decks of cards and rules are a bit different.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">Cards can have one of 21 values (1 to 21 inclusive).</li>
	<li style="user-select: auto !important;">Cards can have one of 5 suits (Elf, Man, Hobbit, Ent, Orc).</li>
</ul>

<p style="user-select: auto !important;">A deck of cards therefore has 105 cards. Each “hand” has 5 cards, just like poker.</p>

<p style="user-select: auto !important;">Your task is to write a program to identify two types of hands: a “spread” and a “rainbow”.</p>

<p style="user-select: auto !important;">The rules for a “spread” are as follows: the suits don’t matter but the values do. The values must be such that the difference between any two card values is not the same as the difference between any other two card values.</p>

<p style="user-select: auto !important;">For example, a hand with containing cards with values 1, 2, 4, 8, 16 is a spread because any pair of values has a unique difference:</p>

<table class="table table-center-40 table table-bordered" style="user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">First Card</th>
			<th style="user-select: auto !important;">Second Card</th>
			<th style="user-select: auto !important;">difference</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">1</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;">3</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">7</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">16</td>
			<td style="user-select: auto !important;">15</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;">2</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">6</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">16</td>
			<td style="user-select: auto !important;">14</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">4</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">4</td>
			<td style="user-select: auto !important;">16</td>
			<td style="user-select: auto !important;">12</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">8</td>
			<td style="user-select: auto !important;">16</td>
			<td style="user-select: auto !important;">8</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">The rule for a “rainbow” is simply that the hand must have exactly one card of each suit.</p>

### 입력 

 <p style="user-select: auto !important;">The first line in the test data file contains the number of test cases (< 100). After that each line will contain a test case, with each card being represented by two integers (thus each test case comprises of 10 integers). The first number is the card’s suit (an int that takes values between 0 and 4, inclusive), and the second represents the card’s suit (an int that takes values between 1 and 21, inclusive).</p>

### 출력 

 <p style="user-select: auto !important;">For each test case, the program needs to indicate whether or not that hand of cards has a spread and whether or not that hand of cards has a rainbow. The exact format is shown below.</p>

