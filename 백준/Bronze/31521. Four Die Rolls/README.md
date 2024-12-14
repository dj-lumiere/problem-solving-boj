# [Bronze I] Four Die Rolls - 31521 

[문제 링크](https://www.acmicpc.net/problem/31521) 

### 성능 요약

메모리: 128160 KB, 시간: 232 ms

### 분류

브루트포스 알고리즘, 조합론, 구현, 수학

### 제출 일자

2024년 12월 14일 22:49:15

### 문제 설명

<p>Ashley and Brandon are playing a game where they roll a six-sided dice four times. Each integer from $1$ to $6$ is on one face of the dice and all values are equally likely to appear. Each time they roll the dice, they write down the value that shows on the top face of the dice, eventually forming a four-digit integer.</p>

<p>Ashley wins if all four digits in the integers are different. Otherwise, Brandon wins.</p>

<p>The dice has been rolled from $1$ to $3$ times so far. Compute the number of different ways to roll the remaining times such that Ashley wins, and the number of different ways to roll the remaining dice such that Brandon wins. Two ways are different if the integers formed are different - for example, rolling a $1$, then a $2$, then a $3$, then a $4$ forms the integer $1234$, and is different from rolling a $1$, then a $2$, then a $4$, then a $3$, which would form the integer $1243$.</p>

### 입력 

 <p>The first line contains $n$ ($1 \le n \le 3$), which is the number of times the dice have been rolled so far.</p>

<p>The next line contains $n$ integers ranging from $1$ to $6$, which are the first $n$ rolls of the dice in order.</p>

### 출력 

 <p>Output two space-separated integers on one line, which are the number of ways to roll the remaining times such that Ashley wins, and the number of ways to roll the remaining dice such that Brandon wins.</p>

