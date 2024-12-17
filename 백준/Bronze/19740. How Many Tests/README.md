# [Bronze I] How Many Tests - 19740 

[문제 링크](https://www.acmicpc.net/problem/19740) 

### 성능 요약

메모리: 127496 KB, 시간: 220 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 12월 17일 16:51:07

### 문제 설명

<p style="user-select: auto !important;">When judges prepare tests for the programming contest problem, they number tests from $1$ to $n$.</p>

<p style="user-select: auto !important;">It is convenient if the files with tests are shown in their correct order, from $1$ to $n$. But file managers sort files by their names as strings, so if the name of the test file is equal to its number, the file order is not correct, for example <<<code style="user-select: auto !important;">10</code>>> goes before <<<code style="user-select: auto !important;">2</code>>>.  </p>

<p style="user-select: auto !important;">To avoid such problem, file names are prepended with leading zeroes. Judges use minimal possible number of leading zeroes to make names of all files have the same length. For example, if the problem has $10$ tests, the names of the files with tests are <<<code style="user-select: auto !important;">01</code>>>, <<<code style="user-select: auto !important;">02</code>>>, <<<code style="user-select: auto !important;">03</code>>>, <<<code style="user-select: auto !important;">04</code>>>, <<<code style="user-select: auto !important;">05</code>>>, <<<code style="user-select: auto !important;">06</code>>>, <<<code style="user-select: auto !important;">07</code>>>, <<<code style="user-select: auto !important;">08</code>>>, <<<code style="user-select: auto !important;">09</code>>> and <<<code style="user-select: auto !important;">10</code>>>.</p>

<p style="user-select: auto !important;">Andrew is an experienced judge, so he always uses the described way to name the files with tests. Recently he has found some files with tests of some ancient problem at his old hard drive. Unfortunately, the drive is damaged, so some tests are missing. Help Andrew to find out how many tests could be there in the problem. He wants to know the minimal and the maximal possible number of tests.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of input contains an integer $k$  --- the number of files ($1 \le k \le 1000$). The following $k$ lines contain file names. All these lines are non-empty, have equal length that doesn't exceed $9$. File names are distinct, they only contain digits. No file name contains only zeroes.</p>

### 출력 

 <p style="user-select: auto !important;">Output two integers: the minimal and the maximal number of tests that the problem could have.</p>

