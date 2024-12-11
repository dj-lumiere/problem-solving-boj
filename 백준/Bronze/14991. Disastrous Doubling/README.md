# [Bronze II] Disastrous Doubling - 14991 

[문제 링크](https://www.acmicpc.net/problem/14991) 

### 성능 요약

메모리: 147716 KB, 시간: 524 ms

### 분류

임의 정밀도 / 큰 수 연산, 사칙연산, 구현, 수학, 시뮬레이션

### 제출 일자

2024년 12월 11일 09:45:43

### 문제 설명

<p style="user-select: auto !important;">A scientist, E. Collie, is going to do some experiments with bacteria. Right now, she has one bacterium. She already knows that this species of bacteria doubles itself every hour. Hence, after one hour there will be 2 bacteria. E.</p>

<p style="user-select: auto !important;">E. Collie will do one experiment every hour, for n consecutive hours. She starts the first experiment exactly one hour after the first bacterium starts growing. In experiment i she will need b<sub style="user-select: auto !important;">i</sub> bacteria.</p>

<p style="user-select: auto !important;">How many bacteria will be left directly after starting the last experiment? If at any point there are not enough bacteria to do the experiment, print “error”.</p>

<p style="user-select: auto !important;">Since the answer may be very large, please print it modulo 10<sup style="user-select: auto !important;">9</sup> + 7.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of two lines.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">The first line contains an integer 1 ≤ n ≤ 10<sup style="user-select: auto !important;">5</sup>, the number of experiments.</li>
	<li style="user-select: auto !important;">The second line contains n integers b<sub style="user-select: auto !important;">1</sub>, . . . , b<sub style="user-select: auto !important;">n</sub>, where 0 ≤ b<sub style="user-select: auto !important;">i</sub> ≤ 2<sup style="user-select: auto !important;">60</sup> is the number of bacteria used in the ith experiment.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">Output a single line containing the number of bacteria that remains after doing all the experiments, or “error”.</p>

