# [Silver III] Binary Seating - 20214 

[문제 링크](https://www.acmicpc.net/problem/20214) 

### 성능 요약

메모리: 128156 KB, 시간: 236 ms

### 분류

조합론, 기댓값의 선형성, 수학, 확률론, 정렬

### 제출 일자

2024년 12월 19일 18:54:46

### 문제 설명

<p style="user-select: auto !important;">By accident, two rooms (room $0$ and room $1$) got booked for the theoretical exam of the B++ Applied Programming Course and both were communicated to the students. Now students might go to either of the rooms, and as a student assistant your job is to supervise room $1$. Since you assisted all these students during the course, you know how much time each student will need to finish the exam. Already before the exam you are eager to go home, but you can only leave when all of the students in your examination room have finished. You assume that every student chooses one of the exam rooms with equal probability, independent of the other students. After how much time do you expect to be able to leave?</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">A line with an integer $n$ ($1 \leq n \leq 40$), the number of students.</li>
	<li style="user-select: auto !important;">A line with $n$ integers $t_1, \ldots, t_n$ ($1 \leq t_i \leq 1000$): $t_i$ is the time it takes for the $i$th student to finish the exam and leave.</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">Output the expected time before you can leave. Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

