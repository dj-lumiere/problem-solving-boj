# [Silver III] Matrix Chain Multiplication - 6604 

[문제 링크](https://www.acmicpc.net/problem/6604) 

### 성능 요약

메모리: 128548 KB, 시간: 228 ms

### 분류

자료 구조, 파싱, 스택, 문자열

### 제출 일자

2024년 12월 25일 17:04:00

### 문제 설명

<p style="user-select: auto !important;">Suppose you have to evaluate an expression like A*B*C*D*E where A,B,C,D and E are matrices.</p>

<p style="user-select: auto !important;">Since matrix multiplication is associative, the order in which multiplications are performed is arbitrary. However, the number of elementary multiplications needed strongly depends on the evaluation order you choose.</p>

<p style="user-select: auto !important;">For example, let A be a 50*10 matrix, B a 10*20 matrix and C a 20*5 matrix.</p>

<p style="user-select: auto !important;">There are two different strategies to compute A*B*C, namely (A*B)*C and A*(B*C).</p>

<p style="user-select: auto !important;">The first one takes 15000 elementary multiplications, but the second one only 3500.</p>

<p style="user-select: auto !important;">Your job is to write a program that determines the number of elementary multiplications needed for a given evaluation strategy.</p>

### 입력 

 <p style="user-select: auto !important;">Input consists of two parts: a list of matrices and a list of expressions.</p>

<p style="user-select: auto !important;">The first line of the input file contains one integer <em style="user-select: auto !important;">n</em> (1 n n lines each contain one capital letter, specifying the name of the matrix, and two integers, specifying the number of rows and columns of the matrix.</p>

<p style="user-select: auto !important;">The second part of the input file strictly adheres to the following syntax (given in EBNF):</p>

<pre style="user-select: auto !important;">SecondPart = Line { Line } <EOF>
Line       = Expression <CR>
Expression = Matrix | "(" Expression Expression ")"
Matrix     = "A" | "B" | "C" | ... | "X" | "Y" | "Z"</pre>

### 출력 

 <p style="user-select: auto !important;">For each expression found in the second part of the input file, print one line containing the word "error" if evaluation of the expression leads to an error due to non-matching matrices. Otherwise print one line containing the number of elementary multiplications needed to evaluate the expression in the way specified by the parentheses.</p>

