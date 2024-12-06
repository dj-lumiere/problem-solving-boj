# [Bronze I] Steed 2: Cruise Control (Large) - 14804 

[문제 링크](https://www.acmicpc.net/problem/14804) 

### 성능 요약

메모리: 111244 KB, 시간: 92 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 12월 6일 21:09:33

### 문제 설명

<p style="user-select: auto !important;">Annie is a bus driver with a high-stress job. She tried to unwind by going on a Caribbean cruise, but that also turned out to be stressful, so she has recently taken up horseback riding.</p>

<p style="user-select: auto !important;">Today, Annie is riding her horse to the east along a long and narrow one-way road that runs west to east. She is currently at kilometer 0 of the road, and her destination is at kilometer <strong style="user-select: auto !important;">D</strong>; kilometers along the road are numbered from west to east.</p>

<p style="user-select: auto !important;">There are <strong style="user-select: auto !important;">N</strong> other horses traveling east on the same road; all of them will go on traveling forever, and all of them are currently between Annie's horse and her destination. The i-th of these horses is initially at kilometer <strong style="user-select: auto !important;">K<sub style="user-select: auto !important;">i</sub></strong> and is traveling at its maximum speed of <strong style="user-select: auto !important;">S<sub style="user-select: auto !important;">i</sub></strong>kilometers per hour.</p>

<p style="user-select: auto !important;">Horses are very polite, and a horse H<sub style="user-select: auto !important;">1</sub> will not pass (move ahead of) another horse H<sub style="user-select: auto !important;">2</sub>that started off ahead of H<sub style="user-select: auto !important;">1</sub>. (Two or more horses can share the same position for any amount of time; you may consider the horses to be single points.) Horses (other than Annie's) travel at their maximum speeds, except that whenever a horse H<sub style="user-select: auto !important;">1</sub> catches up to another slower horse H<sub style="user-select: auto !important;">2</sub>, H<sub style="user-select: auto !important;">1</sub> reduces its speed to match the speed of H<sub style="user-select: auto !important;">2</sub>.</p>

<p style="user-select: auto !important;">Annie's horse, on the other hand, does not have a maximum speed and can travel at any speed that Annie chooses, as long as it does not pass another horse. To ensure a smooth ride for her and her horse, Annie wants to choose a single constant "cruise control" speed for her horse for the entire trip, from her current position to the destination, such that her horse will not pass any other horses. What is the maximum such speed that she can choose?</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>; <strong style="user-select: auto !important;">T</strong> test cases follow. Each test case begins with two integers <strong style="user-select: auto !important;">D</strong> and <strong style="user-select: auto !important;">N</strong>: the destination position of all of the horses (in kilometers) and the number of other horses on the road. Then, <strong style="user-select: auto !important;">N</strong> lines follow. The i-th of those lines has two integers <strong style="user-select: auto !important;">K<sub style="user-select: auto !important;">i</sub></strong> and <strong style="user-select: auto !important;">S<sub style="user-select: auto !important;">i</sub></strong>: the initial position (in kilometers) and maximum speed (in kilometers per hour) of the i-th of the other horses on the road.</p>

<p style="user-select: auto !important;">Limits</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 100.</li>
	<li style="user-select: auto !important;">0 < <strong style="user-select: auto !important;">K<sub style="user-select: auto !important;">i</sub></strong> < <strong style="user-select: auto !important;">D</strong> ≤ 10<sup style="user-select: auto !important;">9</sup>, for all i.</li>
	<li style="user-select: auto !important;"><strong style="user-select: auto !important;">K<sub style="user-select: auto !important;">i</sub></strong> ≠ <strong style="user-select: auto !important;">K<sub style="user-select: auto !important;">j</sub></strong>, for all i ≠ j. (No two horses start in the same position.)</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">S<sub style="user-select: auto !important;">i</sub></strong> ≤ 10000.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">N</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing <code style="user-select: auto !important;">Case #x: y</code>, where <code style="user-select: auto !important;">x</code> is the test case number (starting from 1) and <code style="user-select: auto !important;">y</code> is the maximum constant speed (in kilometers per hour) that Annie can use without colliding with other horses. <code style="user-select: auto !important;">y</code> will be considered correct if it is within an absolute or relative error of 10<sup style="user-select: auto !important;">-6</sup> of the correct answer.</p>

