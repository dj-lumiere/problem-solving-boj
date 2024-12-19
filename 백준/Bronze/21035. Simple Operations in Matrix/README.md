# [Bronze I] Simple Operations in Matrix - 21035 

[문제 링크](https://www.acmicpc.net/problem/21035) 

### 성능 요약

메모리: 128808 KB, 시간: 232 ms

### 분류

구현

### 제출 일자

2024년 12월 19일 18:42:05

### 문제 설명

<p style="user-select: auto !important;">Matrix is a mathematical object which arranges data into a rectangular array of <em style="user-select: auto !important;">N</em> rows and <em style="user-select: auto !important;">M</em> columns. The rows are indexed from 1 to <em style="user-select: auto !important;">N</em>, while the columns are indexed from 1 to <em style="user-select: auto !important;">M</em>. Matrix is very powerful and extremely useful in many applications. In this problem, we are going to focus on two simple operations in matrix: row addition and column addition.</p>

<p style="user-select: auto !important;">You are given a matrix of integers of <em style="user-select: auto !important;">N</em> rows and <em style="user-select: auto !important;">M</em> columns, and <em style="user-select: auto !important;">Q</em> queries of the following format:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">row</code> <em style="user-select: auto !important;">k</em> <em style="user-select: auto !important;">val</em>: add each element on the <em style="user-select: auto !important;">k</em>-th row by <em style="user-select: auto !important;">val</em>,</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">col</code> <em style="user-select: auto !important;">k</em> <em style="user-select: auto !important;">val</em>: add each element on the <em style="user-select: auto !important;">k</em>-th column by <em style="user-select: auto !important;">val</em>.</li>
</ul>

<p style="user-select: auto !important;">Your task is to output the following three numbers after all queries have been performed:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">sum: the sum of all elements in the matrix,</li>
	<li style="user-select: auto !important;">min: the value of the smallest element in the matrix,</li>
	<li style="user-select: auto !important;">max: the value of the largest element in the matrix.</li>
</ul>

<p style="user-select: auto !important;">See the sample input for clarity</p>

### 입력 

 <p style="user-select: auto !important;">The first line contains two integers: <em style="user-select: auto !important;">N</em> <em style="user-select: auto !important;">M</em> (1 ≤ <em style="user-select: auto !important;">N</em>, <em style="user-select: auto !important;">M</em> ≤ 50) denoting the size of the matrix (number of rows and columns, respectively). The next <em style="user-select: auto !important;">N</em> lines, each contains <em style="user-select: auto !important;">M</em> integers: <em style="user-select: auto !important;">A<sub style="user-select: auto !important;">i</sub></em><sub style="user-select: auto !important;">,<em style="user-select: auto !important;">j</em></sub> (-100 ≤ <em style="user-select: auto !important;">A<sub style="user-select: auto !important;">i</sub></em><sub style="user-select: auto !important;">,<em style="user-select: auto !important;">j</em></sub> ≤ 100) denoting the matrix element at the <em style="user-select: auto !important;">i</em>-th row and <em style="user-select: auto !important;">j</em>-th column for 1 ≤ <em style="user-select: auto !important;">i</em> ≤ <em style="user-select: auto !important;">N</em> and 1 ≤ <em style="user-select: auto !important;">j</em> ≤ <em style="user-select: auto !important;">M</em>, respectively. The next line contains an integer: <em style="user-select: auto !important;">Q</em> (0 ≤ <em style="user-select: auto !important;">Q</em> ≤ 100) denoting the number of queries. The next <em style="user-select: auto !important;">Q</em> lines, each contains a query in one of the following format:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">row</code> <em style="user-select: auto !important;">k</em> <em style="user-select: auto !important;">val</em> (1 ≤ <em style="user-select: auto !important;">k</em> ≤ <em style="user-select: auto !important;">N</em>; -100 ≤ <em style="user-select: auto !important;">val</em> ≤ 100)</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">col</code> <em style="user-select: auto !important;">k</em> <em style="user-select: auto !important;">val</em> (1 ≤ <em style="user-select: auto !important;">k</em> ≤ <em style="user-select: auto !important;">M</em>; -100 ≤ <em style="user-select: auto !important;">val</em> ≤ 100)</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">The output contains three integers (each separated by a single space) in a single line: sum min max, as described in the problem statement.</p>

