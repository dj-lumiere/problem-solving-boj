# [Bronze I] Vestigium - 27797 

[문제 링크](https://www.acmicpc.net/problem/27797) 

### 성능 요약

메모리: 161616 KB, 시간: 196 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 12월 4일 23:25:39

### 문제 설명

<p style="user-select: auto !important;">Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.</p>

<p style="user-select: auto !important;">The <i style="user-select: auto !important;">trace</i> of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).</p>

<p style="user-select: auto !important;">An <b style="user-select: auto !important;">N</b>-by-<b style="user-select: auto !important;">N</b> square matrix is a <i style="user-select: auto !important;">Latin square</i> if each cell contains one of <b style="user-select: auto !important;">N</b> different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the <b style="user-select: auto !important;">N</b> values are the integers between 1 and <b style="user-select: auto !important;">N</b>.</p>

<p style="user-select: auto !important;">Given a matrix that contains only integers between 1 and <b style="user-select: auto !important;">N</b>, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <b style="user-select: auto !important;">T</b>. <b style="user-select: auto !important;">T</b> test cases follow. Each starts with a line containing a single integer <b style="user-select: auto !important;">N</b>: the size of the matrix to explore. Then, <b style="user-select: auto !important;">N</b> lines follow. The i-th of these lines contains <b style="user-select: auto !important;">N</b> integers <b style="user-select: auto !important;">M<sub style="user-select: auto !important;">i,1</sub></b>, <b style="user-select: auto !important;">M<sub style="user-select: auto !important;">i,2</sub></b> ..., <b style="user-select: auto !important;">M<sub style="user-select: auto !important;">i,N</sub></b>. <b style="user-select: auto !important;">M<sub style="user-select: auto !important;">i,j</sub></b> is the integer in the i-th row and j-th column of the matrix.</p>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing <code style="user-select: auto !important;">Case #x: k r c</code>, where <code style="user-select: auto !important;">x</code> is the test case number (starting from 1), <code style="user-select: auto !important;">k</code> is the trace of the matrix, <code style="user-select: auto !important;">r</code> is the number of rows of the matrix that contain repeated elements, and <code style="user-select: auto !important;">c</code> is the number of columns of the matrix that contain repeated elements.</p>

