# [Silver IV] Maximizing Productivity - 31650 

[문제 링크](https://www.acmicpc.net/problem/31650) 

### 성능 요약

메모리: 198212 KB, 시간: 412 ms

### 분류

이분 탐색, 정렬

### 제출 일자

2024년 12월 21일 15:20:02

### 문제 설명

<p>Farmer John has $N$ ($1 \leq N \leq 2 \cdot 10^5$) farms, numbered from $1$ to $N$. It is known that FJ closes farm $i$ at time $c_i$. Bessie wakes up at time $S$, and wants to maximize the productivity of her day by visiting as many farms as possible before they close. She plans to visit farm $i$ on time $t_i + S$. Bessie must arrive at a farm strictly before Farmer John closes it to actually visit it.</p>

<p>Bessie has $Q$ $(1 \leq Q \leq 2 \cdot 10^5)$ queries. For each query, she gives you two integers $S$ and $V$. For each query, output whether Bessie can visit at least $V$ farms if she wakes up at time $S$.</p>

### 입력 

 <p>The first line consists of $N$ and $Q$.</p>

<p>The second line consists of $c_1, c_2, c_3 \dots c_N$ ($1 \leq c_i \leq 10^6$).</p>

<p>The third line consists of $t_1, t_2, t_3 \dots t_N$ ($1 \leq t_i \leq 10^6$).</p>

<p>The next $Q$ lines each consist of two integers $V$ ($1 \leq V \leq N$) and $S$ ($1 \leq S \leq 10^6$).</p>

### 출력 

 <p>For each of the $Q$ queries, output YES or NO on a new line.</p>

