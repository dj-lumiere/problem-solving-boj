# [Bronze I] Knockout Racing - 10598 

[문제 링크](https://www.acmicpc.net/problem/10598) 

### 성능 요약

메모리: 129344 KB, 시간: 264 ms

### 분류

구현, 수학

### 제출 일자

2024년 12월 23일 09:42:06

### 문제 설명

<p style="user-select: auto !important;">The races became more popular than ever at Pandora planet. But these races are quite unusual. There are n cars participating in a race on the long straight track. Each car moves with a speed of 1 meter per second. Track has coordinates in meters.</p>

<p style="user-select: auto !important;">The car number i moves between two points on the track with coordinates a<sub style="user-select: auto !important;">i</sub> and b<sub style="user-select: auto !important;">i</sub> starting at the second 0 in the point a<sub style="user-select: auto !important;">i</sub>. The car moves from a<sub style="user-select: auto !important;">i</sub> to b<sub style="user-select: auto !important;">i</sub>, then from b<sub style="user-select: auto !important;">i</sub> to a<sub style="user-select: auto !important;">i</sub>, then from a<sub style="user-select: auto !important;">i</sub> to b<sub style="user-select: auto !important;">i</sub> again, and so on.</p>

<p style="user-select: auto !important;">Handsome Mike wants to knock some cars out of the race using dynamite. Thus he has m questions. The question number j is: what is the number of cars in the coordinates between x<sub style="user-select: auto !important;">j</sub> and y<sub style="user-select: auto !important;">j</sub> inclusive after t<sub style="user-select: auto !important;">j</sub> seconds from the start?</p>

<p style="user-select: auto !important;">Your task is to answer Mike’s questions.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input file contains two integers n and m (1 ≤ n, m ≤ 1000) — the number of cars in the race and the number of questions.</p>

<p style="user-select: auto !important;">Each of the following n lines contains a description of the car: two integers a<sub style="user-select: auto !important;">i</sub> and b<sub style="user-select: auto !important;">i</sub> (0 ≤ a<sub style="user-select: auto !important;">i</sub>, b<sub style="user-select: auto !important;">i</sub> ≤ 10<sup style="user-select: auto !important;">9</sup>, a<sub style="user-select: auto !important;">i</sub> ≠ b<sub style="user-select: auto !important;">i</sub>) — the coordinates of the two points between which the car i moves.</p>

<p style="user-select: auto !important;">Each of the following m lines contains a description of the question: three integers x<sub style="user-select: auto !important;">j</sub> , y<sub style="user-select: auto !important;">j</sub> , and t<sub style="user-select: auto !important;">j</sub> (0 ≤ x<sub style="user-select: auto !important;">j</sub> ≤ y<sub style="user-select: auto !important;">j</sub> ≤ 10<sup style="user-select: auto !important;">9</sup>, 0 ≤ t<sub style="user-select: auto !important;">j</sub> ≤ 10<sup style="user-select: auto !important;">9</sup>) — the coordinate range and the time for the question j.</p>

### 출력 

 <p style="user-select: auto !important;">Write m lines to the output file. Each line must contain one integer — the answer to the corresponding question in order they are given in the input file.</p>

