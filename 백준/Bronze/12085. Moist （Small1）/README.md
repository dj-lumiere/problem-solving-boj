# [Bronze I] Moist (Small1) - 12085 

[문제 링크](https://www.acmicpc.net/problem/12085) 

### 성능 요약

메모리: 127492 KB, 시간: 212 ms

### 분류

구현, 정렬, 문자열

### 제출 일자

2024년 12월 25일 21:14:38

### 문제 설명

<p style="user-select: auto !important;">Moist has a hobby -- collecting figure skating trading cards. His card collection has been growing, and it is now too large to keep in one disorganized pile. Moist needs to sort the cards in alphabetical order, so that he can find the cards that he wants on short notice whenever it is necessary.</p>

<p style="user-select: auto !important;">The problem is -- Moist can't actually pick up the cards because they keep sliding out his hands, and the sweat causes permanent damage. Some of the cards are rather expensive, mind you. To facilitate the sorting, Moist has convinced Dr. Horrible to build him a sorting robot. However, in his rather horrible style, Dr. Horrible has decided to make the sorting robot charge Moist a fee of \$1 whenever it has to move a trading card during the sorting process.</p>

<p style="user-select: auto !important;">Moist has figured out that the robot's sorting mechanism is very primitive. It scans the deck of cards from top to bottom. Whenever it finds a card that is lexicographically smaller than the previous card, it moves that card to its correct place in the stack above. This operation costs \$1, and the robot resumes scanning down towards the bottom of the deck, moving cards one by one until the entire deck is sorted in lexicographical order from top to bottom.</p>

<p style="user-select: auto !important;">As wet luck would have it, Moist is almost broke, but keeping his trading cards in order is the only remaining joy in his miserable life. He needs to know how much it would cost him to use the robot to sort his deck of cards.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>.  <strong style="user-select: auto !important;">T</strong> test cases follow. Each one starts with a line containing a single integer, <strong style="user-select: auto !important;">N</strong>. The next <strong style="user-select: auto !important;">N</strong> lines each contain the name of a figure skater, in order from the top of the deck to the bottom.</p>

<h3 style="user-select: auto !important;">Limits</h3>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 100.</li>
	<li style="user-select: auto !important;">Each name will consist of only letters and the space character.</li>
	<li style="user-select: auto !important;">Each name will contain at most 100 characters.</li>
	<li style="user-select: auto !important;">No name with start or end with a space.</li>
	<li style="user-select: auto !important;">No name will appear more than once in the same test case.</li>
	<li style="user-select: auto !important;">Lexicographically, the space character comes first, then come the upper case letters, then the lower case letters.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of dollars it would cost Moist to use the robot to sort his deck of trading cards.</p>

